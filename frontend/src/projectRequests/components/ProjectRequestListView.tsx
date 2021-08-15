import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import { always, map, pipe } from 'ramda';
import { FC, useDefaultProps } from 'react-default-props-context';
import { useHistory } from 'react-router-dom';
import { ProjectRequestListViewItem } from 'src/projectRequests/components';
import { ProjectRequestT } from 'src/projectRequests/types';
import { getResourceView } from 'src/utils/components';
import './ProjectRequestListView.scss';

type PropsT = {
  className?: any;
};

type DefaultPropsT = {
  projectRequests: ProjectRequestT[];
  projectRequestsResUrl: string;
};

export const ProjectRequestListView: FC<PropsT, DefaultPropsT> = observer(
  (p: PropsT) => {
    const props = useDefaultProps<PropsT, DefaultPropsT>(p);
    const history = useHistory();

    const resourceView = getResourceView({
      resUrl: props.projectRequestsResUrl,
    });
    if (resourceView) return resourceView;

    const projectRequestDivs = pipe(
      always(props.projectRequests),
      map((x: ProjectRequestT) => (
        <ProjectRequestListViewItem
          key={x.id}
          projectRequest={x}
          onClick={() => history.push(`/projectRequests/${x.id}`)}
        />
      ))
    )();

    const noItems = <h2>There are no projectRequests</h2>;

    return (
      <div
        className={classnames(
          'ProjectRequestListView flex flex-col w-full',
          props.className
        )}
      >
        {projectRequestDivs.length && projectRequestDivs}
        {!projectRequestDivs.length && noItems}
      </div>
    );
  }
);
