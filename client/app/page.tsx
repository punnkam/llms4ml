"use client";
import { useState } from "react";
import { Transition } from "@headlessui/react";
import RadixForm from "@/components/RadixForm";
import { useAtom } from "jotai";
import { modelAtom, appStep } from "./lib/atoms";
import DragDropText from "@/components/DragDropText";
import JobStatus from "@/components/JobStatus";

const forms: { [key: string]: any[] } = {
    classification: [
        {
            label: "Task",
            description: "Choose a task",
            error: "Please indicate a task",
            value: "",
        },
        {
            label: "Class name",
            description: "Choose a class name",
            error: "Please indicate a class name",
            value: "",
        },
        {
            label: "Labels (comma-separated)",
            description: "Choose class labels",
            error: "Please indicate class labels",
            value: "",
        },
    ],
    regression: [
        {
            label: "Task",
            description: "Choose a task",
            error: "Please indicate a task",
            value: "",
        },
        {
            label: "Predictive Variable",
            description: "Choose a predictive variable",
            error: "Please indicate a predictive variable",
            value: "",
        },
    ],
    recommendation: [
        {
            label: "Task",
            description: "Choose a task",
            error: "Please indicate a task",
            value: "",
        },
        {
            label: "Recommendation",
            description: "Choose a recommendation",
            error: "Please indicate a recommendation",
            value: "",
        },
    ],
};

export default function Home() {
    const [formData, setFormData] = useState<any>([]);
    const [model, setModel] = useAtom(modelAtom);
    const [step, setStep] = useAtom(appStep);

    const chooseModel = (modelName: string) => {
        const modelForms = forms[modelName];
        setModel({
            title: modelName,
            forms: modelForms,
        });
        setStep(1);
    };

    return (
        <main className='flex flex-col items-center justify-between min-h-screen p-24'>
            <Transition
                className='max-w-md mx-auto my-16 space-y-4'
                show={step == 3}
                enter='transition-all ease-in-out duration-500 delay-[200ms]'
                enterFrom='opacity-0 translate-y-6'
                enterTo='opacity-100 translate-y-0'
                leave='transition-all ease-in-out duration-0'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <JobStatus />
            </Transition>
            <Transition
                className='max-w-md mx-auto my-16 space-y-4'
                show={step == 2}
                enter='transition-all ease-in-out duration-500 delay-[200ms]'
                enterFrom='opacity-0 translate-y-6'
                enterTo='opacity-100 translate-y-0'
                leave='transition-all ease-in-out duration-0'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <DragDropText />
            </Transition>
            <Transition
                className='max-w-md mx-auto my-16 space-y-4'
                show={step == 1}
                enter='transition-all ease-in-out duration-500 delay-[200ms]'
                enterFrom='opacity-0 translate-y-6'
                enterTo='opacity-100 translate-y-0'
                leave='transition-all ease-in-out duration-0'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <RadixForm
                    title={model.title.toUpperCase()[0] + model.title.slice(1)}
                />
            </Transition>
            <Transition
                className='max-w-md mx-auto my-16 space-y-4'
                appear={true}
                show={step == 0}
                enter='transition-all ease-in-out duration-500 delay-[200ms]'
                enterFrom='opacity-0 translate-y-6'
                enterTo='opacity-100 translate-y-0'
                leave='transition-all ease-in-out duration-0'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <div className='z-10 items-center justify-center w-full max-w-5xl font-mono text-sm lg:flex'>
                    <p className='flex justify-center w-full pt-8 pb-6 border-b border-gray-300 bg-gradient-to-b from-zinc-200 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30'>
                        Start by choosing an&nbsp;
                        <code className='font-mono font-bold'>ML task</code>
                    </p>
                </div>

                <div className='grid mt-8 mb-32 text-center lg:mb-0 lg:grid-rows-4 lg:text-left'>
                    <button
                        onClick={() => chooseModel("classification")}
                        className='px-5 py-4 text-left transition-colors border border-transparent rounded-lg group hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
                    >
                        <h2 className={`mb-3 text-2xl font-semibold`}>
                            Classification{" "}
                            <span className='inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none'>
                                -&gt;
                            </span>
                        </h2>
                        <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
                            Automated Text Classification: Categorizing data for
                            efficient analysis.
                        </p>
                    </button>

                    <button
                        onClick={() => chooseModel("regression")}
                        className='px-5 py-4 text-left transition-colors border border-transparent rounded-lg group hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
                    >
                        <h2 className={`mb-3 text-2xl font-semibold`}>
                            Regression{" "}
                            <span className='inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none'>
                                -&gt;
                            </span>
                        </h2>
                        <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
                            Quantitative Predictions: Using AI for predict
                            values.
                        </p>
                    </button>

                    <button
                        onClick={() => chooseModel("recommendation")}
                        className='px-5 py-4 text-left transition-colors border border-transparent rounded-lg group hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
                    >
                        <h2 className={`mb-3 text-2xl font-semibold`}>
                            Recommendation{" "}
                            <span className='inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none'>
                                -&gt;
                            </span>
                        </h2>
                        <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
                            Personalized Suggestions: Align user preferences
                            with AI.
                        </p>
                    </button>

                    {/* <a
                  href='https://vercel.com/new?utm_source=create-next-app&utm_medium=appdir-template&utm_campaign=create-next-app'
                  className='px-5 py-4 transition-colors border border-transparent rounded-lg group hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
                  target='_blank'
                  rel='noopener noreferrer'
              >
                  <h2 className={`mb-3 text-2xl font-semibold`}>
                      Sentiment Analysis{" "}
                      <span className='inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none'>
                          -&gt;
                      </span>
                  </h2>
                  <p className={`m-0 max-w-[30ch] text-sm opacity-50`}>
                      Understanding Emotions: Analyze text to gauge public
                      sentiment and opinions.
                  </p>
              </a> */}
                </div>
            </Transition>
        </main>
    );
}
