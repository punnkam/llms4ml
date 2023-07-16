"use client";
import { useState } from "react";
import { Transition } from "@headlessui/react";
import RadixForm from "@/components/RadixForm";
import { useAtom } from "jotai";
import { modelAtom } from "./lib/atoms";
import DragDropText from "@/components/DragDropText";

const forms: { [key: string]: any[] } = {
    classification: [
        {
            label: "Task",
            description: "Choose a task",
            error: "Please indicate a task",
        },
        {
            label: "Number of Classes",
            description: "Choose a number of classes",
            error: "Please indicate a number of classes",
        },
        {
            label: "Labels (comma-separated)",
            description: "Choose class labels",
            error: "Please indicate class labels",
        },
    ],
    regression: [
        {
            label: "Task",
            description: "Choose a task",
            error: "Please indicate a task",
        },
        {
            label: "Predictive Variable",
            description: "Choose a predictive variable",
            error: "Please indicate a predictive variable",
        },
    ],
    recommendation: [
        {
            label: "Task",
            description: "Choose a task",
            error: "Please indicate a task",
        },
        {
            label: "Recommendation",
            description: "Choose a recommendation",
            error: "Please indicate a recommendation",
        },
    ],
};

export default function Home() {
    const [formData, setFormData] = useState<any>([]);
    const [model, setModel] = useAtom(modelAtom);
    const [step, setStep] = useState<number>(0);

    const chooseModel = (modelName: string) => {
        const modelForms = forms[modelName];
        setModel({
            title: modelName,
            forms: modelForms,
        });
        setStep(1);
    };

    return (
        <main className='flex min-h-screen flex-col items-center justify-between p-24'>
            <Transition
                className='mx-auto my-16 max-w-md space-y-4'
                show={step == 2}
                enter='transition-all ease-in-out duration-500 delay-[200ms]'
                enterFrom='opacity-0 translate-y-6'
                enterTo='opacity-100 translate-y-0'
                leave='transition-all ease-in-out duration-0'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <DragDropText setStep={setStep} />
            </Transition>
            <Transition
                className='mx-auto my-16 max-w-md space-y-4'
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
                    formData={model.forms as any[]}
                    setFormData={setFormData}
                    setStep={setStep}
                />
            </Transition>
            <Transition
                className='mx-auto my-16 max-w-md space-y-4'
                appear={true}
                show={step == 0}
                enter='transition-all ease-in-out duration-500 delay-[200ms]'
                enterFrom='opacity-0 translate-y-6'
                enterTo='opacity-100 translate-y-0'
                leave='transition-all ease-in-out duration-0'
                leaveFrom='opacity-100'
                leaveTo='opacity-0'
            >
                <div className='z-10 w-full max-w-5xl items-center justify-center font-mono text-sm lg:flex'>
                    <p className='flex w-full justify-center border-b border-gray-300 bg-gradient-to-b from-zinc-200 pb-6 pt-8 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:w-auto  lg:rounded-xl lg:border lg:bg-gray-200 lg:p-4 lg:dark:bg-zinc-800/30'>
                        Start by choosing an&nbsp;
                        <code className='font-mono font-bold'>ML task</code>
                    </p>
                </div>

                <div className='mb-32 mt-8 grid text-center lg:mb-0 lg:grid-rows-4 lg:text-left'>
                    <button
                        onClick={() => chooseModel("classification")}
                        className='text-left group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
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
                        className='text-left group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
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
                        className='text-left group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
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
                  className='group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30'
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
