import tkinter

import random
import string
import function
from function import Functions
from tkinter import *

WIN_BGCOLOR = Functions.color_rgb(64,64,64)
WIDG_BGCOLOR = Functions.color_rgb(64,64,64)
WIDG_FGCOLOR = Functions.color_rgb(248,248,242)
HEADERLBL_FONT_STYLE = ('TimesNewRoman',14,'bold')
FONT_STYLE = ('TimesNewRoman',10,'bold')

# Logic
# alphabets_uppercase = string.ascii_uppercase
# alphabets_lowercase = string.ascii_lowercase

# numbers = string.digits
# all_characters.extend(list(numbers))
# punctuations = string.punctuation
# all_characters.extend(list(punctuations))


# all_characters = []

# all_characters.extend(list(alphabets_uppercase))
# all_characters.extend(list(alphabets_lowercase))


# random.shuffle(all_characters)

password_genrator = tkinter.Tk()
password_genrator.configure(bg = WIN_BGCOLOR)
password_genrator.title('Password Genrator')

strgeometry = Functions.Place_In_Centre(password_genrator,500,300)
password_genrator.geometry(strgeometry)






def GetValue():
    print(var)

label = tkinter.Label(
    master = password_genrator,
    bg = WIDG_BGCOLOR,
    fg = WIDG_FGCOLOR,
    font = HEADERLBL_FONT_STYLE,
    text = 'Password Genrator'
    )
label.pack(fill = X,pady = 10)



  
choice = IntVar()
R1 = Radiobutton(
    password_genrator,
    font = FONT_STYLE,
    background = WIDG_BGCOLOR,
    activebackground = WIDG_BGCOLOR,
    text="POOR",
    variable=choice,
    value=1 
    ).pack(anchor=CENTER)
R2 = Radiobutton(
    password_genrator,
    font = FONT_STYLE,
    background = WIDG_BGCOLOR,
    activebackground = WIDG_BGCOLOR,
    text="AVERAGE",
    variable=choice,
    value=2
   ).pack(anchor=CENTER)
R3 = Radiobutton(
    password_genrator,
    font = FONT_STYLE,
    background = WIDG_BGCOLOR,
    activebackground = WIDG_BGCOLOR,
    text="ADVANCED",
    variable=choice,
    value=3
   ).pack(anchor=CENTER)
 
val = IntVar()

def GenratePassword():
    global passoword_length
    selected_rdbutton = choice.get()
    passoword_length = val.get()
    global txt_password
   
   
    text_created = 1
    if selected_rdbutton == 1:
            alphabets_uppercase = string.ascii_uppercase
            alphabets_lowercase = string.ascii_lowercase
            all_characters = []
            all_characters.extend(list(alphabets_uppercase))
            all_characters.extend(list(alphabets_lowercase))
            random.shuffle(all_characters)
            
            
            Genrated_Password =  "".join(random.sample(all_characters, passoword_length))
            txt_Password.configure(text = Genrated_Password)
            txt_Password.update()
    elif selected_rdbutton == 2:
            alphabets_uppercase = string.ascii_uppercase
            alphabets_lowercase = string.ascii_lowercase
            numbers = string.digits
            all_characters = []
            all_characters.extend(list(alphabets_uppercase))
            all_characters.extend(list(alphabets_lowercase))
            all_characters.extend(list(numbers))
            random.shuffle(all_characters)
           
            Genrated_Password =  "".join(random.sample(all_characters, passoword_length))
            txt_Password.configure(text = Genrated_Password)
            txt_Password.update()
        

    elif selected_rdbutton == 3:
            alphabets_uppercase = string.ascii_uppercase
            alphabets_lowercase = string.ascii_lowercase
            numbers = string.digits
            punctuations =  string.punctuation
            all_characters = []
            all_characters.extend(list(alphabets_uppercase))
            all_characters.extend(list(alphabets_lowercase))
            all_characters.extend(list(numbers))
            all_characters.extend(list(punctuations))
            random.shuffle(all_characters)
            
            Genrated_Password =  "".join(random.sample(all_characters, passoword_length))
            txt_Password.configure(text = Genrated_Password)
            txt_Password.update()
            


    
        # Means Text Is Created
        

spinlength = Spinbox(password_genrator, from_=1, to_=100, textvariable=val, width=13).pack()

bt_GenPass = tkinter.Button(
    bg = function.Functions.color_rgb(72,209,204),
    font = FONT_STYLE,
    width = 25,
    text = 'Genrate Password',
    bd = 0,
    activebackground = function.Functions.color_rgb(0,128,128),
    command = GenratePassword
    )
bt_GenPass.pack(pady = 20)
global txt_password
txt_Password = Label(password_genrator,bg = function.Functions.color_rgb(56, 211, 104),text = 'Your Password Will Be Shown Here',height = 1,font = FONT_STYLE)
txt_Password.pack()







password_genrator.mainloop()
