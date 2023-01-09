import React, { useState } from "react";
import SearchBar from "./components/SearchBar";
import Navigation from "./components/Navbar";
import SearchButton from "./components/SearchButton";
import ExpertTile from "./components/ExpertTile";


function App() {

  return (
      <React.StrictMode>
        <div>
            <header>
                <Navigation />
            </header>
            <div >
                <SearchBar   />
                <SearchButton   />
            </div>
            <div>
                <ExpertTile />
            </div>

        </div>
      </React.StrictMode>
  );
}

export default App;
