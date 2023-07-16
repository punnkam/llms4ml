import { atom } from "jotai";

export const appStep = atom(0);

export const modelAtom = atom({
    title: "",
    forms: [{}],
});

export const uploadingFile = atom(false);

export const uploadedFileName = atom("");

export const jobItem = atom({
    label: "Generating API",
    status: "pending",
});
