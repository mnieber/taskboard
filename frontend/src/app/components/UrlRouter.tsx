import { createBrowserHistory } from 'history';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { Route, Router, Switch } from 'react-router-dom';
import { LoadProjectRequestsEffect } from 'src/api/components';
import {
  ProjectRequestListView,
  ProjectRequestsStateProvider,
  ProjectRequestView,
  SelectProjectRequestEffect,
} from 'src/projectRequests/components';

type PropsT = {};

export const history = createBrowserHistory();

export const UrlRouter: React.FC<PropsT> = observer((props: PropsT) => {
  return (
    <Router history={history}>
      <Switch>
        <Route path="/projectRequests/">
          <ProjectRequestsStateProvider>
            <Route path="/projectRequests/list">
              <LoadProjectRequestsEffect />
              <ProjectRequestListView />
            </Route>
            <Route path="/projectRequests/:projectRequestId">
              <SelectProjectRequestEffect />
              <ProjectRequestView />
            </Route>
          </ProjectRequestsStateProvider>
        </Route>
      </Switch>
    </Router>
  );
});
