import React, { useState, useCallback } from "react";
import { useDropzone, FileRejection, DropEvent, Accept } from "react-dropzone";
import axios from "axios";
import { useAtom } from "jotai";
import Spinner from "./Spinner";
import { Transition } from "@headlessui/react";
import {
    uploadingFile,
    uploadedFileName,
    modelAtom,
    appStep,
} from "@/app/lib/atoms";

const DragDropText: React.FC = () => {
    const [text, setText] = useState<string>("");
    const [uploading, setUploading] = useAtom(uploadingFile);
    const [uploaded, setUploaded] = useAtom(uploadedFileName);
    const [model] = useAtom(modelAtom);
    const [error, setError] = useState<string>("");
    const [step, setStep] = useAtom(appStep);

    const upload = (formData: any, jsonObject: any) => {
        formData.append("json", jsonObject);
        axios
            .post(
                `http://127.0.0.1:5000/upload?model=${model.title}`,
                formData,
                {
                    headers: { "Content-Type": "multipart/form-data" },
                }
            )
            .then((response) => {
                const { data } = response;
                setUploaded(data);
                setStep(3);
            })
            .catch((error) => {
                // if status code is 400, then output error message
                if (error.response.status === 400) {
                    setError(error.response.data);
                }
                console.log(error.response.data);
            })
            .finally(() => setUploading(false));
    };

    // The function to handle text file upload
    const uploadTextAsFile = useCallback(() => {
        setUploading(true);
        const blob = new Blob([text], { type: "text/plain" });
        const file = new File([blob], `${model.title}.txt`, {
            type: "text/plain",
        }); // New File object

        let formData = new FormData();
        formData.append("file", file);

        const jsonObject = JSON.stringify(model.forms);
        console.log("jsonObject", jsonObject);

        upload(formData, jsonObject);
    }, [text]);

    const onDrop = useCallback(
        (
            acceptedFiles: any[],
            fileRejections: FileRejection[],
            event: DropEvent
        ) => {
            setUploading(true);
            acceptedFiles.forEach((file) => {
                const reader = new FileReader();
                reader.onload = () => {
                    const binaryStr = reader.result;
                    setText(binaryStr ? binaryStr.toString() : "");
                };
                reader.readAsBinaryString(file);
            });
            console.log(acceptedFiles);

            const file = acceptedFiles[0];
            const formData = new FormData();
            formData.append("file", file);
            const jsonObject = JSON.stringify(model.forms);

            upload(formData, jsonObject);
        },
        []
    );
    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        noClick: true,
        accept: {
            ["text/csv"]: [".csv"],
            ["application/json"]: [".json"],
            ["text/xml"]: [".xml"],
        },
    });

    return (
        <>
            <div className='w-64' {...getRootProps()}>
                <div className='z-10 items-center justify-center w-full max-w-5xl mb-4 font-mono text-sm lg:flex'>
                    <p className='flex justify-center w-full text-lg'>
                        <code className='font-mono font-bold'>Input Data</code>
                    </p>
                </div>
                <input {...getInputProps()} />
                {isDragActive ? (
                    <div className='flex flex-col items-center justify-center w-full h-40 gap-2 p-2 px-4 py-3 text-sm text-gray-300 transition-all duration-200 border-b border-gray-300 outline-none focus:border-gray-50 hover:border-gray-500 bg-gradient-to-b from-zinc-200 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:rounded-xl lg:border lg:bg-gray-200 lg:dark:bg-zinc-800/30'>
                        Drop the file here...
                        <svg
                            width='30'
                            height='30'
                            viewBox='0 0 30 30'
                            fill='none'
                            xmlns='http://www.w3.org/2000/svg'
                        >
                            <path
                                d='M4.5 1C4.22386 1 4 1.22386 4 1.5C4 1.77614 4.22386 2 4.5 2H12V13H4.5C4.22386 13 4 13.2239 4 13.5C4 13.7761 4.22386 14 4.5 14H12C12.5523 14 13 13.5523 13 13V2C13 1.44772 12.5523 1 12 1H4.5ZM6.60355 4.89645C6.40829 4.70118 6.09171 4.70118 5.89645 4.89645C5.70118 5.09171 5.70118 5.40829 5.89645 5.60355L7.29289 7H0.5C0.223858 7 0 7.22386 0 7.5C0 7.77614 0.223858 8 0.5 8H7.29289L5.89645 9.39645C5.70118 9.59171 5.70118 9.90829 5.89645 10.1036C6.09171 10.2988 6.40829 10.2988 6.60355 10.1036L8.85355 7.85355C9.04882 7.65829 9.04882 7.34171 8.85355 7.14645L6.60355 4.89645Z'
                                fill='currentColor'
                                className='text-gray-300'
                                fillRule='evenodd'
                                clipRule='evenodd'
                            ></path>
                        </svg>
                    </div>
                ) : (
                    <textarea
                        className='w-full h-40 p-2 px-4 py-3 text-sm transition-all duration-200 border-b border-gray-300 outline-none focus:border-gray-50 hover:border-gray-500 backdrop-blur-2xl dark:border-neutral-800 lg:static lg:rounded-xl lg:border lg:dark:bg-zinc-900'
                        value={text}
                        autoFocus={true}
                        onChange={(e) => setText(e.target.value)}
                        placeholder='Paste your data here or drop a .csv, .json, .xml file.'
                    />
                )}
            </div>

            <div className='flex flex-row w-full gap-2 mt-4'>
                <button
                    className='inline-flex items-center justify-center w-1/2 px-3 py-2 font-mono text-base font-medium text-white transition-all duration-300 bg-gray-800 border border-gray-600 rounded-lg shadow-sm leading-1 focus:outline-none hover:border-gray-300'
                    onClick={() => setStep(1)}
                    type='button'
                >
                    Back
                </button>
                <button
                    className='inline-flex items-center justify-center w-1/2 px-3 py-2 font-mono text-base font-medium text-white transition-all duration-300 bg-gray-800 border border-gray-600 rounded-lg shadow-sm leading-1 focus:outline-none hover:border-gray-300'
                    onClick={() => {
                        if (!text) {
                            setError("Please enter some text.");
                            return;
                        }
                        uploadTextAsFile();
                    }}
                    type='button'
                >
                    {uploading ? <Spinner /> : "Create"}
                </button>
            </div>
            <Transition
                className='flex w-64 text-center'
                show={error.length > 0}
                enter='transition-opacity duration-150'
                enterFrom='opacity-0'
                enterTo='opacity-100'
                leave='transition-opacity duration-150'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <p className='m-auto text-sm text-red-300'>{error}</p>
            </Transition>
        </>
    );
};

export default DragDropText;
