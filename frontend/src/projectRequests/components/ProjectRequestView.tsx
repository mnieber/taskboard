import { observer } from 'mobx-react-lite';
import { FC, useDefaultProps } from 'react-default-props-context';
import { ProjectRequestT } from 'src/projectRequests/types';
import { getResourceView } from 'src/utils/components';

type PropsT = {};

type DefaultPropsT = {
  projectRequest: ProjectRequestT;
  projectRequestResUrl: string;
};

export const ProjectRequestView: FC<PropsT, DefaultPropsT> = observer(
  (p: PropsT) => {
    const props = useDefaultProps<PropsT, DefaultPropsT>(p);

    const resourceView = getResourceView({
      resUrl: props.projectRequestResUrl,
    });
    if (resourceView) return resourceView;

    return (
      <div className="ProjectRequestView flex flex-col w-full">
        To do: show projectRequest with id {props.projectRequest.id}
      </div>
    );
  }
);
