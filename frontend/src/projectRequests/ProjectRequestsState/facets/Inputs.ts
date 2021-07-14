import { input } from 'skandha';
import { ProjectRequestT } from 'src/projectRequests/types';

export class Inputs {
  @input projectRequests: Array<ProjectRequestT> = [];
}
