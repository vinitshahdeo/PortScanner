import React, {Component} from 'react';
import { Table  } from "reactstrap";
import { HISTORY } from "../shared/history";
import '../css/history.css';

class HistoryComponent extends Component{
    constructor(){
        super();
        this.state = {
            history: HISTORY
        }
    }

    render(){
        const history_data = this.state.history.map((object, index)=>{
            return <tr key={index}>
                        <td>{object["host-scanned"]}</td>
                        <td>{object["low-port"]}</td>
                        <td>{object["high-port"]}</td>
                    </tr>;
        });
        return(
            <div className="row row-content" id="history-component">
                <div className="col-12"><h3>History</h3></div>
                <hr/>
                <div className="col-12"><h4>Last 10 Scans</h4></div>
                <div className="col-12 mt-3">
                    <Table borderless>
                        <thead>
                            <tr>
                                <th>Host Scanned</th>
                                <th>Low</th>
                                <th>High</th>
                            </tr>
                        </thead>
                        <tbody>
                            {history_data}
                        </tbody>
                    </Table>
                </div>
            </div>
        );
    }
}

export default HistoryComponent;