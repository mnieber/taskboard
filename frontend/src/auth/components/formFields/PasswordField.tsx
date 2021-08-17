import React from 'react';
import {
  createFormFieldProps,
  useFormStateContext,
} from 'react-form-state-context';
import { useFormFieldContext } from 'src/forms/components/FormFieldContext';

type PropsT = { placeholder: string };

export const PasswordField = (props: PropsT) => {
  const formState = useFormStateContext();
  const fieldContext = useFormFieldContext();

  return (
    <input
      placeholder={props.placeholder}
      type="password"
      {...createFormFieldProps({
        formState,
        fieldName: fieldContext.fieldName,
        fieldType: 'password',
      })}
    />
  );
};
