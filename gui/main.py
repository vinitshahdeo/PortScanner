from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import socket
import subprocess
import sys
from datetime import datetime
import json

from scanner_thread import split_processing

class MainWindow(QMainWindow):
    label = None
    scanInProgress = False

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Port Scanner")
        self.initUI()
        
    def initUI(self):
        font = QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        
        self.scanBtn = QPushButton("Scan", self)
        self.scanBtn.setGeometry(QRect(280, 180, 75, 23))
        self.scanBtn.clicked.connect(self.scanButtonClicked)

        self.hostTextField = QTextEdit(self)
        self.hostTextField.setGeometry(QRect(330, 41, 151, 31))

        self.hostLabel = QLabel("Host Address", self)
        self.hostLabel.setGeometry(QRect(180, 40, 121, 31))
        self.hostLabel.setFont(font)

        self.lowerRangeLabel = QLabel("Lower Range", self)
        self.lowerRangeLabel.setGeometry(QRect(70, 120, 121, 31))
        self.lowerRangeLabel.setFont(font)

        self.higherRangeLabel = QLabel("Higher Range", self)
        self.higherRangeLabel.setGeometry(QRect(340, 120, 121, 31))
        self.higherRangeLabel.setFont(font)

        self.portRangeLabel = QLabel("Port Range", self)
        self.portRangeLabel.setGeometry(QRect(50, 80, 121, 31))
        self.portRangeLabel.setFont(font)

        self.dividerLine = QFrame(self)
        self.dividerLine.setGeometry(QRect(175, 90, 391, 16))
        self.dividerLine.setFrameShape(QFrame.HLine)
        self.dividerLine.setFrameShadow(QFrame.Sunken)

        self.lowRangeSpinner = QSpinBox(self)
        self.lowRangeSpinner.setMaximum(65535)
        self.lowRangeSpinner.setGeometry(QRect(180, 120, 91, 31))

        self.highRangeSpinner = QSpinBox(self)
        self.highRangeSpinner.setMaximum(65535)
        self.highRangeSpinner.setGeometry(QRect(460, 120, 91, 31))

        self.createProgressBar()

        self.scanResultsLabel = QLabel("Scan Results",self)
        self.scanResultsLabel.setGeometry(QRect(270, 250, 121, 31))
        self.scanResultsLabel.setFont(font)

        self.resultTextField = QPlainTextEdit(self)
        self.resultTextField.setGeometry(QRect(35, 290, 570, 150))
        self.resultTextField.setReadOnly(True)

        self.statusBar().showMessage('Ready')
        self.statusBar().setStyleSheet("background-color : grey")

        self.createMenuBar()

        self.setFixedSize(640, 480)
        self.show()

    def createProgressBar(self):
        self.scanProgressBar = QProgressBar(self)
        self.scanProgressBar.setGeometry(QRect(130, 220, 401, 23))
        self.scanProgressBar.setHidden(False)
        self.scanProgressBar.setValue(0)
        #self.startThread()

    def startThread(self):
        self.threadClass = self.ThreadClass()
        self.threadClass.finished.connect(self.onScanCompleted)
        self.threadClass.start()
        self.scanProgressBar.setValue(0)
    
        lowRange = int(self.lowRangeSpinner.value())
        highRange = int(self.highRangeSpinner.value())

        hostAddress = str(self.hostTextField.toPlainText())
        self.threadClass.remoteServer = hostAddress

        self.threadClass.lowRange = lowRange
        self.threadClass.highRange = highRange

        self.threadClass.cng_val.connect(self.updateProgressBar)
        self.threadClass.log_message.connect(self.newLog)

    def newLog(self, log): 
        self.resultTextField.insertPlainText(log)

    def createMenuBar(self):
        exitAct = QAction(self.style().standardIcon(QStyle.SP_FileDialogBack), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        saveAct = QAction(self.style().standardIcon(QStyle.SP_DialogSaveButton), '&Save Config', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save Configuration')
        saveAct.triggered.connect(self.saveConfig)
        
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(saveAct)
        fileMenu.addAction(exitAct)

    def terminate_scan(self):
        if (self.scanInProgress):
            self.scanInProgress = False
            self.scanBtn.setText("Scan")
            self.threadClass.terminate()
            self.statusBar().showMessage("Ready")

    def start_scan(self):
        self.scanInProgress = True
        self.startThread()
        self.scanBtn.setText("Stop")
        self.statusBar().showMessage('Scan Started')

    def onScanCompleted(self):
        self.statusBar().showMessage('Scan Complete')
        self.scanBtn.setText("Scan")
        scanInProgress = False

    def scanButtonClicked(self, *args):
        if self.scanInProgress:
            self.terminate_scan()
        else:
            self.start_scan()

    def updateProgressBar(self, val):
        self.scanProgressBar.setValue(val)
        self.statusBar().showMessage('Scanning. Ports Scanned: '+str(self.threadClass.ports_scanned))
    
    def saveConfig(self, *args):
        #Need to save current configuration here
        print("Saved config.")

    class ThreadClass(QThread):
        cng_val = pyqtSignal(int)
        log_message = pyqtSignal(str)
        lowRange = 0
        highRange = 100
        totalports = highRange - lowRange
        remoteServer = None
        ports_scanned = 0
        threadCount = 8

        def scan(self, ports, range_low, range_high):
            if self.remoteServer is not None:
                remoteServerIP  = socket.gethostbyname(self.remoteServer)
            else:
                print("Remote Server not defined.")
                self.log_message.emit("Remote Server not defined."+"\n")
                return
            try:
                for port in range(range_low, range_high):
                    print("Scanning port:", port)
                    self.log_message.emit("Scanning port:"+ str(port)+"\n")
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex((remoteServerIP, port))
                    if result == 0:
                        print ("Port {}: 	 Open".format(port))
                        self.log_message.emit("Port "+str(port) + ":    Open"+"\n")
                    sock.close()

                    self.ports_scanned += 1
                    progress = (self.ports_scanned * 100)/(self.highRange - self.lowRange)
                    self.cng_val.emit(int(progress))

            except KeyboardInterrupt:
                print ("You pressed Ctrl+C")
                self.log_message.emit("You pressed Ctrl+C"+"\n")
                return

            except socket.gaierror:
                print ('Hostname could not be resolved. Exiting')
                self.log_message.emit('Hostname could not be resolved. Exiting'+"\n")
                return
            except socket.error:
                print ("Couldn't connect to server")
                self.log_message.emit("Couldn't connect to server"+"\n")
                return 

        def run(self):
            if self.remoteServer is not None:
                try:
                    remoteServerIP  = socket.gethostbyname(self.remoteServer)
                except socket.gaierror:
                    print ('Hostname could not be resolved. Exiting')
                    self.log_message.emit('Hostname could not be resolved. Exiting'+"\n")
                    return
                except socket.error:
                    print ("Couldn't connect to server")
                    self.log_message.emit("Couldn't connect to server"+"\n")
                    return  

            else:
                print("Remote Server not defined.")
                self.log_message.emit("Remote Server not defined."+"\n")
                return

            print ("-" * 60)
            print ("Please wait, scanning remote host....", remoteServerIP)
            print ("-" * 60)

            self.log_message.emit("-"*60+"\n")
            self.log_message.emit("Please wait, scanning remote host.... "+str(remoteServerIP) + "\n")
            self.log_message.emit("-"*60+"\n")

            t1 = datetime.now()
            ports = list(range(self.lowRange, self.highRange))

            split_processing(ports, self.threadCount, self.scan, self.lowRange, self.highRange)
            # Checking the time again
            t2 = datetime.now()
            # Calculates the difference of time, to see how long it took to run the script
            total =  t2 - t1

            # Printing the information to screen
            print ('Scanning Completed in: ', total)
            self.log_message.emit('Scanning Completed in: '+ str(total)+"\n")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()