import React from "react";

function Note(props) {
  const styles= {
      borderWidth: 5,
      paddingLeft:30
    };
  return (
    <div className="Card">  
      <table>
        <tr>
          <td style={styles}>{props.host_scanned}</td>
          <td style={styles}>{props.low_range}</td>
          <td style={styles}>{props.high_range}</td>    
        </tr>
      </table>
    </div>
  );
}

export default Note;
