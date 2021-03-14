import React, {Component} from 'react';


class PortScannerForm extends Component{
    constructor(){
        super();
        this.state = {
            host: '',
            lowerRange: '',
            higherRange: ''
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event){
        const value = event.target.value;
        const name = event.target.name;
        this.setState({
            [name]: value
        });
    }

    handleSubmit(event){
        console.log(JSON.stringify(this.state));
        event.preventDefault();
    }

    render(){
        return(
            <div>
                <form onSubmit={this.handleSubmit}>
                    <input type="text" 
                            id="host"
                            name="host"
                            placeholder="https://www.facebook.com"
                            value={this.state.host}
                            onChange={this.handleChange}/>
                    <input type="number" 
                            id="lowerRange"
                            name="lowerRange"
                            placeholder="1"
                            value={this.state.lowerRange}
                            onChange={this.handleChange}/>
                    <input type="number" 
                            id="higherRange"
                            name="higherRange"
                            placeholder="8888"
                            value={this.state.higherRange}
                            onChange={this.handleChange}/>
                    <button type="submit">SCAN</button>
                </form>
            </div>
        );
    }
}

export default PortScannerForm;