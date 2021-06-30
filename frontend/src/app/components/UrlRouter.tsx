import { createBrowserHistory } from 'history';
import { observer } from 'mobx-react-lite';
import React from 'react';
import { Route, Router, Switch } from 'react-router-dom';
import { TaskListView, TaskView } from 'src/tasks/components';

type PropsT = {};

export const history = createBrowserHistory();

export const UrlRouter: React.FC<PropsT> = observer((props: PropsT) => {
  return (
    <Router history={history}>
      <Switch>
        <Route path="/tasks/">
          <TaskListView />
        </Route>
        <Route path="/task/">
          <TaskView />
        </Route>
      </Switch>
    </Router>
  );
});
