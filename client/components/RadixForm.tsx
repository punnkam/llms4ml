import React from "react";
import * as Form from "@radix-ui/react-form";
import { appStep } from "@/app/lib/atoms";
import { useAtom } from "jotai";
import { modelAtom } from "@/app/lib/atoms";

interface FormProps {
    title: string;
}

const FormDemo = ({ title }: FormProps) => {
    const [step, setStep] = useAtom(appStep);
    const [model, setModel] = useAtom(modelAtom);

    return (
        <Form.Root className='w-64'>
            <div className='z-10 items-center justify-center w-full max-w-5xl mb-4 font-mono text-sm lg:flex'>
                <p className='flex justify-center w-full text-lg'>
                    <code className='font-mono font-bold'>{title}</code>
                </p>
            </div>
            <Form.Field className='grid my-2' name='email'>
                {model.forms &&
                    model.forms.map((form: any, index: number) => (
                        <div key={index} className='pb-2 font-mono'>
                            <Form.Label className='text-sm font-medium leading-9 text-white'>
                                {form.label}
                            </Form.Label>
                            <Form.Control asChild>
                                <input
                                    className='w-full p-2 px-4 py-3 text-sm transition-all duration-200 border-b border-gray-300 outline-none focus:border-gray-50 hover:border-gray-500 bg-gradient-to-b from-zinc-200 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static lg:rounded-xl lg:border lg:bg-gray-200 lg:dark:bg-zinc-800/30 '
                                    autoComplete='off'
                                    type='text'
                                    required
                                    onChange={(e: any) =>
                                        setModel((prev: any) => ({
                                            ...prev,
                                            forms: prev.forms.map(
                                                (item: any, i: number) =>
                                                    i === index
                                                        ? {
                                                              ...item,
                                                              value: e.target
                                                                  .value,
                                                          }
                                                        : item
                                            ),
                                        }))
                                    }
                                />
                            </Form.Control>
                            {/* <Form.Message
                            match='valueMissing'
                            className='text-sm text-white opacity-80'
                        >
                            {form.description}
                        </Form.Message> */}
                            <Form.Message
                                match='typeMismatch'
                                className='text-sm text-white opacity-80'
                            >
                                {form.error}
                            </Form.Message>
                        </div>
                    ))}
            </Form.Field>
            <div className='flex flex-row w-full gap-2 mt-4'>
                <button
                    className='inline-flex items-center justify-center w-1/2 px-3 py-2 font-mono text-base font-medium text-white transition-all duration-300 bg-gray-800 border border-gray-600 rounded-lg shadow-sm leading-1 focus:outline-none hover:border-gray-300'
                    onClick={() => setStep(0)}
                    type='button'
                >
                    Back
                </button>
                <button
                    className='inline-flex items-center justify-center w-1/2 px-3 py-2 font-mono text-base font-medium text-white transition-all duration-300 bg-gray-800 border border-gray-600 rounded-lg shadow-sm leading-1 focus:outline-none hover:border-gray-300'
                    onClick={() => setStep(2)}
                    type='button'
                >
                    Next
                </button>
            </div>
        </Form.Root>
    );
};

export default FormDemo;
