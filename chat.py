from tkinter import * 
import customtkinter
import openai
import os
import pickle
import ctypes
​
# Initiate App
root = customtkinter.CTk()
root.title("Project BootCon Bot")
root.geometry('800x800')
​
​
# Set Color Scheme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")
​
# Automatic HighDPI Scaling for Windows
try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except AttributeError:
    pass
​
​
# Submit To OpenAi
def speak():
	if chat_entry.get():
		# Define the file name
		filename = "api_key"
			
		try:
			if os.path.isfile(filename):
				# Open the file
				input_file = open(filename, 'rb')
​
				# Load data from file into defined variable
				misc = pickle.load(input_file)
​
				# Query ChatGPT
				# Define the API key
				openai.api_key = misc
​
				# Create an instance
				openai.Model.list()
​
				# Define the query / response
				response = openai.Completion.create(
					model="text-davinci-003",
					prompt=chat_entry.get(),
					temperature=0,
					max_tokens=4000,
					top_p=1.0,
					frequency_penalty=0.0,
					presence_penalty=0.0
					)
​
				my_text.insert(END, (response["choices"][0]["text"]).strip())
				my_text.insert(END, "\n\n")
​
			else:
				# Create the file
				input_file = open(filename, 'wb')
				# Close the file
				input_file.close()
				# Error message - you need an api key
				my_text.insert(END, "\n\nYou need an API key to talk with this AI bot. \n\nFind it at openai, https://beta.openai.com/account/api-keys")
​
​
		except Exception as e:
			my_text.insert(END, f"\n\nThe MATE Pipeline Medics have failed you, There was an error\n\n{e}")
				
	else:
		my_text.insert(END, "\n\nHey not all of us can be as intelligent as The MATE Pipeline Medics, you forgot to type something!")
​
# Clear Screen
def clear():
	# Clear the primary text box
	my_text.delete(1.0, END)
	# Clear the primary chat entry
	chat_entry.delete(0, END)
​
# API
def key():
	# Resize App
	root.geometry('600x750')
	# Reshow API Frame
	api_frame.pack(pady=30)
​
​
	# Define the file name
	filename = "api_key"
​
​
	try:
		if os.path.isfile(filename):
			# Open the file
			input_file = open(filename, 'rb')
​
			# Load data from file into defined variable
			misc = pickle.load(input_file)
​
			# Output misc to the entry box
			api_entry.insert(END, misc)
		else:
			# Create the file
			input_file = open(filename, 'wb')
		 	# Close the file
			input_file.close()
​
	except Exception as e:
		my_text.insert(END, f"\n\nThe MATE Pipeline Medics have failed you, There was an error\n\n{e}")
​
​
# Save API Key
def save_key():
	#Define file name
	filename = "api_key"
	
	try:
		# Open File
		output_file = open(filename, 'wb')
​
		#Add data to file
		pickle.dump(api_entry.get(), output_file)
​
		# Delete Entry Box
		api_entry.delete(0, END)
​
		#Hide API Frame
		api_frame.pack_forget()
		#Resize API App
		root.geometry('600x600')
	
	except Exception as e:
		my_text.insert(END, f"\n\nThe MATE Pipeline Medics have failed you, There was an error\n\n{e}")
​
# Create Text Frame
text_frame = customtkinter.CTkFrame(root)
text_frame.pack(pady=20)
​
# Add Text Widget To Get ChatGPT Responses
my_text = Text(text_frame,
	font=100,
	bg="#343638",
	width=75,
	bd=1,
	fg="#d6d6d6",
	relief="flat",
	wrap=WORD,
	selectbackground="#1f538d")
my_text.grid(row=0, column=0)
​
# Create Scrollbar for text widget
text_scroll = customtkinter.CTkScrollbar(text_frame,
	command=my_text.yview)
text_scroll.grid(row=0, column=1, sticky="ns")
​
# Add Scrollbar to the textbox
my_text.configure(yscrollcommand=text_scroll.set) 
​
# Entry Widget to enter text into ChatGPT
chat_entry = customtkinter.CTkEntry(root,
	placeholder_text="Type something to Project BootCon Bot, it knows everything...",
	width=535,
	height=50,
	border_width=1)
chat_entry.pack(pady=10)
​
# Create Button Frame
button_frame =customtkinter.CTkFrame(root, fg_color="#242424")
button_frame.pack(pady=10)
​
# Create Submit Button
submit_button = customtkinter.CTkButton(button_frame,
	text="Speak to Project BootCon Bot",
	command=speak)
submit_button.grid(row=0, column=0, padx=25)
​
# Create Clear Button
clear_button = customtkinter.CTkButton(button_frame,
		text="Clear Response",
	command=clear)
clear_button.grid(row=0, column=1, padx=35)
​
# Create API Button
api_button = customtkinter.CTkButton(button_frame,
	text="Update API Key",
	command=key)
api_button.grid(row=0, column=2, padx=25)
​
# Add API Key Frame
api_frame = customtkinter.CTkFrame(root, border_width=1)
api_frame.pack(pady=30)
​
# Add API Entry Widget
api_entry = customtkinter.CTkEntry(api_frame,
	placeholder_text="Enter API Key",
	width=350, height=50, border_width=1)	
api_entry.grid(row=0, column=0, padx=20, pady=20)
​
# Add API Button
api_save_button = customtkinter.CTkButton(api_frame,
	text="Save Key",
	command=save_key)
api_save_button.grid(row=0, column=1, padx=10)
​
​
​
​
​
root.mainloop()
