#first i loaded the required package for making a gui
import tkinter as tk
import tkinter.font as tkfont
from tkinter import *
from tkinter.ttk import *


#we start by creating our GUI app. We initialize tkinter by creating a root widget, which is a frame/window 
# Creating a window
Groot = tk.Tk()


# For changing the title of the title bar 
Groot.title("Text Encryptor-Decryptor")


#We can set the dimensions of our window: so user can change it
Groot.resizable(width=FALSE, height=FALSE)

#add a canvas to our window. Canvas is a rectangular area where we can place our text and widgets
# Creating a canvas 
canvas = tk.Canvas(Groot,height = 500, width=400, bg="MediumPurple1")
# Attaching the canvas
canvas.pack()

# Set the family,size and style of the font
bold_font = tkfont.Font(family="Arial",size=12,weight="bold")

#lets add a text in our canvas. We create a label which basically allows us to display text and images
# Creating a label with a text and attaching it to the root
label1 = tk.Label(Groot,text= "Enter the Text",width=20,bg="MediumPurple1")
# adding the font features to the label
label1.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200,100,window=label1)

#We will create a text bar where the user can enter the text. We use the Entry widget to enter and display single line of text.
# Text Area 
user_text = tk.Entry(Groot)
canvas.create_window(200,150,window=user_text)

#We create another text label which tells the user to “choose an operation” from the given options.
# Creating a label with a text and attaching it to the root
label2=tk.Label(Groot,text="Choose an Operation",width=25,bg="MediumPurple1")
# adding the font features to the label
label2.config(font=bold_font)
# placing the label in the canvas
canvas.create_window(200,200,window=label2)

#variables which we can use to manipulate the values of Tkinter widget. The connection works both ways: if the variable changes for any reason, the widget it’s connected to will be updated to reflect the new value.
# Tkinter Variable 
v = tk.IntVar()

#We now define a function “choice”, which will get the value of the radio button selected by the user and will perform either encryption or decryption based on the option selected by the user.
# Defined a function choice
def choice():
  # Retrieve the value of the radio button
    x = v.get()
  # Performs Encryption if the value is 1 else performs Decryption.
    if(x==1):
        encryption()
    elif(x==2):
        decryption()

        # Defined a function Encryption
def encryption():
  # Get the user entered text to get function and store it in a variable plain_text
    plain_text = user_text.get()
  # To store the result   
    cipher_text = ""
  # Number of shift to be performed. For Caesar Cipher it's 3
    key = 3
  # traversing the text
    for i in range(len(plain_text)):
        letter = plain_text[i]
  # UpperCase Condition
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
  # LowerCase Condition
            cipher_text+=chr((ord(letter)+key-97)%26+97)
  # Creating a label with a text and attaching it to the root       
    label3 =tk.Label(Groot,text=cipher_text,width=30, height=8,bg="light yellow")
  # adding the font features to the label
    label3.config(font=bold_font)
  # placing the label in the canvas
    canvas.create_window(200,350,window=label3)
    # Defined a function Decryption
def decryption():
  # Get the user entered text to get function and store it in a varaible cipher_text
    cipher_text = user_text.get()
  # To store the result
    plain_text = ""
  # Number of shifts to be performed. For Caesar Cipher it's 3.
    key = 3
  # Traversing the text
    for i in range(len(cipher_text)):
        letter = cipher_text[i]
  # Uppercase condition
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
  # Lowercase condition
            plain_text+=chr((ord(letter)-key-97)%26+97) 
  # Creating a label with a text and attaching it to the root
    label4 =tk.Label(Groot,text=plain_text,width=30, height=8,bg="light yellow")
  # Adding the font features to the label
    label4.config(font=bold_font)
  # Placing the label in the canvas
    canvas.create_window(200,350,window=label4)

    #Now, we create the radio buttons
label5=tk.Radiobutton(Groot, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
label5.config(font=bold_font)
canvas.create_window(100,250,window=label5)

# Radio Button for Decryption
label6=tk.Radiobutton(Groot, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
label6.config(font=bold_font)
canvas.create_window(300,250,window=label6)

Groot.mainloop()
