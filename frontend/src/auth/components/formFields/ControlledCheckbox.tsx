import React from 'react';
import {
  createFormFieldProps,
  useFormStateContext,
} from 'react-form-state-context';
import { useFormFieldContext } from 'src/forms/components/FormFieldContext';

type PropsT = {};

export const ControlledCheckbox = (props: PropsT) => {
  const formState = useFormStateContext();
  const fieldContext = useFormFieldContext();

  return (
    <input
      className="text-primary"
      {...createFormFieldProps({
        formState,
        fieldName: fieldContext.fieldName,
        fieldType: 'checkbox',
      })}
    />
  );
};
