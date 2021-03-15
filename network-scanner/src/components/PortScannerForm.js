import React, {Component} from 'react';
import { Button, Form, FormGroup, Label, Input, Col, FormFeedback  } from "reactstrap";

class PortScannerForm extends Component{
    constructor(){
        super();
        this.state = {
            host: '',
            lowerRange: '',
            higherRange: '',
            errors: false,
            touched: {
                host: false,
                lowerRange: false,
                higherRange: false
            }
        }
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleBlur = this.handleBlur.bind(this);
    }

    handleBlur(event){
        const field = event.target.name;
        this.setState((state, props)=>({
            touched: { ...state.touched, [field]: true }
        }));
    }

    validate({host, lowerRange, higherRange}) {
        const errors = {
            host: '',
            lowerRange: '',
            higherRange: ''
        };

        const reg = /^\d+$/;

        if (this.state.touched.host && host.length < 3){
            errors.host = 'Invalid hostname';
        }
        else
        {
            errors.host = '';
        }
        
        if (this.state.touched.lowerRange && !reg.test(lowerRange)){
            errors.lowerRange = 'Lower port range must contain only numbers';
        }
        else
        {
            errors.lowerRange = '';
        } 

        if (this.state.touched.higherRange && !reg.test(higherRange)){
            errors.higherRange = 'Higher port range muse contain only numbers';
        }
        else
        {
            errors.higherRange = '';
        } 

        if (this.state.touched.lowerRange && this.state.touched.higherRange && parseInt(lowerRange) > parseInt(higherRange)){
            errors.lowerRange = 'Lower port range must be less than Higher port range';
        }

        return errors;
    }


    handleChange(event){
        const value = event.target.value;
        const name = event.target.name;
        this.setState({
            [name]: value
        });
    }

    handleSubmit(event){
        const errors = this.validate(this.state);
        if(errors.host !== '' || errors.lowerRange !== '' || errors.higherRange !== '')
            return

        console.log("Host: " + this.state.host);
        console.log("Lower Range: " + this.state.lowerRange);
        console.log("Higher Range: " + this.state.higherRange);
        event.preventDefault();
    }

    render(){
        const errors = this.validate(this.state);
        
        return(
            <div className="row row-content">
                <div className="col-12"><h3>Search Port</h3></div>
                <hr/>
                <div className="col-12">
                    <Form onSubmit={this.handleSubmit}>
                        <FormGroup row>
                            <Col sm={12}>
                                <Label htmlFor="host">Enter website you want to search open ports for</Label>
                            </Col>
                            <Col sm={12}>
                                <Input type="text"  
                                        id="host"
                                        name="host"
                                        placeholder="https://www.facebook.com"
                                        value={this.state.host}
                                        valid={errors.host === ''}
                                        invalid={errors.host !== ''}
                                        onBlur={this.handleBlur}
                                        onChange={this.handleChange}
                                        required/>
                                <FormFeedback>{errors.host}</FormFeedback>
                            </Col>        
                        </FormGroup>
                        <FormGroup row>
                            <Col sm={12}>
                                <Label htmlFor="lowerRange" sm={6}>Enter lower range (inclusive)</Label>
                                <Label htmlFor="higherRange" sm={6}>Enter higher range (inclusive)</Label>
                            </Col>
                            <Col sm={{size: 6}}>
                                <Input  type="number" 
                                        id="lowerRange"
                                        name="lowerRange"
                                        min="1"
                                        max="65535"
                                        placeholder="1"
                                        valid={errors.lowerRange === ''}
                                        invalid={errors.lowerRange !== ''}
                                        value={this.state.lowerRange}
                                        onBlur={this.handleBlur}
                                        onChange={this.handleChange}
                                        required/>
                                <FormFeedback>{errors.lowerRange}</FormFeedback>
                            </Col>
                            <Col sm={{size: 6}}>
                                <Input  type="number" 
                                        id="higherRange"
                                        name="higherRange"
                                        placeholder="8888"
                                        min="1"
                                        max="65535"
                                        value={this.state.higherRange}
                                        valid={errors.higherRange === ''}
                                        invalid={errors.higherRange !== ''}
                                        onBlur={this.handleBlur}
                                        onChange={this.handleChange}
                                        required/>
                                <FormFeedback>{errors.higherRange}</FormFeedback>
                            </Col>
                        </FormGroup>
                        <div className="text-center">
                            <Button outline type="submit" 
                                    style={{
                                        backgroundColor: '#80cbc4', 
                                        color: '#ffffff'
                                    }}>
                                    <strong>SCAN</strong>
                            </Button>
                        </div>
                    </Form>
                </div>
            </div>
        );
    }
}

export default PortScannerForm;