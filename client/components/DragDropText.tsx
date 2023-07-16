import React, { useState, useCallback } from "react";
import { useDropzone, FileRejection, DropEvent, Accept } from "react-dropzone";

interface Props {
    setStep: any;
}

const DragDropText: React.FC<Props> = ({ setStep }: Props) => {
    const [text, setText] = useState<string>("");

    const onDrop = useCallback(
        (
            acceptedFiles: any[],
            fileRejections: FileRejection[],
            event: DropEvent
        ) => {
            acceptedFiles.forEach((file) => {
                const reader = new FileReader();
                reader.onload = () => {
                    const binaryStr = reader.result;
                    setText(binaryStr ? binaryStr.toString() : "");
                };
                reader.readAsBinaryString(file);
            });
            console.log(acceptedFiles);
        },
        []
    );
    const { getRootProps, getInputProps, isDragActive } = useDropzone({
        onDrop,
        accept: {
            ["text/csv"]: [".csv"],
            ["application/json"]: [".json"],
            ["text/xml"]: [".xml"],
        },
    });

    return (
        <>
            <div className='w-64' {...getRootProps()}>
                <div className='z-10 w-full max-w-5xl items-center justify-center font-mono text-sm lg:flex mb-4'>
                    <p className='flex w-full justify-center text-lg'>
                        <code className='font-mono font-bold'>Input Data</code>
                    </p>
                </div>
                <input {...getInputProps()} />
                {isDragActive ? (
                    <div className='flex flex-col items-center gap-2 justify-center h-40 text-sm outline-none focus:border-gray-50 hover:border-gray-500 transition-all duration-200 p-2 border-b border-gray-300 bg-gradient-to-b from-zinc-200 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static w-full lg:rounded-xl lg:border lg:bg-gray-200 py-3 px-4 lg:dark:bg-zinc-800/30 text-gray-300'>
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
                                fill-rule='evenodd'
                                clip-rule='evenodd'
                            ></path>
                        </svg>
                    </div>
                ) : (
                    <textarea
                        className='h-40 text-sm outline-none focus:border-gray-50 hover:border-gray-500 transition-all duration-200 p-2 border-b border-gray-300 backdrop-blur-2xl dark:border-neutral-800  lg:static w-full lg:rounded-xl lg:border py-3 px-4 lg:dark:bg-zinc-900'
                        value={text}
                        autoFocus={true}
                        onChange={(e) => setText(e.target.value)}
                        placeholder='Paste your data here or drop a .csv, .json, .xml file.'
                    />
                )}
            </div>
            <div className='w-full flex flex-row gap-2 mt-4'>
                <button
                    className='w-1/2 inline-flex items-center justify-center rounded-lg py-2 px-3 text-base font-mono font-medium leading-1 bg-gray-800 text-white shadow-sm focus:outline-none transition-all duration-300 border border-gray-600 hover:border-gray-300'
                    onClick={() => setStep(1)}
                    type='button'
                >
                    Back
                </button>
                <button
                    className='w-1/2 inline-flex items-center justify-center rounded-lg py-2 px-3 text-base font-mono font-medium leading-1 bg-gray-800 text-white shadow-sm focus:outline-none transition-all duration-300 border border-gray-600 hover:border-gray-300'
                    onClick={() => setStep(3)}
                    type='button'
                >
                    Create
                </button>
            </div>
        </>
    );
};

export default DragDropText;
