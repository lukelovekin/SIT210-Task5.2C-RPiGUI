from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT) 
GPIO.setup(38, GPIO.OUT) 
GPIO.setup(36, GPIO.OUT) 


class MyGUI(QMainWindow):
	def __init__(self):
		super(MyGUI, self).__init__()
		self.setGeometry(100, 100, 200, 200)
		self.setWindowTitle("Traffic Lights")
		self.initGUI()
		
	def initGUI(self):
		self.red = QtWidgets.QPushButton(self)
		self.red.setText("Red")
		self.red.move(50,50)
		self.red.clicked.connect(lambda: self.changeLight('red'))
	
		self.green = QtWidgets.QPushButton(self)
		self.green.setText("Green")
		self.green.move(50,90)
		self.green.clicked.connect(lambda: self.changeLight('green'))
		
		self.blue = QtWidgets.QPushButton(self)
		self.blue.setText("Blue")
		self.blue.move(50,130)
		self.blue.clicked.connect(lambda: self.changeLight("blue"))
		
	def lightsOut(self):
		GPIO.output(36, GPIO.LOW)
		GPIO.output(40, GPIO.LOW)
		GPIO.output(38, GPIO.LOW)

	def changeLight(self, color: str):
		self.lightsOut()
		print(color)
		if color == "red":
			GPIO.output(36, GPIO.HIGH)
		elif color == "green":
			GPIO.output(40, GPIO.HIGH)
		elif color == "blue":
			GPIO.output(38, GPIO.HIGH)
			
			
def window():
	app = QApplication(sys.argv)
	win = MyGUI()
	win.show()
	sys.exit(app.exec_())
	
	
window()