# resize-figures

Resize and convert PNG figures to web-optimized JPEGs with rounded corners.

## Trigger

Use when user asks to:
- Resize figures/images for documentation
- Convert PNGs to JPEGs
- Optimize figure file sizes
- Add rounded corners to images

## Usage

```bash
# Process all figures
uv run python docs/figures/scripts/resize_and_convert.py

# Dry run (preview)
uv run python docs/figures/scripts/resize_and_convert.py --dry-run

# Single file
uv run python docs/figures/scripts/resize_and_convert.py --input fig-tech-01-attribution-pipeline.png

# Force reconvert
uv run python docs/figures/scripts/resize_and_convert.py --force
```

## Configuration

- **Input**: `docs/figures/generated/*.png` (raw Nano Banana Pro output)
- **Output**: `docs/figures/assets/*.jpg` (web-optimized)
- **Width**: 1600px (maintains aspect ratio)
- **Quality**: 85% JPEG
- **Corners**: 24px radius with white background

## Typical Results

- Input: ~7MB PNG → Output: ~150-200KB JPEG
- Compression ratio: 30-50x
- Total savings: ~50MB → ~1.5MB for 8 figures

## After Running

1. Verify output in `docs/figures/assets/`
2. Update README files to reference `.jpg` files from assets
3. Consider gitignoring the large PNGs in `generated/`
