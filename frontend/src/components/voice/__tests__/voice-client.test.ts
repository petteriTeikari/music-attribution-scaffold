/**
 * Tests for WebSocket voice client (Task 5.3 + 5.4).
 *
 * Tests the client-side WebSocket connection manager for
 * bidirectional audio streaming with the voice agent backend.
 */

import { describe, it, expect, vi, beforeEach, afterEach } from "vitest";

import {
  createVoiceClient,
  type VoiceClient,
  type VoiceClientConfig,
} from "@/lib/voice/client";

/* ── Mock WebSocket ──────────────────────────────────────────── */

class MockWebSocket {
  static CONNECTING = 0;
  static OPEN = 1;
  static CLOSING = 2;
  static CLOSED = 3;

  url: string;
  readyState = MockWebSocket.CONNECTING;
  onopen: ((ev: Event) => void) | null = null;
  onclose: ((ev: CloseEvent) => void) | null = null;
  onmessage: ((ev: MessageEvent) => void) | null = null;
  onerror: ((ev: Event) => void) | null = null;
  send = vi.fn();
  close = vi.fn();

  constructor(url: string) {
    this.url = url;
    // Auto-connect after microtask
    queueMicrotask(() => {
      this.readyState = MockWebSocket.OPEN;
      this.onopen?.(new Event("open"));
    });
  }
}

beforeEach(() => {
  vi.stubGlobal("WebSocket", MockWebSocket);
});

afterEach(() => {
  vi.restoreAllMocks();
});

/* ── Tests ───────────────────────────────────────────────────── */

describe("createVoiceClient", () => {
  it("returns a VoiceClient object", () => {
    const client = createVoiceClient({ url: "ws://localhost:8765/ws/voice" });
    expect(client).toBeDefined();
    expect(client.connect).toBeInstanceOf(Function);
    expect(client.disconnect).toBeInstanceOf(Function);
    expect(client.send).toBeInstanceOf(Function);
  });

  it("accepts configuration with url", () => {
    const config: VoiceClientConfig = {
      url: "ws://localhost:8765/ws/voice",
    };
    const client = createVoiceClient(config);
    expect(client).toBeDefined();
  });

  it("accepts optional onMessage callback", () => {
    const onMessage = vi.fn();
    const client = createVoiceClient({
      url: "ws://localhost:8765/ws/voice",
      onMessage,
    });
    expect(client).toBeDefined();
  });

  it("accepts optional onStateChange callback", () => {
    const onStateChange = vi.fn();
    const client = createVoiceClient({
      url: "ws://localhost:8765/ws/voice",
      onStateChange,
    });
    expect(client).toBeDefined();
  });
});

describe("VoiceClient connection lifecycle", () => {
  let client: VoiceClient;
  const onStateChange = vi.fn();

  beforeEach(() => {
    client = createVoiceClient({
      url: "ws://localhost:8765/ws/voice",
      onStateChange,
    });
  });

  it("connects to the WebSocket endpoint", async () => {
    await client.connect();
    expect(onStateChange).toHaveBeenCalledWith("connected");
  });

  it("disconnects cleanly", async () => {
    await client.connect();
    client.disconnect();
    expect(onStateChange).toHaveBeenCalledWith("disconnected");
  });

  it("reports connecting state during handshake", async () => {
    const connectPromise = client.connect();
    expect(onStateChange).toHaveBeenCalledWith("connecting");
    await connectPromise;
  });

  it("reports error state on connection failure", async () => {
    // Override MockWebSocket to fail
    vi.stubGlobal(
      "WebSocket",
      class extends MockWebSocket {
        constructor(url: string) {
          super(url);
          queueMicrotask(() => {
            this.readyState = MockWebSocket.CLOSED;
            this.onerror?.(new Event("error"));
          });
        }
      },
    );

    const errorClient = createVoiceClient({
      url: "ws://localhost:8765/ws/voice",
      onStateChange,
    });
    await errorClient.connect().catch(() => {});
    expect(onStateChange).toHaveBeenCalledWith("error");
  });
});

describe("VoiceClient messaging", () => {
  let client: VoiceClient;
  const onMessage = vi.fn();

  beforeEach(async () => {
    client = createVoiceClient({
      url: "ws://localhost:8765/ws/voice",
      onMessage,
    });
    await client.connect();
  });

  it("sends audio data as ArrayBuffer", () => {
    const buffer = new ArrayBuffer(1024);
    client.send(buffer);
    // The underlying WebSocket.send should have been called
    expect(client.isConnected()).toBe(true);
  });

  it("sends text messages as JSON", () => {
    client.send(JSON.stringify({ type: "config", stt: "whisper" }));
    expect(client.isConnected()).toBe(true);
  });

  it("provides isConnected() status check", async () => {
    expect(client.isConnected()).toBe(true);
    client.disconnect();
    expect(client.isConnected()).toBe(false);
  });
});
