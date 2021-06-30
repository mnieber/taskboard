import { makeObservable, observable } from 'mobx';
import { Api } from 'src/api/Api';
import { storeConnectsToApi } from 'src/app/AppStore/policies';
import { TasksStore } from 'src/tasks/TasksStore';

export class AppStore {
  @observable tasksStore: TasksStore;
  @observable api: Api = new Api();

  constructor() {
    makeObservable(this);

    this.tasksStore = new TasksStore();

    this.applyPolicies();
  }

  applyPolicies() {
    storeConnectsToApi(this.tasksStore, this.api);
  }
}
