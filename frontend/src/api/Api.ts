import { normalize, schema } from 'normalizr';
import { ApiBase } from 'src/api/ApiBase';
import { ObjT } from 'src/utils/types';

const task = new schema.Entity('task');
const taskList = new schema.Array(task);

export class Api extends ApiBase {
  getTasks() {
    return this._doQuery(
      'getTasks',
      `query getTasks {
        tasks {
          id
          name
        }
      }`,
      {},
      (response: ObjT) => normalize(response.tasks, taskList).entities,
      (error: ObjT) => error.response.errors[0].message
    );
  }
}
