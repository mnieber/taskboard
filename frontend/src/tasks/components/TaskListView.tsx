import classnames from 'classnames';
import { always, flow, map } from 'lodash/fp';
import { observer } from 'mobx-react-lite';
import { FC, useDefaultProps } from 'react-default-props-context';
import { TaskListViewItem } from 'src/tasks/components';
import { TaskT } from 'src/tasks/types';
import { getResourceView } from 'src/utils/components';
import './TaskListView.scss';

type PropsT = {
  className?: any;
};

type DefaultPropsT = {
  tasks: TaskT[];
  tasksResUrl: string;
};

export const TaskListView: FC<PropsT, DefaultPropsT> = observer((p: PropsT) => {
  const props = useDefaultProps<PropsT, DefaultPropsT>(p);

  const taskDivs = flow(
    always(props.tasks),
    map((x) => <TaskListViewItem key={x.id} task={x} />)
  )();

  const noItems = <h2>There are no tasks</h2>;

  const resourceView = getResourceView({ resourceUrl: props.tasksResUrl });
  if (resourceView) return resourceView;

  return (
    <div
      className={classnames(
        'TaskListView flex flex-col w-full',
        props.className
      )}
    >
      {taskDivs.length && taskDivs}
      {!taskDivs.length && noItems}
    </div>
  );
});
