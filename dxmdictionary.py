from tkinter import *
from PyDictionary import PyDictionary
import customtkinter

WIN = customtkinter.CTk()
WIN.title('DXM - DICTIONARY')
WIN.config(bg="#121212")
WIN.geometry("520x470")
WIN.resizable(False, False)

def lookup():

	my_text.delete(1.0, END)

	dictionary = PyDictionary()
	definition = dictionary.meaning(my_entry.get())

	for key,value in definition.items():

		my_text.insert(END, key + '\n\n')

		for values in value:
			my_text.insert(END, f'- {values}\n\n')

# APP DESIGN

spacer = Label(WIN)
spacer.config(bg="#121212")
spacer.pack()

my_labelframe = customtkinter.CTkFrame(WIN, corner_radius=10, width=650, height=50, fg_color="#212124")
my_labelframe.pack(pady=15)

my_entry = customtkinter.CTkEntry(my_labelframe, width=310, height=30, border_width=0, placeholder_text="Enter A Word", text_color="#c3c3c9", fg_color="#2d2d31")
my_entry.grid(row=0, column=0, padx=15, pady=10)

my_button = customtkinter.CTkButton(my_labelframe, text="LOOKUP", fg_color="#dc214c", hover_color="#e1365d", command=lookup, width=30, )
my_button.grid(row=0, column=1, padx=20)

text_frame = customtkinter.CTkFrame(WIN, corner_radius=10, fg_color="#212124")
text_frame.pack(pady=10)

my_text = Text(text_frame, height=20, width=60, wrap=WORD, bd=0, bg="#212124", fg="silver", highlightthickness=0)
my_text.pack(padx=15, pady=30)

WIN.mainloop()
