import React from 'react';
import { AppStore } from 'src/app/AppStore';

const appStore = new AppStore();

export const StoreContext = React.createContext<AppStore>(appStore);

export const StoreProvider: React.FC = ({ children }) => {
  return (
    <StoreContext.Provider value={appStore}>{children}</StoreContext.Provider>
  );
};
