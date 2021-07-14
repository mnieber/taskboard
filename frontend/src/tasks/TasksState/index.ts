import {
  addCleanUpFunctionToCtr,
  cleanUpCtr,
} from 'react-default-props-context';
import * as Skandha from 'skandha';
import { ClassMemberT as CMT, facet, getm } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { Inputs } from 'src/tasks/TasksState/facets/Inputs';
import { Outputs } from 'src/tasks/TasksState/facets/Outputs';
import { TasksStore } from 'src/tasks/TasksStore';

type PropsT = {
  tasksStore: TasksStore;
};

export class TasksState {
  @facet inputs = new Inputs();
  @facet outputs = new Outputs();
  tasks = {};

  _setTasksCallbacks(props: PropsT) {}

  _applyTasksPolicies(props: PropsT) {
    const Inputs_items = [Inputs, 'tasks', this] as CMT;
    const Outputs_display = [Outputs, 'tasksDisplay', this] as CMT;

    const policies = [
      Skandha.mapDataToFacet(Outputs_display, getm(Inputs_items)),
    ];

    Skandha.installPolicies(policies, this.tasks);
  }

  destroy() {
    cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    registerCtr({
      ctr: this,
      childCtrs: [
        {
          ctr: this.tasks,
          details: { name: 'Tasks' },
          initCtr: () => {
            this._setTasksCallbacks(props);
            this._applyTasksPolicies(props);
            addCleanUpFunctionToCtr(this, () => cleanUpCtr(this.tasks));
          },
        },
      ],
    });
  }
}
