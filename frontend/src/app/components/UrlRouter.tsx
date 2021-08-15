import { createBrowserHistory } from 'history';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { Route, Router, Switch } from 'react-router-dom';
import { LoadProjectRequestsEffect } from 'src/api/components';
import { AuthSwitch } from 'src/auth/components';
import {
  ProjectRequestListView,
  ProjectRequestManageView,
  ProjectRequestsStateProvider,
  SelectProjectRequestEffect,
} from 'src/projectRequests/components';

type PropsT = {};

export const history = createBrowserHistory();

export const UrlRouter: React.FC<PropsT> = observer((props: PropsT) => {
  return (
    <Router history={history}>
      <AuthSwitch />
      <Route path="/projectRequests/">
        <ProjectRequestsStateProvider>
          <Switch>
            <Route path="/projectRequests/list">
              <LoadProjectRequestsEffect />
              <ProjectRequestListView />
            </Route>
            <Route path="/projectRequests/:projectSlug">
              <SelectProjectRequestEffect />
              <ProjectRequestManageView />
            </Route>
          </Switch>
        </ProjectRequestsStateProvider>
      </Route>
    </Router>
  );
});
