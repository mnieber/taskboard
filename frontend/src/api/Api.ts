import { normalize, schema } from 'normalizr';
import { ApiBase } from 'src/api/ApiBase';
import { ObjT } from 'src/utils/types';

const projectRequest = new schema.Entity('projectRequest');

const projectRequestList = new schema.Array(projectRequest);

export class Api extends ApiBase {
  getProjectRequests() {
    return this._doQuery(
      'getProjectRequests',
      `query getProjectRequests {
        projectRequests {
          id
          name
        }
      }`,
      {},
      (response: ObjT) =>
        normalize(response.projectRequests, projectRequestList).entities,
      (error: ObjT) => error.response.errors[0].message
    );
  }
}
