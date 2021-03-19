#  [PORT SCANNER](https://vinitshahdeo.github.io/PortScanner/)

## 💻 Introduction

Build in **Software-Defined Networking** (SDN) technology which is used for efficient and real-time defense against cyber attacks, 
 Port Scanner is an application intended to test a server or host for open ports. 

This application can be utilized by managers to check security approaches of their systems and by assailants to recognize arrange administrations running on a host and adventure vulnerabilities.

It ought to be noticed that port scanning can be viewed as, or interpreted as, a wrongdoing. One ought to never execute a port scanner against any site or IP address without unequivocal, composed, authorization from the proprietor of the server or PC that you are focusing on. Port scanning resembles to going into somebody's home and looking at all of their entryways and windows. There is extremely just motivation behind why anybody would do this, and it is to survey protections and vulnerabilities. In this way, on the off chance that you have no rhyme or reason to test these things, it tends to be expected you are a criminal.

## ✨Tech Stack Required

The Tech Stacks required to build this Port Scanner are:

1. Python programming language to write the scanning code for open ports .

2. `express.js` which is a server side scripting language and creates and starts servers to build the server

## 📌 Working

 #### To check for the open ports, Using `scanner.py` the Port Scanner attempts to connect to various ports and if it is able to connect that means the port is open.
  

   ![](https://github.com/SSHREYA71/PortScanner/blob/feature/documentation/assets/scanner.py%20screen.png)
   
   
1. First the server code is executed where the `index.js` starts ten servers.`index.js` is coded in `express.js` which imports `randNum.js` to generate random number and open ports at those `localhost`. 


   ![](https://raw.githubusercontent.com/SSHREYA71/PortScanner/feature/documentation/assets/index.js.png)


   ![](https://raw.githubusercontent.com/SSHREYA71/PortScanner/feature/documentation/assets/randomnm.js.png)
   
    It also imports `config.json` which stores values of low and high i.e. values within whose range the ports will open. In this code, it is set from 1 (inclusive) to 80      (exclusive). The code generates 10 random numbers from 1 to 8888 i.e low to high and starts servers at those ports. 
   

2. Then the `scanner.py` code imports and uses several python libraries like socket, subprocess and sys. 


   ![](https://raw.githubusercontent.com/SSHREYA71/PortScanner/feature/documentation/assets/scanner.py.png)
   

The `scanner.py` searches for all the open ports on remote server using sockets and prints the ports which are open i.e. where the server had started by `index.js`


  #### To scan all the IP addresses and print the addresses which are live, We use `ipscanner.py`.
  

1. To run IP Scanner open terminal and type `python src/ipscanner.py`and enter any IP address XXX.XXX.XXX.YYY in the space provided.


    ![](https://github.com/SSHREYA71/PortScanner/blob/feature/documentation/assets/ipscanner.png)
    
 
2. And all the addresses in the range XXX.XXX.XXX.0 to XXX.XXX.XXX.255   which are live will be printed.


    ![](https://github.com/SSHREYA71/PortScanner/blob/feature/documentation/assets/ipscanned.png)
   

  #### To run the scanner in a virtual enviornment we use `mainScanner`. 
  
  
1. To run the portscanner in a virtual enviornment firstly we need to install `flask` using the `pip install flask` command after this we also need to install the virtual enviorment using `pip install virtualenv` and then activate the enviornment. Then in the termianal we run the `python src/mainScanner` command.


   ![](https://github.com/SSHREYA71/PortScanner/blob/feature/documentation/assets/mainScanner.png)
   

2. After this we need to click on the url provided and this redirects us to the virtual environment of PortScanner.


   ![](https://github.com/SSHREYA71/PortScanner/blob/feature/documentation/assets/virtual%20screen.png)
   
  

## 🔗 Links


1.  [Click here](https://youtu.be/6v8yi4mLhlM) to **view the demo** | A YouTube Video by [Ishika](https://github.com/ishika1727). :raised_hands:


2.  [Click here](./Documentation.docx) to download the report.
