import { action, makeObservable, observable } from 'mobx';
import { forEach, values } from 'ramda';
import { rsMap } from 'src/api/ResourceStateMap';
import {
  ProjectRequestByIdT,
  ProjectRequestT,
} from 'src/projectRequests/types';
import { isUpdatedRS, RST } from 'src/utils/RST';

export const resUrls = {
  projectRequestById: `ProjectRequestsStore/projectRequestById`,
};

export class ProjectRequestsStore {
  @observable projectRequestById: ProjectRequestByIdT = {};

  resUrls = () => resUrls;

  constructor() {
    makeObservable(this);
  }

  @action onLoadData(event: any, rs: RST, queryName: string) {
    if (queryName === 'getProjectRequests') {
      if (isUpdatedRS(rs)) {
        this.addProjectRequests(values(event.payload.data.projectRequests));
      }
      rsMap.registerRS(rs, [resUrls.projectRequestById]);
    }
  }

  @action addProjectRequests = (projectRequests: ProjectRequestT[]) => {
    forEach((projectRequest: ProjectRequestT) => {
      this.projectRequestById[projectRequest.id] = projectRequest;
    }, projectRequests);
  };
}
