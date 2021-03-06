#! python3

import tkinter as tk
from time import sleep
from fibonaccimod import *

class App(object):
	def __init__(self, master, **kwargs):
		self.master = master
		self.setFrames()
		self.setTitle()
		self.setInputs()
		self.setResults()

		self.currentLoop = False

	def setFrames(self):
		self.titleFrame = tk.Frame(self.master)
		self.titleFrame.grid(row=0,column=0)

		self.inputFrame = tk.Frame(self.master)
		self.inputFrame.grid(row=1,column=0)

		self.resultFrame = tk.Frame(self.master)
		self.resultFrame.grid(row=2,column=0)

		self.ratioFrame = tk.Frame(self.master)
		self.ratioFrame.grid(row=3,column=0)

	def setTitle(self):
		self.title = tk.Label(self.titleFrame,text="Golden Ratio",font=("Verdana",18),height=3)
		self.title.grid(row=0,column=0)

	def setInputs(self):
		self.startlabel = tk.Label(self.inputFrame,text="First Term",anchor="center")
		self.startlabel.grid(row=0,column=0)
		self.startInput = tk.Entry(self.inputFrame,borderwidth=5,width=20)
		self.startInput.grid(row=1,column=0)

		self.secondlabel = tk.Label(self.inputFrame,text="Second Term", anchor="center")
		self.secondlabel.grid(row=0,column=1)
		self.secondInput = tk.Entry(self.inputFrame,borderwidth=5,width=20)
		self.secondInput.grid(row=1,column=1)

		self.lengthLabel = tk.Label(self.inputFrame, text="Length",anchor="center")
		self.lengthLabel.grid(row=0,column=2)
		self.sLength = tk.Entry(self.inputFrame,borderwidth=5,width=20)
		self.sLength.grid(row=1,column=2)

		
		self.submit = tk.Button(self.inputFrame,borderwidth=3,text="SUBMIT", command = self.calculate, anchor="center")
		self.submit.grid(row=1,column=3)

	def setResults(self):

		self.ratioLabel = tk.Label(self.ratioFrame, text="Ratio: ", relief="flat",height=2,font=("sans-serif",15,"bold"))
		self.ratioLabel.grid(row=0,column=0)
		self.ratio  = tk.Label(self.ratioFrame,text="0",relief="flat",anchor="center",height=2,font=("sans-serif",15))
		self.ratio.grid(row=0,column=2)

		self.stats = tk.Text(self.resultFrame, relief="flat",borderwidth=0, state="disabled",width=55,wrap="word",bg="#d6d6c2")
		result_scroll = tk.Scrollbar(self.resultFrame)
		result_scroll.config(command=self.stats.yview)
		self.stats.config(yscrollcommand=result_scroll.set)
		self.stats.grid(row=1,column=0)
		result_scroll.grid(row=1,column=1,sticky="NS")

	def calculate(self):
		if self.startInput.get() and self.secondInput.get() and self.sLength.get():
			start = int(self.startInput.get())
			second = int(self.secondInput.get())
			length = int(self.sLength.get())
			sequence = generate_sequence(start, second, length)
			sequence = [str(i) for i in sequence]
			ratio = generate_golden_ratio(start,second,length)
			self.ratio.config(text=str(ratio))
			self.stats.config(state="normal")
			self.stats.delete('1.0',"end-1c")
			self.stats.insert('1.0',", ".join(sequence))
			self.stats.tag_add("a","1.0","end-1c")
			self.stats.tag_config("a",font=("Courier",20))
			self.stats.config(state="disabled")
		else:
			return

			




root = tk.Tk()
root.wm_title("Golden Ratio Generator")
app = App(root)
root.mainloop()