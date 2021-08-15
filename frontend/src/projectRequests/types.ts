export type ProjectRequestT = {
  changemakerName: string;
  dateOfBirth: date;
  description: string;
  email: string;
  id: string;
  location: string;
  projectName: string;
};

export type ProjectRequestByIdT = { [id: string]: ProjectRequestT };
