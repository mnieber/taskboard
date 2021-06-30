import { computed } from 'mobx';
import { output } from 'skandha';
import { TaskByIdT, TaskT } from 'src/tasks/types';
import { listToItemById } from 'src/utils/ids';

export class Outputs {
  @output tasksDisplay: Array<TaskT> = [];

  @computed get taskById(): TaskByIdT {
    return listToItemById(this.tasksDisplay);
  }
}
