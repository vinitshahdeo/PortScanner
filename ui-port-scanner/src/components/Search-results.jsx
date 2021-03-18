import React from "react";

function Result(props) {
    var styles = {
        margin: '5px',
      };

  return (
    <div className="Card">
        <div style={styles}>Scanning remote host {props.host_scanned} Completed in {props.complete_time} between {props.low_range} to {props.high_range}</div>    
        <hr></hr>
    </div>
  );
}

export default Result;
