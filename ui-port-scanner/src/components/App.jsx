import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Note from "./Note";
import notes from "../notes"
import results from "../results"
import Card from "react-bootstrap/Card"
import Port from "./Search-port"
import Result from "./Search-results"

function App() {
  return (
    <div>
      <Header />
      <h2 style={{textAlign: "center"}}> 
        Fetch Timer 
        00:00
      </h2>
      <Card.Body>
      <h3>Search Port</h3>
      <hr></hr>
      <Port />
      </Card.Body>
      <Card>
      <h3>Results</h3>
      <hr></hr>
      <h4>Last 10 scans</h4>
      <br></br>
        {  
          notes.map(noteItem => {
            return (
              <Note
                key={noteItem.key}
                host_scanned={noteItem.host_scanned}
                low_range={noteItem.low_range}
                high_range={noteItem.high_range}
              />
            );
          })
        }
        </Card>
        <Card>
        <h3>Search Results</h3>
        <hr></hr>
        {  
          results.map(resultsItem => {
            return (
              <Result
                key={resultsItem.key}
                host_scanned={resultsItem.host_scanned}
                low_range={resultsItem.low_range}
                high_range={resultsItem.high_range}
              />
            );
          })
        };
        </Card>
      <Footer />
    </div>
  );
}

export default App;
