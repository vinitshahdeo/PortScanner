# Port Scanner 
## A basic [Port Scanner](https://vinitshahdeo.github.io/PortScanner/) using Python with an [Express](https://expressjs.com/) Server to test!

[![GitHub license](https://img.shields.io/github/license/vinitshahdeo/PortScanner?logo=github)](https://github.com/vinitshahdeo/PortScanner/blob/master/LICENSE) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/vinitshahdeo/PortScanner?logo=github)](https://github.com/vinitshahdeo/PortScanner/) [![GitHub last commit](https://img.shields.io/github/last-commit/vinitshahdeo/PortScanner?logo=git&logoColor=white)](https://github.com/vinitshahdeo/PortScanner/commits/master)

With this port scanner, I just attempt to connect<sup>This is a form of "reconnaissance" for hackers and penetration testers</sup> at various ports, and do nothing else. If I'm able to connect to open ports, then I know at least the port is open.

## Pre-requisites

[![node-current](https://img.shields.io/node/v/express?logo=node.js)](https://nodejs.org/)

- **Python** `>= v2.7.0`
    - Install Python from [here](https://www.python.org/).

- **Node.js** `>= v0.10.0`
    - Install Node.js from [here](https://nodejs.org/).

## How to run?

- **Open terminal** and **type `npm install`**: This will install the dependencies ([Express](https://expressjs.com)).

- In the same terminal and **type `npm start`**: This will start multiple servers within the given range.

- **Open another terminal** and **type `python scanner.py`**: Enter `localhost` or `127.0.0.1`. It will scan all the ports and print the open ports.


> Note: You can enter remote host if you want to scan the ports for any remote host. Check the [DISCLAIMER.md](./DISCLAIMER.md) before doing this.

## Configuration

The servers are opened at multiple ports, you can change the low range and high range for the ports to be listened by the Express server.

```js
{
    "range": {
        "low": "1",
        "high": "8888"
    },
    "count": "10"
}
```

- `low`: _lowest port number (**inclusive**)_
- `high`: _highest port number (**exclusive**)_
- `count`: _total number of ports_

## Useful resources: 

- [Express](https://expressjs.com/): Node.js web framework used for creating server. Check `server/index.js`
- [Socket](https://docs.python.org/3/library/socket.html):  Low-level networking interface. Check `scanner.py`

## Author

|                                                                                         <a href="https://fayz.in/stories/s/1522/0/?ckt_id=ZGL1ZGVk&title=story_of_vinit_shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/vinit-shahdeo.jpg" width="150px " height="150px" /></a>                                                                                         |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                        **[Vinit Shahdeo](https://fayz.in/stories/s/1522/0/?ckt_id=ZGL1ZGVk&title=story_of_vinit_shahdeo)**                                                                                                                                        |
| <a href="https://twitter.com/Vinit_Shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/twitter.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/vinit.shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/vinitshahdeo/"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/linkedin.png" width="32px" height="32px"></a> |

## TL;DR

Check out [this](https://gist.github.com/vinitshahdeo/92bf103f74a98cc55a447aa522bcdea9) gist if you're only looking for a **Python** script for **scanning ports**.

----
```javascript

if (_.isAwesome(thisRepo)) {
  thisRepo.star(); // thanks in advance :p
}

```
----

[![GitHub followers](https://img.shields.io/github/followers/vinitshahdeo.svg?label=Follow%20@vinitshahdeo&style=social)](https://github.com/vinitshahdeo/)  [![Twitter Follow](https://img.shields.io/twitter/follow/Vinit_Shahdeo?style=social)](https://twitter.com/Vinit_Shahdeo)

<sup>This repository is intended for individuals to test their own equipment for weak
 security, and the author(**@vinitshahdeo**) will take no responsibility if it is put to any other use. Check [DISCLAIMER.md](./DISCLAIMER.md)</sup>
 
[![Made with Python](https://forthebadge.com/images/badges/made-with-python.svg)](https://github.com/vinitshahdeo/PortScanner/) [![Built with love](https://forthebadge.com/images/badges/built-with-love.svg)](https://github.com/vinitshahdeo/)
 
