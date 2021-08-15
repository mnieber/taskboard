import { setCallbacks } from 'aspiration';
import {
  addCleanUpFunctionToCtr,
  cleanUpCtr,
} from 'react-default-props-context';
import * as Skandha from 'skandha';
import { ClassMemberT as CMT, facet, getm } from 'skandha';
import * as Facets from 'skandha-facets';
import { Highlight, HighlightCbs } from 'skandha-facets/Highlight';
import * as FacetPolicies from 'skandha-facets/policies';
import {
  handleSelectItem,
  Selection,
  SelectionCbs,
} from 'skandha-facets/Selection';
import { registerCtr } from 'skandha-mobx';
import { Inputs } from 'src/projectRequests/ProjectRequestsState/facets/Inputs';
import { Outputs } from 'src/projectRequests/ProjectRequestsState/facets/Outputs';
import { ProjectRequestsStore } from 'src/projectRequests/ProjectRequestsStore';
import { getIds } from 'src/utils/ids';

type PropsT = {
  projectRequestsStore: ProjectRequestsStore;
};

export class ProjectRequestsState {
  @facet inputs = new Inputs();
  @facet outputs = new Outputs();
  projectRequests = {
    selection: new Selection(),
    highlight: new Highlight(),
  };

  _setProjectRequestsCallbacks(props: PropsT) {
    const ctr = this.projectRequests;
    setCallbacks(ctr.selection, {
      selectItem: {
        selectItem(this: SelectionCbs['selectItem']) {
          handleSelectItem(ctr.selection, this.selectionParams);
          FacetPolicies.highlightFollowsSelection(
            ctr.selection,
            this.selectionParams
          );
        },
      },
    } as SelectionCbs);
    setCallbacks(ctr.highlight, {} as HighlightCbs);
  }

  _applyProjectRequestsPolicies(props: PropsT) {
    const Inputs_items = [Inputs, 'projectRequests', this] as CMT;
    const Outputs_display = [Outputs, 'projectRequestsDisplay', this] as CMT;
    const Outputs_itemById = [Outputs, 'projectRequestById', this] as CMT;

    const policies = [
      Skandha.mapDataToFacet(Outputs_display, getm(Inputs_items)),
      // selection
      Facets.selectionUsesSelectableIds(getm(Outputs_display), getIds),
      Facets.selectionUsesItemLookUpTable(getm(Outputs_itemById)),
      // highlight
      Facets.highlightUsesItemLookUpTable(getm(Outputs_itemById)),
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
