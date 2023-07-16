import React, { useEffect, useState } from "react";
import * as Form from "@radix-ui/react-form";
import { appStep, uploadedFileName, jobItem, modelAtom } from "@/app/lib/atoms";
import { useAtom } from "jotai";
import Spinner from "./Spinner";
import CheckMark from "./Checkmark";

const JobStatus = () => {
    const [step, setStep] = useAtom(appStep);
    const [job, setJob] = useAtom(jobItem);
    const [model] = useAtom(modelAtom);
    const [uploaded, setUploaded] = useAtom(uploadedFileName);
    const [copySuccess, setCopySuccess] = useState("");
    const [url, setUrl] = useState("");

    const copyToClipboard = async (text: string) => {
        try {
            await navigator.clipboard.writeText(text);
            setCopySuccess("Copied!");
        } catch (err) {
            setCopySuccess("Failed to copy text");
        } finally {
            setTimeout(() => {
                setCopySuccess("");
            }, 3000);
        }
    };

    useEffect(() => {
        setTimeout(() => {
            setJob({
                ...job,
                status: "done",
            });
            setUrl(
                `curl -X POST -H "Content-Type: application/json" -d '{"data":"<data>", "filename": "${uploaded}"}' http://localhost:5000/${model.title.toLowerCase()}`
            );
        }, 5000);
    }, [uploaded]);

    return (
        <div className='flex flex-col w-full'>
            <div className='z-10 items-center justify-center w-full max-w-5xl mb-4 font-mono text-sm lg:flex'>
                <p className='flex justify-center w-full text-lg'>
                    <code className='font-mono font-bold'>
                        {job.status === "done" ? "Your API" : "Progress"}
                    </code>
                </p>
            </div>
            <div className='grid self-center w-64 my-2'>
                {job && (
                    <div className='flex flex-row items-center justify-between w-full pb-2 font-mono'>
                        <div className='text-sm font-medium leading-9 text-white'>
                            {job.label}
                        </div>
                        <div>
                            {job.status === "done" ? (
                                <CheckMark />
                            ) : (
                                <Spinner />
                            )}
                        </div>
                    </div>
                )}
            </div>
            {job.status === "done" && url && (
                <div className='flex flex-col w-full gap-2 mt-4'>
                    <button
                        className='inline-flex items-center justify-center w-full h-48 px-3 py-2 font-mono text-sm font-medium text-white transition-all duration-300 bg-gray-800 border border-gray-600 rounded-lg shadow-sm leading-1 focus:outline-none hover:border-gray-300'
                        onClick={() => copyToClipboard(url)}
                        type='button'
                    >
                        {copySuccess ? "Copied!" : url}
                    </button>
                </div>
            )}
        </div>
    );
};

export default JobStatus;
