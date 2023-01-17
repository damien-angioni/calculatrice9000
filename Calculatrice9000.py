from tkinter import *
result=0
ligne=""
calc=Tk()
calc.configure(background="light gray")
calc.title("Calculatrice")
calc.geometry('420x350')
affiche=StringVar()
affiche.set("Bienvenue dans la calculatrice de moi")
def Effacer():
    global ligne
    ligne=""
    affiche.set("0")
def Egal():
    global ligne
    chk_div_0=ligne.__contains__("/0")
    if chk_div_0==True:
        affiche.set("Error: div by 0")
    else:
        result = str(eval(ligne))
    affiche.set(result)
    ligne = ""
def clique(effet):
    global ligne
    ligne = ligne + str(effet)
    affiche.set(ligne)
label=Label(calc,textvariable=affiche,font=('times 17'), width=31, height=2).place(x=5,y=5)
boutonpls = Button(calc,text="+",command=lambda: clique("+"),height= 3, width=7,cursor = "hand2").place(x=355,y=75)
boutonmns = Button(calc,text="-",command=lambda: clique("-"),height= 3, width=7,cursor = "hand2").place(x=285,y=75)
boutondvd = Button(calc,text="/",command=lambda: clique("/"),height= 3, width=7,cursor = "hand2").place(x=285,y=145)
boutonmlt = Button(calc,text="X",command=lambda: clique("*"),height= 3, width=7,cursor = "hand2").place(x=355,y=145)
boutonprct = Button(calc,text="%",command=lambda: clique("%"),height= 3, width=7,cursor = "hand2").place(x=285,y=215)
boutonroot = Button(calc,text="√",command=lambda: clique("**0.5"),height= 3, width=7,cursor = "hand2").place(x=355,y=215)
boutonrslt = Button(calc,text="=",command=Egal,height= 8, width=7,cursor = "hand2").place(x=215,y=211)
boutonCE = Button(calc,text="CE",command=Effacer,height= 8, width=7,cursor = "hand2").place(x=215,y=75)
boutondot = Button(calc,text=".",command=lambda: clique("."),height= 3, width=7,cursor = "hand2").place(x=145,y=285)
bouton0 = Button(calc,text="0",command=lambda: clique("0"),height= 3, width=17,cursor = "hand2").place(x=5,y=285)
bouton1 = Button(calc,text="1",command=lambda: clique("1"),height= 3, width=7,cursor = "hand2").place(x=5,y=215)
bouton2 = Button(calc,text="2",command=lambda: clique("2"),height= 3, width=7,cursor = "hand2").place(x=75,y=215)
bouton3 = Button(calc,text="3",command=lambda: clique("3"),height= 3, width=7,cursor = "hand2").place(x=145,y=215)
bouton4 = Button(calc,text="4",command=lambda: clique("4"),height= 3, width=7,cursor = "hand2").place(x=5,y=145)
bouton5 = Button(calc,text="5",command=lambda: clique("5"),height= 3, width=7,cursor = "hand2").place(x=75,y=145)
bouton6 = Button(calc,text="6",command=lambda: clique("6"),height= 3, width=7,cursor = "hand2").place(x=145,y=145)
bouton7 = Button(calc,text="7",command=lambda: clique("7"),height= 3, width=7,cursor = "hand2").place(x=5,y=75)
bouton8 = Button(calc,text="8",command=lambda: clique("8"),height= 3, width=7,cursor = "hand2").place(x=75,y=75)
bouton9 = Button(calc,text="9",command=lambda: clique("9"),height= 3, width=7,cursor = "hand2").place(x=145,y=75)
fermer = Button(calc, text="Fermer", command=calc.destroy,height= 3, width=17,cursor = "hand2").place(x=285,y=285)
calc.mainloop()