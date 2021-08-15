import classnames from 'classnames';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { FC, useDefaultProps } from 'react-default-props-context';
import './ProjectRequestManageViewBottomPanel.scss';

type PropsT = React.PropsWithChildren<{
  className?: any;
}>;

type DefaultPropsT = {};

export const ProjectRequestManageViewBottomPanel: FC<PropsT, DefaultPropsT> =
  observer((p: PropsT) => {
    const props = useDefaultProps<PropsT, DefaultPropsT>(p);
    return (
      <div
        className={classnames(
          'ProjectRequestManageViewBottomPanel',
          'flex flex-col',
          props.className
        )}
      >
        <RejectProjectRequestFormView />
        <ApproveProjectRequestFormView />
      </div>
    );
  });
