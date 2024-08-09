from tkinter import *
def Story1(win):
    def final(tl:Toplevel, First_Adjective, First_Noun, Number, Plural_Noun, Second_Adjective, First_Verb, Third_Adjective, Second_Noun, Fourth_Adjective, Second_Verb):

        text = f'''
            Are you looking for a {First_Adjective} {First_Noun}? Look no further! Our {First_Adjective} {First_Noun} is now available for only {Number} {Plural_Noun}. This {Second_Adjective} deal won’t last long, so {First_Verb} now!

            Visit our {Third_Adjective} store, and for a limited time, get a free {Second_Noun} with every purchase. Our {Fourth_Adjective} team is ready to {Second_Verb} you with any questions.

            Hurry, this offer ends soon!'''
        #Advertisment_List = ['first adjective', 'first noun', 'number', 'plural noun', 'second adjective', 'first verb', 'third adjective', 'second noun', 'fourth adjective', 'second verb']
        '''
        for word in Advertisment_List:
            sub = "{" + word + "}"
            repl = BlankSpace_Type[word]
            Completed_Story = Completed_Story.replace(sub, BlankSpace_Type[word])
        '''   

        tl.geometry(newGeometry='500x720')

        Label(tl, text='Story:',  wraplength=tl.winfo_width(),font=("Times New Roman", 12), bg='#d8d6ff', fg='#1b335f').place(x=160, y=500)
        Label(tl, text=text,wraplength=tl.winfo_width(),font=("Times New Roman", 13), bg='#d8d6ff', fg='#1b335f').place(x=0, y=525)

    NewScreen = Toplevel(win, bg='#d8d6ff')
    NewScreen.title("Final Advertisement Script")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Final Advertisement Script', font=("Times New Roman", 12), bg='#d8d6ff', fg = '#1b335f').place(x=100, y=0)
    Label(NewScreen, text='Enter the first adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=30)
    Label(NewScreen, text='Enter the first noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=70)
    Label(NewScreen, text='Enter a number:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=110)
    Label(NewScreen, text='Enter a plural noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=150)
    Label(NewScreen, text='Enter the second adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=190)
    Label(NewScreen, text='Enter the first verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=230)
    Label(NewScreen, text='Enter the third adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=270)
    Label(NewScreen, text='Enter the second noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=310)
    Label(NewScreen, text='Enter the fourth adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=350)
    Label(NewScreen, text='Enter the second verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=390)

    
    
    First_Adjective = Entry(NewScreen, width=17)
    First_Adjective.place(x=250, y=30)
    First_Noun = Entry(NewScreen, width=17)
    First_Noun.place(x=250, y=70)
    Number = Entry(NewScreen, width=17)
    Number.place(x=250, y=110)
    Plural_Noun = Entry(NewScreen, width=17)
    Plural_Noun.place(x=250, y=150)
    Second_Adjective = Entry(NewScreen, width=17)
    Second_Adjective.place(x=250, y=190)
    First_Verb = Entry(NewScreen, width=17)
    First_Verb.place(x=250, y=230)
    Third_Adjective = Entry(NewScreen, width=17)
    Third_Adjective.place(x=250, y=270)
    Second_Noun = Entry(NewScreen, width=17)
    Second_Noun.place(x=250, y=310)
    Fourth_Adjective = Entry(NewScreen, width=17)
    Fourth_Adjective.place(x=250, y=350)
    Second_Verb = Entry(NewScreen, width=17)
    Second_Verb.place(x=250, y=390)
    
    
    SubmitButton = Button(NewScreen, text="Submit", background="#FED8E6", fg = '#1b335f', font=('Times', 12), command=lambda:(final(NewScreen, First_Adjective.get(), First_Noun.get(), Number.get(), Plural_Noun.get(), Second_Adjective.get(), First_Verb.get(), Third_Adjective.get(), Second_Noun.get(), Fourth_Adjective.get(), Second_Verb.get())))
    SubmitButton.place(x=150, y=440)
        
    NewScreen.mainloop()


def Story2(win):
    def final(tl:Toplevel, First_Adjective, First_Company_Name, Second_Company_Name, Second_Adjective, First_Plural_Noun, Third_Adjective, Second_Plural_Noun, Verb, Present_Tense_Verb, Emotion):

        text = f'''
            We are thrilled to announce a {First_Adjective} partnership between {First_Company_Name} and {Second_Company_Name}. This collaboration will bring {Second_Adjective} {First_Plural_Noun} and {Third_Adjective} {Second_Plural_Noun} to our customers.

            Together, we will {Verb} to achieve {First_Plural_Noun} and {Second_Plural_Noun} to begin {Present_Tense_Verb}!. We feel incredibly {Emotion} to be partnering together!

            Sincerely, The {First_Company_Name} and {Second_Company_Name} Teams
            '''

   

        tl.geometry(newGeometry='500x720')

        Label(tl, text='Story:',  wraplength=tl.winfo_width(),font=("Times New Roman", 12), bg='#d8d6ff', fg='#1b335f').place(x=160, y=500)
        Label(tl, text=text,wraplength=tl.winfo_width(),font=("Times New Roman", 13), bg='#d8d6ff', fg='#1b335f').place(x=0, y=525)

    NewScreen = Toplevel(win, bg='#d8d6ff')
    NewScreen.title("Exciting Partnership Announcement!")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Exciting Partnership Announcement!', font=("Times New Roman", 12), bg='#d8d6ff', fg = '#1b335f').place(x=100, y=0)
    Label(NewScreen, text='Enter the first adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=30)
    Label(NewScreen, text='Enter the first company name:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=70)
    Label(NewScreen, text='Enter the second company name:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=110)
    Label(NewScreen, text='Enter the second adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=150)
    Label(NewScreen, text='Enter the first plural noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=190)
    Label(NewScreen, text='Enter the third adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=230)
    Label(NewScreen, text='Enter the second plural noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=270)
    Label(NewScreen, text='Enter the verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=310)
    Label(NewScreen, text='Enter the present tense verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=350)
    Label(NewScreen, text='Enter the emotion:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=390)

    
    First_Adjective = Entry(NewScreen, width=17)
    First_Adjective.place(x=250, y=30)
    First_Company_Name = Entry(NewScreen, width=17)
    First_Company_Name.place(x=250, y=70)
    Second_Company_Name = Entry(NewScreen, width=17)
    Second_Company_Name.place(x=250, y=110)
    Second_Adjective = Entry(NewScreen, width=17)
    Second_Adjective.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    First_Plural_Noun = Entry(NewScreen, width=17)
    First_Plural_Noun.place(x=250, y=230)
    Third_Adjective = Entry(NewScreen, width=17)
    Third_Adjective.place(x=250, y=270)
    Second_Plural_Noun = Entry(NewScreen, width=17)
    Second_Plural_Noun.place(x=250, y=310)
    Present_Tense_Verb = Entry(NewScreen, width=17)
    Present_Tense_Verb.place(x=250, y=350)
    Emotion = Entry(NewScreen, width=17)
    Emotion.place(x=250, y=390)
    
    
    SubmitButton = Button(NewScreen, text="Submit", background="#FED8E6", fg = '#1b335f', font=('Times', 12), command=lambda:(final(NewScreen, First_Adjective.get(), First_Company_Name.get(), Second_Company_Name.get(), Second_Adjective.get(), First_Plural_Noun.get(), Third_Adjective.get(), Second_Plural_Noun.get(), Verb.get(), Present_Tense_Verb.get(), Emotion.get())))
    SubmitButton.place(x=150, y=440)
        
    NewScreen.mainloop()
  
def Story3(win):
    def final(tl:Toplevel, Noun, Past_Tense_Verb, First_Adjective, Second_Noun, Present_Tense_Verb, Second_Adjective, Third_Noun, Third_Adjective, Fourth_Adjective, Name):

        text = f'''
            Attention all residents,

            Due to an unexpected {Noun}, we have {Past_Tense_Verb} all {First_Adjective} activities until further notice. Please ensure that your {Second_Noun} is {Present_Tense_Verb} at all times.
            For your safety, avoid {Second_Adjective} {Third_Noun} and remember to end any {Third_Adjective} situations immediately.
            Thank you for your cooperation and understanding during this {Fourth_Adjective} time,
            
            {Name}
            '''

   

        tl.geometry(newGeometry='500x750')

        Label(tl, text='Story:',  wraplength=tl.winfo_width(),font=("Times New Roman", 12), bg='#d8d6ff', fg='#1b335f').place(x=160, y=500)
        Label(tl, text=text,wraplength=tl.winfo_width(),font=("Times New Roman", 13), bg='#d8d6ff', fg='#1b335f').place(x=0, y=525)

    NewScreen = Toplevel(win, bg='#d8d6ff')
    NewScreen.title("Emergency Advisory Notice")
    NewScreen.geometry('500x500')
    Label(NewScreen, text='Emergency Advisory Notice', font=("Times New Roman", 12), bg='#d8d6ff', fg = '#1b335f').place(x=100, y=0)
    Label(NewScreen, text='Enter a noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=30)
    Label(NewScreen, text='Enter a past tense verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=70)
    Label(NewScreen, text='Enter the first adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=110)
    Label(NewScreen, text='Enter the second noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=150)
    Label(NewScreen, text='Enter a present tense verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=190)
    Label(NewScreen, text='Enter the second adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=230)
    Label(NewScreen, text='Enter the third noun:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=270)
    Label(NewScreen, text='Enter the third adjective:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=310)
    Label(NewScreen, text='Enter the verb:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=350)
    Label(NewScreen, text='Enter a name:',font=("Times New Roman", 13), bg='#d8d6ff', fg = '#1b335f').place(x=0, y=390)

    
    
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=30)
    Past_Tense_Verb = Entry(NewScreen, width=17)
    Past_Tense_Verb.place(x=250, y=70)
    First_Adjective = Entry(NewScreen, width=17)
    First_Adjective.place(x=250, y=110)
    Second_Noun = Entry(NewScreen, width=17)
    Second_Noun.place(x=250, y=150)
    Present_Tense_Verb = Entry(NewScreen, width=17)
    Present_Tense_Verb.place(x=250, y=190)
    Second_Adjective = Entry(NewScreen, width=17)
    Second_Adjective.place(x=250, y=230)
    Third_Noun = Entry(NewScreen, width=17)
    Third_Noun.place(x=250, y=270)
    Third_Adjective = Entry(NewScreen, width=17)
    Third_Adjective.place(x=250, y=310)
    Fourth_Adjective = Entry(NewScreen, width=17)
    Fourth_Adjective.place(x=250, y=350)
    Name = Entry(NewScreen, width=17)
    Name.place(x=250, y=390)
    
    
    SubmitButton = Button(NewScreen, text="Submit", background="#FED8E6", fg = '#1b335f', font=('Times', 12), command=lambda:(final(NewScreen, Noun.get(), Past_Tense_Verb.get(), First_Adjective.get(), Second_Noun.get(), Present_Tense_Verb.get(), Second_Adjective.get(), Third_Noun.get(), Third_Adjective.get(), Fourth_Adjective.get(), Name.get())))
    SubmitButton.place(x=150, y=440)
        
    NewScreen.mainloop()
 
# Create the main window
Screen = Tk()
Screen.title("MadLib Game - Bushra")
Screen.geometry('400x400')
Screen.config(bg= '#cce6ff')

# Get the width of the window and the label widget

Label(Screen, text="Madlibs Stories:", font = ('Times New Roman', 24, 'bold'), bg = '#cce6ff', fg = '#0e4b58').place(x=200,y = 30, anchor = 'n')
Story1Button = Button(Screen, text='Final Advertisement Script', font=("Times New Roman", 13), fg = '#0b3c47',command=lambda: Story1(Screen),bg='#d0ccff', activebackground= '#c5c2ff')
Story1Button.place(x=200, y=140, anchor="center")
Story2Button = Button(Screen, text='Exciting Partnership Announcement!', font=("Times New Roman", 13), fg = '#0b3c47',command=lambda: Story2(Screen), bg='#d0ccff', activebackground= '#c5c2ff')
Story2Button.place(x = 200, y = 200, anchor="center")
Story3Button = Button(Screen, text='Emergency Advisory Notice', font=("Times New Roman", 13), fg = '#0b3c47',command=lambda: Story3(Screen), bg='#d0ccff', activebackground= '#c5c2ff')
Story3Button.place(x=200, y=260, anchor = 'center')


Screen.update()
Screen.mainloop()

