/**
 * WebSocket voice client for bidirectional audio streaming.
 *
 * Connects to the voice agent backend WebSocket endpoint and
 * manages connection lifecycle + message passing.
 */

import type { VoiceConnectionState } from "@/lib/stores/voice";

/* ── Types ───────────────────────────────────────────────────── */

/** Re-export for convenience. */
export type ConnectionState = VoiceConnectionState;

export interface VoiceClientConfig {
  /** WebSocket URL (e.g. "ws://localhost:8765/ws/voice"). */
  url: string;
  /** Called when a message arrives from the server. */
  onMessage?: (data: ArrayBuffer | string) => void;
  /** Called when connection state changes. */
  onStateChange?: (state: VoiceConnectionState) => void;
}

export interface VoiceClient {
  /** Open the WebSocket connection. */
  connect: () => Promise<void>;
  /** Close the WebSocket connection. */
  disconnect: () => void;
  /** Send audio data or a text message. */
  send: (data: ArrayBuffer | string) => void;
  /** Check if currently connected. */
  isConnected: () => boolean;
}

/* ── Factory ─────────────────────────────────────────────────── */

export function createVoiceClient(config: VoiceClientConfig): VoiceClient {
  let ws: WebSocket | null = null;
  let state: ConnectionState = "disconnected";

  const setState = (newState: ConnectionState) => {
    state = newState;
    config.onStateChange?.(newState);
  };

  return {
    connect(): Promise<void> {
      return new Promise<void>((resolve, reject) => {
        setState("connecting");

        ws = new WebSocket(config.url);
        ws.binaryType = "arraybuffer";

        ws.onopen = () => {
          setState("connected");
          resolve();
        };

        ws.onclose = () => {
          setState("disconnected");
          ws = null;
        };

        ws.onerror = () => {
          setState("error");
          reject(new Error("WebSocket connection failed"));
        };

        ws.onmessage = (event: MessageEvent) => {
          config.onMessage?.(event.data as ArrayBuffer | string);
        };
      });
    },

    disconnect() {
      if (ws) {
        ws.close();
        ws = null;
      }
      setState("disconnected");
    },

    send(data: ArrayBuffer | string) {
      if (ws && ws.readyState === WebSocket.OPEN) {
        ws.send(data);
      }
    },

    isConnected(): boolean {
      return state === "connected" && ws !== null;
    },
  };
}
