from Tkinter import *
import os

# Client app for the #cs Domination game
# Author: Rob J
# Created: 12/04/2013
# For the record, I've never done graphical Python before so this will probably
# not be efficient, although I will try to improve as the app develops.
# This app will use TKinter to create an event-driven REST interface to the counterpart
# server. Developed using Python 2.7.3

class Main:
#---------SHOW-CONNECT-DIALOG-----
	def showConnectDialog(self):
		dialog = Frame(self.tlTop)
		dialog.pack()
		
		#Instruction label
		lblInstruction = Label(dialog, text="Enter a hostname or IP address to connect to")
		lblInstruction.pack(side=TOP)
		
		#Hostname/IP box
		entAddress = Entry(dialog)
		entAddress.pack(side=BOTTOM)
		
		#Connect button
		btnConnect = Button(dialog, text="Connect", command=self.connect)
		btnConnect.pack(side=BOTTOM)
		
		#Cancel button
		btnCancel = Button(dialog, text="Cancel", command=dialog.quit)
		btnCancel.pack(side=BOTTOM)
#-------CONNECT------------------
	def connect(self):
		return ""
#-------INIT------------------
	def __init__(self, master):
	
		self.frame = Toplevel(master)
		
		self.frame = Frame(self.tlTop)
		self.frame.pack()
		
		#Version - increment as necessary
		self.version = 0.01
		
		#Host to connect to
		self.host = ''

		#Connect button
		self.btnConnect = Button(self.frame, text="Connect...", command=self.showConnectDialog)
		self.btnConnect.pack(side=BOTTOM)	
		
		#Quit button
		self.btnQuit = Button(self.frame, text="Quit", command=self.frame.quit)
		self.btnQuit.pack(side=BOTTOM)
		
		#Title label
		self.lblTitle = Label(self.frame, text=("PyRisk %s" % self.version))
		self.lblTitle.pack(side=TOP)
		
		#Game map image
		piMap = PhotoImage(file=(os.path.dirname(os.path.realpath(__file__)) + "/map.png"))

		#Game board label
		self.lblMap = Label(self.frame, image=piMap)
		self.lblMap.pack(side=TOP)

#----------RUN---------
root = Tk()
main_app = Main(root)
root.mainloop()
	
