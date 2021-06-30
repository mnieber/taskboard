import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { TaskT } from 'src/tasks/types';
import './TaskListViewItem.scss';

export type PropsT = {
  task: TaskT;
  className?: any;
};

export const TaskListViewItem: React.FC<PropsT> = observer((props: PropsT) => {
  return (
    <div
      className={classnames(
        'TaskListViewItem flex flex-row flex-1 mb-2',
        props.className
      )}
    >
        {props.task.name}
    </div>
  );
});
