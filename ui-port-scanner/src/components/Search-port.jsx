import React from "react";
import ReactDOM from "react-dom";

function Port(props) {
  return (
    <div>
        <form>
        <label for="fname">Enter Website you want to search open ports for</label>
        <br></br>
        <input type="text" id="fname" />
        <br></br>
        <label for="lname">Enter low range(inclusive)</label>
        <br></br><input type="text" id="lname"/>
        <br></br>
        <label for="hname">Enter higher range(exclusive)</label>
        <br></br><input type="text" id="hname"/>
        <br></br>
        <input variant="info" type="submit" value="SCAN" className="btn-info"/>
        </form>
    </div>
  );
}

export default Port;
