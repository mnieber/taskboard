import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { ProjectRequestT } from 'src/projectRequests/types';
import './ProjectRequestListViewItem.scss';

export type PropsT = {
  projectRequest: ProjectRequestT;
  className?: any;
  onClick?: any;
};

export const ProjectRequestListViewItem: React.FC<PropsT> = observer(
  (props: PropsT) => {
    return (
      <div
        className={classnames(
          'ProjectRequestListViewItem flex flex-row flex-1 mb-2',
          props.className
        )}
        onClick={props.onClick}
      >
        {props.projectRequest.id}
      </div>
    );
  }
);
