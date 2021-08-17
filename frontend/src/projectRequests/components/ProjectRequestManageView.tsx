import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { FC, useDefaultProps } from 'react-default-props-context';
import {
  ApproveProjectRequestFormView,
  ProjectRequestView,
  RejectProjectRequestFormView,
} from 'src/projectRequests/components';
import './ProjectRequestManageView.scss';

type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

type DefaultPropsT = {};

export const ProjectRequestManageView: FC<PropsT, DefaultPropsT> = observer(
  (p: PropsT) => {
    const props = useDefaultProps<PropsT, DefaultPropsT>(p);
    return (
      <div
        className={classnames(
          'ProjectRequestManageView',
          'flex flex-col',
          props.className
        )}
      >
        <div className="ProjectRequestManageView__topPanel">
          <ProjectRequestView />
        </div>
        <div className="ProjectRequestManageView__bottomPanel">
          <RejectProjectRequestFormView />
          <ApproveProjectRequestFormView />
        </div>
      </div>
    );
  }
);
