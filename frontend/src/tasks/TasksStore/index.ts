import { action, makeObservable, observable } from 'mobx';
import { rsMap } from 'src/api/ResourceStateMap';
import { TaskByIdT } from 'src/tasks/types';
import { isUpdatedRS, RST } from 'src/utils/RST';

export const resourceUrls = {
  tasks: `TasksStore/tasks`,
};

export class TasksStore {
  @observable taskById: TaskByIdT = {};

  constructor() {
    makeObservable(this);
  }

  @action onLoadData(event: any, state: RST, queryName: string) {
    if (queryName === 'getTasks') {
      if (isUpdatedRS(state)) {
        this.taskById = event.payload.tasks;
      }
      rsMap.registerState(state, [resourceUrls.tasks]);
    }
  }
}
