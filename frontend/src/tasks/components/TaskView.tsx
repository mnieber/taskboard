import { observer } from 'mobx-react-lite';
import { FC, useDefaultProps } from 'react-default-props-context';
import { TaskT } from 'src/tasks/types';
import { getResourceView } from 'src/utils/components';

type PropsT = {};

type DefaultPropsT = {
  task: TaskT;
  taskResUrl: string;
};

export const TaskView: FC<PropsT, DefaultPropsT> = observer((p: PropsT) => {
  const props = useDefaultProps<PropsT, DefaultPropsT>(p);

  const resourceView = getResourceView({ resUrl: props.taskResUrl });
  if (resourceView) return resourceView;

  return (
    <div className="TaskView flex flex-col w-full">
      To do: show task with name {props.task.name}
    </div>
  );
});
