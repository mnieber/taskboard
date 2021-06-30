import { input } from 'skandha';
import { TaskT } from 'src/tasks/types';

export class Inputs {
  @input tasks: Array<TaskT> = [];
}
