import { observer } from 'mobx-react-lite';
import React from 'react';
import {
  FormStateProvider,
  HandleSubmitArgsT,
  HandleValidateArgsT,
} from 'react-form-state-context';
import { useStore } from 'src/app/components';
import { Field } from 'src/forms/components/Field';
import { GlobalError } from 'src/forms/components/GlobalError';
import { SaveButton } from 'src/forms/components/SaveButton';
import { TextField } from 'src/forms/components/TextField';
import './RejectProjectRequestFormView.scss';

type PropsT = {};

export const RejectProjectRequestFormView: React.FC<PropsT> = observer(() => {
  const { projectRequestsStore } = useStore();

  const initialValues = {
    projectRequestId: null,
    sendEmail: null,
    emailTo: null,
    emailBody: null,
  };
  const initialErrors = {};
  const handleValidate = ({ values, setError }: HandleValidateArgsT) => {};
  const handleSubmit = ({ values }: HandleSubmitArgsT) => {
    projectRequestsStore.saveRejectProjectRequestForm(values);
  };

  const formDiv = (
    <div className="RejectProjectRequestFormView flex flex-col w-full">
      <FormStateProvider
        initialValues={initialValues}
        initialErrors={initialErrors}
        handleValidate={handleValidate}
        handleSubmit={handleSubmit}
      >
        <GlobalError />
        <Field fieldName="name" label="Name">
          <TextField />
        </Field>
        <SaveButton label="Save" disabled={false} />
      </FormStateProvider>
    </div>
  );

  return formDiv;
});
