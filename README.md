# Port Scanner 
## A basic [Port Scanner](https://vinitshahdeo.github.io/PortScanner/) :mag_right: using Python with an [Express](https://expressjs.com/) Server to test!

[![GitHub license](https://img.shields.io/github/license/vinitshahdeo/PortScanner?logo=github)](https://github.com/vinitshahdeo/PortScanner/blob/master/LICENSE) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/vinitshahdeo/PortScanner?logo=github)](https://github.com/vinitshahdeo/PortScanner/) [![GitHub last commit](https://img.shields.io/github/last-commit/vinitshahdeo/PortScanner?logo=git&logoColor=white)](https://github.com/vinitshahdeo/PortScanner/commits/master)

> ### **Note: Please follow [this link](https://github.com/vinitshahdeo/PortScanner/discussions/117) if you're a [GSSoC](https://gssoc.girlscript.tech/) participant.** Keep watching this repo, we'll be opening more `beginner-friendly` [issues](https://github.com/vinitshahdeo/PortScanner/issues).


With this port scanner, I just attempt to connect<sup>This is a form of "reconnaissance" for hackers and penetration testers</sup> at various ports, and do nothing else. If I'm able to connect to open ports, then I know at least the port is open.

## Pre-requisites :rotating_light:

[![node-current](https://img.shields.io/node/v/express?logo=node.js)](https://nodejs.org/) [![GitHub top language](https://img.shields.io/github/languages/top/vinitshahdeo/PortScanner?logo=python&logoColor=white)](https://www.python.org/)

- **Python** `>= v2.7.0`
    - Install Python from [here](https://www.python.org/).

- **Node.js** `>= v0.10.0`
    - Install Node.js from [here](https://nodejs.org/).
    
- **Pip** `>= v9.0.1`
    - Install pip from [here](https://pip.pypa.io/en/stable/installing/).

## How to run? :rocket:

### To run Port Scanner: (Via Terminal)

- **Open terminal** and **type `npm install`**: This will install the dependencies ([Express](https://expressjs.com)).

- In the same terminal and **type `npm start`**: This will start multiple servers within the given range.

- **Open another terminal** and **type `python src/scanner.py`**: Enter `localhost` or `127.0.0.1`. It will scan all the ports and print the open ports.

> Note: You can enter remote host if you want to scan the ports for any remote host. Check the [DISCLAIMER.md](./DISCLAIMER.md) before doing this.

### To run Port Scanner: (Via UI)

#### Install [flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)

> *Make sure you have `Python27\Scripts` path added to your system's environment variables.*

**1**. In PowerShell,

```ps 
pip install flask
```

#### Install virtual environment 

> *This step is required only if you are using Python2.7, skip this step when running Python3.X.*

**2**. For Python 2, (via pip)

   In PowerShell,

```ps
pip install virtualenv
virtualenv --help
```

> *Kindly [check this](https://virtualenv.pypa.io/en/latest/installation.html) if pip installation fails.*

#### Create virtual environment

**3**. Create a `venv` folder inside `src`,

```ps
python -m virtualenv venv
\Python27\Scripts\virtualenv.exe venv
```

#### Activate the virtual environment

**4**. Activate `venv`,

```ps
venv\Scripts\activate
```

**5**. Run `mainScanner.py`,

```ps
pip install flask
python src/mainScanner.py
```
**6**. Go to the port url returned by your terminal.

### To run IP Scanner:

- **Open terminal** and **type `python src/ipscanner.py`**: Enter any IP address `XXX.XXX.XXX.YYY`. It will scan all the addresses in the range `XXX.XXX.XXX.0` to `XXX.XXX.XXX.255` and print the addresses which are live.

## Configuration :gear:

The servers are opened at multiple ports, you can change the low range and high range for the ports to be listened by the Express server.

```js
{
    "range": {
        "low": "1",
        "high": "8888"
    },
    "ipRange": {
        "low": "0",
        "high": "255"
    },
    "count": "10",
    "thread": { 
        "count": 8
    }
}
```

- `range.low`: _lowest port number (**inclusive**)_
- `range.high`: _highest port number (**exclusive**)_
- `ipRange.low`: _lowest IP address range (**inclusive**)_
- `ipRange.high`: _highest IP address range (**inclusive**)_
- `count`: _total number of ports_
- `thread.count`: _total number of concurrent threads_

## Contributing :handshake:

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat&logo=git&logoColor=white)](https://github.com/vinitshahdeo/PortScanner/pulls) [![CodeFactor](https://www.codefactor.io/repository/github/vinitshahdeo/portscanner/badge)](https://www.codefactor.io/repository/github/vinitshahdeo/portscanner) [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/vinitshahdeo/PortScanner)

> Please read our [Code of Conduct](CODE_OF_CONDUCT.md).

**We're accepting PRs for our open and unassigned [issues](https://github.com/vinitshahdeo/PortScanner/issues)**. Please check [CONTRIBUTING.md](CONTRIBUTING.md). We'd love your contributions! **Kindly follow the steps below to get started:** 

**1.** Fork [this](https://github.com/vinitshahdeo/PortScanner) repository.

**2.** Clone the forked repository.

```bash
git clone https://github.com/<your-github-username>/PortScanner
```

**3.** Navigate to the project directory.

```bash
cd PortScanner
```

**4.** Create a new branch.

```bash
git checkout -b <your_branch_name>
```

**5.** Make changes in source code.

**6.** Stage your changes and commit

```bash
git add .

git commit -m "<your_commit_message>"
```

**7.** Push your local commits to the remote repo.

```bash
git push -u origin <your_branch_name>
```

**8.** Create a [PR](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request) to `develop` !

**9.** **Congratulations!** :tada: Sit and relax, you've made your contribution to [Port Scanner](https://vinitshahdeo.github.io/PortScanner/) project. :v: :heart:

## Branching :construction:

- `master` branch is maintained and tested regulary for **Python 2**.

- Please checkout `feature/python3.8` if you're using **[Python 3](https://www.python.org/download/releases/3.0/)**.

```sh
git checkout feature/python3.8
```

## Need for Multithreading :white_check_mark:

>The ability of a process to execute multiple threads parallelly is called multithreading. Ideally, multithreading can significantly improve the performance of any program.

Imagine scanning substantial number of ports(`range.high` = 8888) consecutively. The process would require quite a long time. 

This calls for the need of concurrency in different parts of this range(1-8888). That is, running different parts(1-1111, 1112-2222, 2223-3333...) of the same process at the same time. This would reduce the time required for completion by significant amount. The reduction in time can be related to the number of concurrent ranges(threads) being scanned simultaneously. Checkout the `Performance Analysis` for a follow up.

## Performance using threads :dart:

- `src/single/scanner.py`: Scanner without thread
- `src/scanner.py`: Scanner with multi threads

|Range(low-high)|`src/single/scanner.py` (in milliseconds)    |`src/scanner.py` (in milliseconds)   |
|---------------|----------------------------------|----------------------------------------|
|1-80           |143243                            |30862                                   |

> `CONST_NUM_THREADS` : 8

### Performance on the basis of number of threads :chart_with_downwards_trend:

Range of ports: `1-80`

|Number of threads|Execution time (in milliseconds)   | Compared Performances|
|-----------------|-----------------------------------|----------------------|
|2                |71627                              |50 % faster           |
|4                |40808                              |71.51 % faster        |
|8                |37003                              |74.17 % faster        |
|16               |36870                              |74.26 % faster        |
|32               |32674                              |77.19 % faster        |

#### Performance Analysis 

![Performance Analysis](./assets/Graph.png)

## Blog


[![Medium Story](https://img.shields.io/static/v1.svg?label=check&message=story%20on%20medium&color=success&logo=medium&style=for-the-badge&logoColor=white&colorA=grey)](https://medium.com/@kashish_121/go-green-featuring-github-f8750fbf0729)

- Check out [Kashish](https://github.com/kashish121)'s story on Medium - [GO-GREEN featuring GITHUB](https://medium.com/@kashish_121/go-green-featuring-github-f8750fbf0729)! 
She has shared her experience working on [this](https://vinitshahdeo.github.io/PortScanner/) project - **How it marks the commencement of her perennial journey to open source?**

- Check out [Ishika](https://github.com/ishika1727)'s story on Medium: [**`git push`**: You just need a little PUSH](https://medium.com/@ishikadubey2000/look-mom-im-on-github-521bb6c1f51d)!
She has shared her experience in working on [this](https://vinitshahdeo.github.io/PortScanner/) project and making her identity in the open-source world.

## Open Source Programs

<a href="https://www.leapcode.io/"><img src="./assets/leapcode.png" width="40%" height="10%"/></a>

We're now a part of **[Leapcode](https://www.leapcode.io/)**. It helps you contribute to open-source projects right from your first PR to working on major projects. It's still under construction and hopeful to have their platform up pretty soon. [Click here](https://www.leapcode.io/) to get an early access.


## Useful resources :books:

- [Express](https://expressjs.com/): Node.js web framework used for creating server. Check `server/index.js`
- [Socket](https://docs.python.org/3/library/socket.html):  Low-level networking interface in Python. Check `src/scanner.py`
- [Threading](https://docs.python.org/3/library/threading.html): Thread-based parallelism in python. Check `src/scanner_thread.py`
- [Flask](https://flask.palletsprojects.com/en/1.1.x/quickstart/): A micro web framework written in Python. Check `src/mainScanner.py`

## [Contributors](https://github.com/vinitshahdeo/PortScanner/graphs/contributors) :trophy:

[![GitHub issues](https://img.shields.io/github/issues/vinitshahdeo/PortScanner?logo=github)](https://github.com/vinitshahdeo/PortScanner/issues) [![GitHub pull requests](https://img.shields.io/github/issues-pr/vinitshahdeo/PortScanner?color=olive&logo=github)](https://github.com/vinitshahdeo/PortScanner/pulls)


|      Name :medal_military:    |     Social Media :wave:    | GitHub :octocat: |
|:-------------:|:-------------------|------------------|
| Vinit Shahdeo | :bird: [Twitter](https://twitter.com/Vinit_Shahdeo) <br>:mortar_board: [LinkedIn](https://www.linkedin.com/in/vinitshahdeo/) | [@vinitshahdeo](https://github.com/vinitshahdeo/)  |
| Kashish       | :bird: [Twitter](https://twitter.com/Kashish_121) <br>:mortar_board: [LinkedIn](https://www.linkedin.com/in/kashish121/) | [@Kashish121](https://github.com/Kashish121/)      |
| Ishika Dubey  | :bird: [Twitter](https://twitter.com/ishika1727) <br>:mortar_board: [LinkedIn](https://www.linkedin.com/in/ishika1727/) | [@ishika1727](https://github.com/ishika1727/)      |

> **See the contribution graph [here](https://github.com/vinitshahdeo/PortScanner/graphs/contributors).**

[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/0)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/1)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/2)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/3)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/4)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/5)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/6)](https://github.com/vinitshahdeo/PortScanner/)[![](https://sourcerer.io/fame/vinitshahdeo/vinitshahdeo/PortScanner/images/7)](https://github.com/vinitshahdeo/PortScanner/)

## Admin

|                                                                                         <a href="https://www.eatmy.news/2020/06/code-like-you-eat-i-mean-code-daily-as.html"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/vinit-shahdeo.jpg" width="150px " height="150px" /></a>                                                                                         |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                                                                                                                                        **[Vinit Shahdeo](https://fayz.in/stories/s/1522/0/?ckt_id=ZGL1ZGVk&title=story_of_vinit_shahdeo)**                                                                                                                                        |
| <a href="https://twitter.com/Vinit_Shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/twitter.png" width="32px" height="32px"></a> <a href="https://www.facebook.com/vinit.shahdeo"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/facebook.png" width="32px" height="32px"></a> <a href="https://www.linkedin.com/in/vinitshahdeo/"><img src="https://raw.githubusercontent.com/vinitshahdeo/Water-Monitoring-System/master/assets/linkedin.png" width="32px" height="32px"></a> |


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fvinitshahdeo%2FPortScanner.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fvinitshahdeo%2FPortScanner?ref=badge_large)

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
 
