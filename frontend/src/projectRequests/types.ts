export type ProjectRequestT = {
  id: string;
  name: string;
};

export type ProjectRequestByIdT = { [id: string]: ProjectRequestT };
