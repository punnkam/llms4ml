import React from "react";
import * as Form from "@radix-ui/react-form";

interface FormProps {
    title: string;
    formData: {
        label: string;
        description: string;
        error: string;
        value: string;
    }[];
    setFormData: any;
    setStep: any;
}

const FormDemo = ({ title, formData, setFormData, setStep }: FormProps) => (
    <Form.Root className='w-64'>
        <div className='z-10 w-full max-w-5xl items-center justify-center font-mono text-sm lg:flex mb-4'>
            <p className='flex w-full justify-center text-lg'>
                <code className='font-mono font-bold'>{title}</code>
            </p>
        </div>
        <Form.Field className='grid my-2' name='email'>
            {formData &&
                formData.map((form, index) => (
                    <div className='font-mono pb-2'>
                        <Form.Label className='text-sm font-medium text-white leading-9'>
                            {form.label}
                        </Form.Label>
                        <Form.Control asChild>
                            <input
                                className='text-sm outline-none focus:border-gray-50 hover:border-gray-500 transition-all duration-200 p-2 border-b border-gray-300 bg-gradient-to-b from-zinc-200 backdrop-blur-2xl dark:border-neutral-800 dark:bg-zinc-800/30 dark:from-inherit lg:static w-full lg:rounded-xl lg:border lg:bg-gray-200 py-3 px-4 lg:dark:bg-zinc-800/30 '
                                autoComplete='off'
                                type='text'
                                required
                                onChange={(e: any) =>
                                    setFormData({
                                        ...formData,
                                        [index]: {
                                            ...formData[index],
                                            value: e.target.value,
                                        },
                                    })
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
        <div className='w-full flex flex-row gap-2 mt-4'>
            <button
                className='w-1/2 inline-flex items-center justify-center rounded-lg py-2 px-3 text-base font-mono font-medium leading-1 bg-gray-800 text-white shadow-sm focus:outline-none transition-all duration-300 border border-gray-600 hover:border-gray-300'
                onClick={() => setStep(0)}
                type='button'
            >
                Back
            </button>
            <button
                className='w-1/2 inline-flex items-center justify-center rounded-lg py-2 px-3 text-base font-mono font-medium leading-1 bg-gray-800 text-white shadow-sm focus:outline-none transition-all duration-300 border border-gray-600 hover:border-gray-300'
                onClick={() => setStep(2)}
                type='button'
            >
                Next
            </button>
        </div>
    </Form.Root>
);

export default FormDemo;
