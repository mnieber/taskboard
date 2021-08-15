import { reaction } from 'mobx';
import { observer } from 'mobx-react-lite';
import { values } from 'ramda';
import * as React from 'react';
import { CtrProvider, FC, useDefaultProps } from 'react-default-props-context';
import { useStore } from 'src/app/components';
import { TasksState } from 'src/tasks/TasksState';
import { resUrls } from 'src/tasks/TasksStore';

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
      return reaction(
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
    };

    const getDefaultProps = (state: TasksState) => {
      return {
        tasksState: () => state,
        tasks: () => state.outputs.tasksDisplay,
        tasksResUrl: () => resUrls.taskById,
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
