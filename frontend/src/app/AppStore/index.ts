import { makeObservable, observable } from 'mobx';
import { Api } from 'src/api/Api';
import { storeConnectsToApi } from 'src/app/AppStore/policies';
import { ProjectRequestsStore } from 'src/projectRequests/ProjectRequestsStore';
import { TasksStore } from 'src/tasks/TasksStore';

export class AppStore {
  @observable tasksStore: TasksStore;
  @observable projectRequestsStore: ProjectRequestsStore;
  @observable api: Api = new Api();

  constructor() {
    makeObservable(this);

    this.tasksStore = new TasksStore();
    this.projectRequestsStore = new ProjectRequestsStore();

    this.applyPolicies();
  }

  applyPolicies() {
    storeConnectsToApi(this.tasksStore, this.api);
    storeConnectsToApi(this.projectRequestsStore, this.api);
  }
}
