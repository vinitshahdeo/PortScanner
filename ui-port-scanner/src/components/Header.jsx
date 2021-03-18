import React from "react";

function Header() {
  var styles = {
    margin: '20px',
    width: '250px',
    height: '250px',
    //backgroundColor: blue,
    display: 'inline-block',
  };
  var bgColors = { "Default": "#81b71a",
                    "Blue": "#00B1E1",
                    "Cyan": "#37BC9B",
                    "Green": "#8CC152",
                    "Red": "#E9573F",
                    "Yellow": "#F6BB42",
  };
  return (
    <header style={{backgroundColor: bgColors.Green}}>
      <h1 style={{display: "inine"}}>Port Scanner</h1>
      <h2 style={{ display: "inline", padding:30}}> Scan Port </h2>
      <h2 style={{display: "inline", padding:30}}> About </h2>
      <h2 style={{ display: "inline", padding:30}}> Contact </h2>
    </header>
  );
}

export default Header;
