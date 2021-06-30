import React from 'react';
import { useStore } from 'src/app/components';
import { EffectWithoutArgs } from 'src/utils/components';

type PropsT = {};

export const LoadTasksEffect: React.FC<PropsT> = (p: PropsT) => {
  const { api } = useStore();
  return (
    <EffectWithoutArgs
      f={() => {
        api.getTasks();
      }}
    />
  );
};
