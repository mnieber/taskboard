import { values } from 'lodash/fp';
import { reaction } from 'mobx';
import { observer } from 'mobx-react-lite';
import * as React from 'react';
import { CtrProvider } from 'react-default-props-context';
import { useStore } from 'src/app/components';
import { TasksState } from 'src/tasks/TasksState';

type PropsT = React.PropsWithChildren<{}>;

export const TasksStateProvider: React.FC<PropsT> = observer(
  (props: PropsT) => {
    const { tasksStore } = useStore();

    const createState = () => {
      return new TasksState({
        tasksStore,
      });
    };

    const updateState = (state: TasksState) => {
      reaction(
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
