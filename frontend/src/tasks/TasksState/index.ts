import { makeObservable } from 'mobx';
import { cleanUpCtr } from 'react-default-props-context';
import {
  ClassMemberT as CMT,
  facet,
  getm,
  installPolicies,
  mapDataToFacet,
  registerFacets,
} from 'skandha';
import { makeCtrObservable } from 'skandha-mobx';
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

    const policies = [mapDataToFacet(Outputs_display, getm(Inputs_items))];

    installPolicies(policies, this.tasks);
  }

  destroy() {
    cleanUpCtr(this.tasks);
  }

  constructor(props: PropsT) {
    registerFacets(this, {});
    makeObservable(this);

    registerFacets(this.tasks, { name: 'Tasks' });
    this._setTasksCallbacks(props);
    this._applyTasksPolicies(props);
    makeCtrObservable(this.tasks);
  }
}
