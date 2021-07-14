import {
  addCleanUpFunctionToCtr,
  cleanUpCtr,
} from 'react-default-props-context';
import * as Skandha from 'skandha';
import { ClassMemberT as CMT, facet, getm } from 'skandha';
import { registerCtr } from 'skandha-mobx';
import { Inputs } from 'src/projectRequests/ProjectRequestsState/facets/Inputs';
import { Outputs } from 'src/projectRequests/ProjectRequestsState/facets/Outputs';
import { ProjectRequestsStore } from 'src/projectRequests/ProjectRequestsStore';

type PropsT = {
  projectRequestsStore: ProjectRequestsStore;
};

export class ProjectRequestsState {
  @facet inputs = new Inputs();
  @facet outputs = new Outputs();
  projectRequests = {};

  _setProjectRequestsCallbacks(props: PropsT) {}

  _applyProjectRequestsPolicies(props: PropsT) {
    const Inputs_items = [Inputs, 'projectRequests', this] as CMT;
    const Outputs_display = [Outputs, 'projectRequestsDisplay', this] as CMT;

    const policies = [
      Skandha.mapDataToFacet(Outputs_display, getm(Inputs_items)),
    ];

    Skandha.installPolicies(policies, this.projectRequests);
  }

  destroy() {
    cleanUpCtr(this);
  }

  constructor(props: PropsT) {
    registerCtr({
      ctr: this,
      childCtrs: [
        {
          ctr: this.projectRequests,
          details: { name: 'ProjectRequests' },
          initCtr: () => {
            this._setProjectRequestsCallbacks(props);
            this._applyProjectRequestsPolicies(props);
            addCleanUpFunctionToCtr(this, () =>
              cleanUpCtr(this.projectRequests)
            );
          },
        },
      ],
    });
  }
}
