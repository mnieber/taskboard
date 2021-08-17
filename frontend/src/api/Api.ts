import { normalize, schema } from 'normalizr';
import { ApiBase } from 'src/api/ApiBase';
import { ObjT } from 'src/utils/types';

const projectRequest = new schema.Entity('projectRequests');

const projectRequestList = new schema.Array(projectRequest);

export class Api extends ApiBase {
  getProjectRequests() {
    return this._doQuery(
      'getProjectRequests',
      `query getProjectRequests {
        projectRequests {
          changemakerName,
          dateOfBirth,
          description,
          email,
          id,
          location,
          projectName,
        }
      }`,
      {},
      (response: ObjT) => {
        return normalize(response.projectRequests, projectRequestList).entities;
      },
      (error: ObjT) => {
        return error.response.errors[0].message;
      }
    );
  }

  postRejectProjectRequestForm(
    projectRequestId: string,
    sendEmail: boolean,
    emailTo: string,
    emailBody: string
  ) {
    return this._doQuery(
      'postRejectProjectRequestForm',
      `query postRejectProjectRequestForm(

      ) {
        postRejectProjectRequestForm(

        ) {
          success,
          errors {
            message
          }
        }
      }`,
      {},
      (response: ObjT) =>
        normalize(response.rejectProjectRequestForm, rejectProjectRequestForm)
          .entities,
      (error: ObjT) => error.response.errors[0].message
    );
  }

  postApproveProjectRequestForm(projectRequestId: string) {
    return this._doQuery(
      'postApproveProjectRequestForm',
      `query postApproveProjectRequestForm(

      ) {
        postApproveProjectRequestForm(

        ) {
          success,
          errors {
            message
          }
        }
      }`,
      {},
      (response: ObjT) =>
        normalize(response.approveProjectRequestForm, approveProjectRequestForm)
          .entities,
      (error: ObjT) => error.response.errors[0].message
    );
  }
}
