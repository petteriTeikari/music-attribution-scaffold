#!/usr/bin/env python3
"""
Resize and convert PNG images to optimized JPEGs with rounded corners.

This script converts large PNG figures (~7MB each) to web-friendly JPEGs
(~150-200KB each) suitable for embedding in documentation.

Features:
- Resize to 1600px width (maintains aspect ratio)
- JPEG compression at 85% quality
- 24px rounded corners with white (#FFFFFF) background
- Batch processing with progress tracking

Usage:
    python resize_and_convert.py                    # Process all PNGs
    python resize_and_convert.py --dry-run          # Preview without saving
    python resize_and_convert.py --input fig-tech-01-attribution-pipeline.png  # Single file
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw
except ImportError:
    print("Error: Pillow is required. Install with: uv add pillow --group dev")
    sys.exit(1)


# Configuration
DEFAULT_WIDTH = 1600
JPEG_QUALITY = 85
CORNER_RADIUS = 24
BACKGROUND_COLOR = (255, 255, 255)  # White


def add_rounded_corners(image: Image.Image, radius: int) -> Image.Image:
    """
    Add rounded corners to an image with a white background.

    Args:
        image: PIL Image (RGBA mode expected)
        radius: Corner radius in pixels

    Returns:
        Image with rounded corners, composited onto white background
    """
    # Ensure RGBA mode for alpha channel manipulation
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    width, height = image.size

    # Create a mask for rounded corners
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)

    # Draw rounded rectangle on mask (white = visible)
    draw.rounded_rectangle([(0, 0), (width - 1, height - 1)], radius=radius, fill=255)

    # Create white background
    background = Image.new("RGBA", (width, height), (*BACKGROUND_COLOR, 255))

    # Composite: place image on white background using rounded mask
    background.paste(image, (0, 0), mask)

    return background


def resize_image(image: Image.Image, target_width: int) -> Image.Image:
    """
    Resize image to target width while maintaining aspect ratio.

    Args:
        image: PIL Image
        target_width: Desired width in pixels

    Returns:
        Resized image
    """
    width, height = image.size

    if width <= target_width:
        # Don't upscale
        return image

    # Calculate new height maintaining aspect ratio
    ratio = target_width / width
    target_height = int(height * ratio)

    # Use high-quality downsampling
    return image.resize((target_width, target_height), Image.Resampling.LANCZOS)


# Placeholder detection threshold (placeholders are ~631 bytes)
PLACEHOLDER_THRESHOLD_BYTES = 2000


def is_placeholder(file_path: Path) -> bool:
    """
    Check if a file is a placeholder image (tiny file).

    Placeholders are 16x16 black images at ~631 bytes.
    Real converted images are 100KB+.
    """
    if not file_path.exists():
        return False
    return file_path.stat().st_size < PLACEHOLDER_THRESHOLD_BYTES


def process_image(
    input_path: Path,
    output_path: Path,
    target_width: int = DEFAULT_WIDTH,
    quality: int = JPEG_QUALITY,
    corner_radius: int = CORNER_RADIUS,
    dry_run: bool = False,
) -> dict:
    """
    Process a single image: resize, add rounded corners, convert to JPEG.

    Args:
        input_path: Path to input PNG
        output_path: Path for output JPEG
        target_width: Target width in pixels
        quality: JPEG quality (1-100)
        corner_radius: Corner radius in pixels
        dry_run: If True, don't save, just report what would happen

    Returns:
        Dict with processing stats
    """
    # Load image
    with Image.open(input_path) as img:
        original_size = input_path.stat().st_size
        original_dimensions = img.size

        # Convert to RGBA for processing
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        # Resize
        resized = resize_image(img, target_width)
        new_dimensions = resized.size

        # Add rounded corners
        rounded = add_rounded_corners(resized, corner_radius)

        # Convert to RGB for JPEG (no alpha channel)
        rgb_image = rounded.convert("RGB")

        if not dry_run:
            # Ensure output directory exists
            output_path.parent.mkdir(parents=True, exist_ok=True)

            # Save as JPEG
            rgb_image.save(output_path, "JPEG", quality=quality, optimize=True)
            new_size = output_path.stat().st_size
        else:
            new_size = 0  # Unknown in dry run

    return {
        "input": input_path.name,
        "output": output_path.name,
        "original_size_mb": original_size / (1024 * 1024),
        "new_size_kb": new_size / 1024 if not dry_run else None,
        "original_dimensions": original_dimensions,
        "new_dimensions": new_dimensions,
        "compression_ratio": original_size / new_size if not dry_run and new_size > 0 else None,
    }


def find_pngs(input_dir: Path) -> list[Path]:
    """Find all PNG files in directory."""
    return sorted(input_dir.glob("*.png"))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resize and convert PNG figures to optimized JPEGs with rounded corners."
    )
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path(__file__).parent.parent / "generated",
        help="Directory containing PNG files (default: ../generated)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path(__file__).parent.parent / "assets",
        help="Directory for output JPEGs (default: ../assets)",
    )
    parser.add_argument("--input", type=str, help="Process single file (filename only, not path)")
    parser.add_argument(
        "--width",
        type=int,
        default=DEFAULT_WIDTH,
        help=f"Target width in pixels (default: {DEFAULT_WIDTH})",
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=JPEG_QUALITY,
        help=f"JPEG quality 1-100 (default: {JPEG_QUALITY})",
    )
    parser.add_argument(
        "--radius",
        type=int,
        default=CORNER_RADIUS,
        help=f"Corner radius in pixels (default: {CORNER_RADIUS})",
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without saving files")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force reconversion even if output exists (and is not a placeholder)",
    )

    args = parser.parse_args()

    # Resolve paths
    input_dir = args.input_dir.resolve()
    output_dir = args.output_dir.resolve()

    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)

    # Find files to process
    if args.input:
        input_files = [input_dir / args.input]
        if not input_files[0].exists():
            print(f"Error: File not found: {input_files[0]}")
            sys.exit(1)
    else:
        input_files = find_pngs(input_dir)

    if not input_files:
        print("No PNG files found to process.")
        sys.exit(0)

    print(f"{'[DRY RUN] ' if args.dry_run else ''}Processing {len(input_files)} files...")
    print(f"  Input:  {input_dir}")
    print(f"  Output: {output_dir}")
    print(f"  Width:  {args.width}px")
    print(f"  Quality: {args.quality}%")
    print(f"  Corner radius: {args.radius}px")
    print()

    total_original = 0.0
    total_new = 0.0
    results = []

    skipped = 0
    for i, input_path in enumerate(input_files, 1):
        output_path = output_dir / (input_path.stem + ".jpg")

        # Check if we should skip this file
        if output_path.exists() and not args.force and not args.dry_run:
            if is_placeholder(output_path):
                # It's a placeholder - we should convert
                status = "PLACEHOLDER->CONVERT"
            else:
                # Already converted - skip
                skipped += 1
                print(f"[{i}/{len(input_files)}] SKIP (already converted): {input_path.name}")
                continue
        else:
            status = "NEW" if not output_path.exists() else "FORCE"

        try:
            result = process_image(
                input_path,
                output_path,
                target_width=args.width,
                quality=args.quality,
                corner_radius=args.radius,
                dry_run=args.dry_run,
            )
            results.append(result)

            total_original += result["original_size_mb"]
            if result["new_size_kb"]:
                total_new += result["new_size_kb"]

            # Progress output
            orig_dim = f"{result['original_dimensions'][0]}x{result['original_dimensions'][1]}"
            new_dim = f"{result['new_dimensions'][0]}x{result['new_dimensions'][1]}"

            if args.dry_run:
                print(f"[{i}/{len(input_files)}] {result['input']}")
                print(f"         {result['original_size_mb']:.1f}MB ({orig_dim}) -> {new_dim}")
            else:
                print(f"[{i}/{len(input_files)}] {result['input']} [{status}]")
                print(
                    f"         {result['original_size_mb']:.1f}MB -> {result['new_size_kb']:.0f}KB "
                    f"({result['compression_ratio']:.0f}x compression)"
                )
                print(f"         {orig_dim} -> {new_dim}")

        except Exception as e:
            print(f"[{i}/{len(input_files)}] ERROR: {input_path.name}")
            print(f"         {e}")

    # Summary
    print()
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(f"Files processed: {len(results)}")
    print(f"Files skipped:   {skipped} (already converted)")
    print(f"Total original:  {total_original:.1f} MB")
    if not args.dry_run and total_original > 0:
        print(f"Total new:       {total_new / 1024:.1f} MB")
        print(
            f"Space saved:     {total_original - (total_new / 1024):.1f} MB "
            f"({(1 - total_new / 1024 / total_original) * 100:.0f}%)"
        )

    if args.dry_run:
        print()
        print("This was a dry run. No files were modified.")
        print("Run without --dry-run to process files.")


if __name__ == "__main__":
    main()
