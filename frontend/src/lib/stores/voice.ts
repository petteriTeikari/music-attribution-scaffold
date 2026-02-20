import { atom } from "jotai";

/** Possible states for the voice interaction. */
export type VoiceState = "idle" | "recording" | "processing" | "playing";

/** Connection state for the WebSocket voice client. */
export type VoiceConnectionState =
  | "disconnected"
  | "connecting"
  | "connected"
  | "error";

/** Global voice interaction state atom. */
export const voiceStateAtom = atom<VoiceState>("idle");

/** WebSocket connection state atom. */
export const voiceConnectionAtom = atom<VoiceConnectionState>("disconnected");
