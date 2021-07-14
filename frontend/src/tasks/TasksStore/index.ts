import { action, makeObservable, observable } from 'mobx';
import { values } from 'ramda';
import { rsMap } from 'src/api/ResourceStateMap';
import { TaskByIdT, TaskT } from 'src/tasks/types';
import { isUpdatedRS, RST } from 'src/utils/RST';

export const resUrls = {
  taskById: `TasksStore/taskById`,
};

export class TasksStore {
  @observable taskById: TaskByIdT = {};

  constructor() {
    makeObservable(this);
  }

  @action onLoadData(event: any, rs: RST, queryName: string) {
    if (queryName === 'getTasks') {
      if (isUpdatedRS(rs)) {
        this.addTasks(values(event.payload.data.tasks));
      }
      rsMap.registerRS(rs, [resUrls.taskById]);
    }
  }

  @action addTasks = (tasks: TaskT[]) => {
    forEach((task: TaskT) => {
      this.taskById[task.id] = task;
    }, tasks);
  };
}
