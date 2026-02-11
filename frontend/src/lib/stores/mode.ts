import { atom } from "jotai";

export type UserRole = "artist" | "query";

export const userRoleAtom = atom<UserRole>("query");
