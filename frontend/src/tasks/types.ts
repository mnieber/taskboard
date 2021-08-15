export type TaskT = {
  assignedTo: string;
  id: string;
  state: string;
  title: string;
};

export type TaskByIdT = { [id: string]: TaskT };
