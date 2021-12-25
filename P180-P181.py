from tkinter import *
from tkinter import ttk 
from googletrans import Translator
from googletrans import LANGUAGES
root = Tk()
root.geometry('800x600')
root.config(bg='lightblue')

label_title = Label(root,text='LANGUAGE TRANSLATOR',bg='lightblue',font=('Sylfean',30,'bold')) 
label_title.place(relx=0.5,rely=0.1,anchor=CENTER)

label = Label(root,text='Enter Text',bg='lightblue',font=('Sylfean',20))
label.place(relx=0.19,rely=0.3,anchor=W)

textarea = Text(root,bg='white',font=('Sylfean',18),height=10,wrap='word',width=25,padx=2,pady=2,bd=0)
textarea.place(relx=0.25,rely=0.55,anchor=CENTER)

language = list(LANGUAGES.values())
dropdown = ttk.Combobox(state='readonly',values=language,width=18)
dropdown.place(relx=0.82,rely=0.3,anchor=CENTER)
dropdown.set('english')

label2 = Label(root,text='Output',bg='lightblue',font=('Sylfean',20))
label2.place(relx=0.6,rely=0.3,anchor=W)

textarea2 = Text(root,bg='white',font=('Sylfean',18),height=10,wrap='word',width=25,padx=2,pady=2,bd=0)
textarea2.place(relx=0.75,rely=0.55,anchor=CENTER)

def translate():
    obj = Translator()
    try:
        translated = translator.translate(text=textarea.get(1.0,END),sr =src_lang.get(),dest=textarea2)
        textarea2.delete(1.0,END)
        textarea2.insert(END,translated.text)
    except:
        print('Try Again!')
        
btn = Button(root,text='Translate',command=translate,font=('Sylfean',20,'bold'),background='blue',activebackground='green',fg='black',relief=FLAT,pady=0.1)
btn.place(relx=0.5,rely=0.9,anchor=S)

root.mainloop()