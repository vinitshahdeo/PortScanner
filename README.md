# Port Scanner
## A basic Port Scanner using Python with an Express Server to test!

With this port scanner, I just attempt to connect<sup>This is a form of "reconnaissance" for hackers and penetration testers</sup> at various ports, and do nothing else. If I'm able to connect to open ports, then I know at least the port is open.

## How to run?

- **Open terminal and type `npm start`**: This will start multiple servers within the given range.

- **Open another terminal and type `python scanner.py`**: Enter `localhost` or `127.0.0.1`. It will scan all the ports and print the open ports.


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

- [Express](https://expressjs.com/) -  Node.js web framework used for creating server. Check `server/index.js`
- [Socket](https://docs.python.org/3/library/socket.html) -  Low-level networking interface. Check `scanner.py`



<p align="center"><sup>This repository is intended for individuals to test their own equipment for weak
 security, and the author(<b>@vinitshahdeo</b>) will take no responsibility if it is put to any other use.</sup></p>
