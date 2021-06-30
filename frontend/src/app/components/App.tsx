import React from 'react';
import { UrlRouter } from 'src/app/components/UrlRouter';
import './App.scss';

export function App() {
  return (
    <div className="App w-screen">
      <header className="App__Header">
        <UrlRouter />
      </header>
    </div>
  );
}
