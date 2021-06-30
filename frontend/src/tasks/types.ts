export type TaskT = {
  id: string;
  name: string;
};

export type TaskByIdT = { [id: string]: TaskT };
