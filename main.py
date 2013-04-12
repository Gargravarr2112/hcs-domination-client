from Tkinter import *
import os

class Main:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		
		self.version = 0.1
		
		self.button = Button(frame, text="Quit", command=frame.quit)
		self.button.pack(side=BOTTOM)
		
		self.title_label = Label(frame, text=("PyRisk %s" % self.version))
		self.title_label.pack(side=TOP)
		
		self.map_image = PhotoImage(file=(os.path.dirname(os.path.realpath(__file__)) + "/map.png"))
		self.map_label = Label(frame, image=self.map_image)
		self.map_label.pack(side=TOP)
	
root = Tk()
main_app = Main(root)
root.mainloop()
	
