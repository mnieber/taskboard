import { computed } from 'mobx';
import { output } from 'skandha';
import {
  ProjectRequestByIdT,
  ProjectRequestT,
} from 'src/projectRequests/types';
import { listToItemById } from 'src/utils/ids';

export class Outputs {
  @output projectRequestsDisplay: Array<ProjectRequestT> = [];

  @computed get projectRequestById(): ProjectRequestByIdT {
    return listToItemById(this.projectRequestsDisplay);
  }
}
