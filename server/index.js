/**
 * 
 * @description Creates multiple Express servers
 * @author Vinit Shahdeo <vinitshahdeo@gmail.com>
 */

var express = require('express');
var config = require('../config.json');
var randNumGenerator = require('./utils/randomNum');

let countOfPorts = config.count, // total number of ports to open
    low = config.range.low, // lower range of port (inclusive)
    high = config.range.high; // higher range of port (exclusive)

// generating the ports
let ports = new Set(); // using set because ports can't be duplicate

while(ports.size != countOfPorts) { // adding the required number of ports
    ports.add(randNumGenerator(low, high));
}

console.log(`Starting server at ${countOfPorts} different ports....\n`);

let portsArray = [...ports];

for (let index = 0; index < portsArray.length; index++) {
    
    express().listen(portsArray[index], () => {
        console.log('--Server started at port '+portsArray[index]);
        if(index==portsArray.length-1)
        {
            console.log("\n\nStop these servers only after doing port analysis !!!\n\n")
        }
    })
}