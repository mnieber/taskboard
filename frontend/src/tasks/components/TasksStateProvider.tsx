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
import { TasksState } from 'src/tasks/TasksState';

type PropsT = React.PropsWithChildren<{}>;

type DefaultPropsT = {};

export const TasksStateProvider: FC<PropsT, DefaultPropsT> = observer(
  (p: PropsT) => {
    const props = useDefaultProps<PropsT, DefaultPropsT>(p);
    const { tasksStore } = useStore();

    const createState = () => {
      return new TasksState({
        tasksStore,
      });
    };

    const updateState = (state: TasksState) => {
      const cleanUpFunction = reaction(
        () => ({
          tasks: values(tasksStore.taskById),
        }),
        (inputs) => {
          state.inputs.tasks = inputs.tasks;
        },
        {
          fireImmediately: true,
        }
      );
      addCleanUpFunctionToCtr(state, cleanUpFunction);
    };

    const getDefaultProps = (state: TasksState) => {
      return {
        tasksState: () => state,
        tasks: () => state.outputs.tasksDisplay,
      };
    };

    return (
      <CtrProvider
        createCtr={createState}
        updateCtr={updateState}
        destroyCtr={(state: TasksState) => state.destroy()}
        getDefaultProps={getDefaultProps}
      >
        {props.children}
      </CtrProvider>
    );
  }
);
