import { reaction } from 'mobx';
import { observer } from 'mobx-react-lite';
import { values } from 'ramda';
import * as React from 'react';
import {
  addCleanUpFunctionToCtr,
  CtrProvider,
  FC,
  useDefaultProps,
} from 'react-default-props-context';
import { useStore } from 'src/app/components';
import { ProjectRequestsState } from 'src/projectRequests/ProjectRequestsState';

type PropsT = React.PropsWithChildren<{}>;

type DefaultPropsT = {};

export const ProjectRequestsStateProvider: FC<PropsT, DefaultPropsT> = observer(
  (p: PropsT) => {
    const props = useDefaultProps<PropsT, DefaultPropsT>(p);
    const { projectRequestsStore } = useStore();

    const createState = () => {
      return new ProjectRequestsState({
        projectRequestsStore,
      });
    };

    const updateState = (state: ProjectRequestsState) => {
      const cleanUpFunction = reaction(
        () => ({
          projectRequests: values(projectRequestsStore.projectRequestById),
        }),
        (inputs) => {
          state.inputs.projectRequests = inputs.projectRequests;
        },
        {
          fireImmediately: true,
        }
      );
      addCleanUpFunctionToCtr(state, cleanUpFunction);
    };

    const getDefaultProps = (state: ProjectRequestsState) => {
      return {
        projectRequestsState: () => state,
        projectRequests: () => state.outputs.projectRequestsDisplay,
      };
    };

    return (
      <CtrProvider
        createCtr={createState}
        updateCtr={updateState}
        destroyCtr={(state: ProjectRequestsState) => state.destroy()}
        getDefaultProps={getDefaultProps}
      >
        {props.children}
      </CtrProvider>
    );
  }
);
