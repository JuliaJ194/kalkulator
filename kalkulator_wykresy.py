
import tkinter.ttk as ttk
from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from numpy import *

okno = Tk()
okno.geometry('1000x600')
okno.configure(background='light blue')
topFrame = Frame(okno)
topFrame.pack()
bottomFrame = Frame(okno)
bottomFrame.pack(side=BOTTOM)
okno.title("Program rysujący wykresy funkcji") 
frame = Frame(okno, width=500, height=440,  bg='white')
frame.pack()
frame.place(x=400,y=100)


def wykres():  
    """Funkcja rysująca wykresy"""

    funkcje = entry1.get().split(';')    #tworzymy listę rozdzielając podane wzory funkcji po ;
    zakres_X = entry2.get().split(',')    #definiujemy zakresy x i y 
    zakres_Y = entry3.get().split(',')
    tytuł = entry4.get()
    etykieta_x = entry5.get()
    etykieta_y = entry6.get()

    x =  arange(float(zakres_X[0]), float(zakres_X[1]), 0.001) #zakres x z dokładnością do 0.001 dla ładniejszych wykresów
    f = Figure(figsize=(5,4))
    ax = f.add_subplot(111)
    y = []    #pusta lista do której dodamy wartości y dla każdej funkcji z osobna
    for i in range(len(funkcje)):
        y.append(eval(funkcje[i]))   #używając funkcji eval tworzymy wykres     
        ax.plot(x, y[i], label=funkcje[i])
    ax.set_xlabel(etykieta_x)    #ustawiamy etykiety, zakresy oraz tytuł
    ax.set_ylabel(etykieta_y)
    ax.set_title(tytuł)
    ax.set_xticks(range(round(float(zakres_X[0])),round(float(zakres_X[1])+1)))
    ax.set_yticks(range(round(float(zakres_Y[0])),round(float(zakres_Y[1])+1)))
    if decyzja.get() == True or len(funkcje)>1: #w przypadku więcej niż jednej funcji legenda tworzy się automatycznie
            ax.legend()

    canvas  = FigureCanvasTkAgg(f, master=frame) #dołączamy wykres do naszego okna, inaczej wyświetla się osobno, poza interfejsem
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, frame)
    toolbar.update()
    canvas._tkcanvas.pack(expand=True)
    canvas.get_tk_widget().pack()
    
def wyczyść():
    """Funkcja usuwająca widgety (wykresy) zanjdujące się w framie."""
    for widget in frame.winfo_children():
        widget.destroy() 

def zamknij():
    """Funkcja zamykająca okno."""
    okno.quit()
    okno.destroy()
    
def przycisk(p):
    """
    Funkcja, która po wciśnięciu guzika wpisuje do okienka entry
    odpowiednie operatory arytmetyczne lub funkcje elementarne.
    """
    entry1.insert(END, p) 
    
przycisk1 = Button(okno, text = "RYSUJ", font = ("Calibri", 14), height=2, width=8,
                   fg = "black", bg = "light green", command = wykres)   #przycisk rysujący wykresy
przycisk1.pack(side=BOTTOM, expand=YES)
przycisk1.place(x=150,y=400)

przycisk2 = Button(bottomFrame, text = "ZAMKNIJ", font = ("Calibri", 12),
                   fg = "black", bg = "light pink", command = zamknij)  #przycisk zamykający okno
przycisk2.pack(side=BOTTOM, expand=YES)  

przycisk3= Button(okno, text = "WYCZYŚĆ", font = ("Calibri", 12),
                   fg = "black", bg = "light pink", command = wyczyść)  #przycisk czyszczący frame z wykresami
przycisk3.pack() 
przycisk3.place(x=160,y=480)

label_błąd = Label(okno, text="",bg='light blue', font = ("Calibri", 12))   #tutaj wyskoczy błąd jeśli się pojawi
label_błąd.pack()
label_błąd.place(x=100,y=550)

label1 = Label(okno, text='Wpisz wzór funkcji', bg='light blue', font = ("Calibri", 12))
label1.pack()
label1.place(x=150, y=100)
entry1 = Entry(okno)
entry1.pack()
entry1.place(x=150, y=140)

label2 = Label(okno, text='Podaj zakres osi X', bg='light blue', font = ("Calibri", 12))
label2.pack()
label2.place(x=100, y=10)
entry2 = Entry(okno)
entry2.pack()
entry2.place(x=100,y=30)

label3 = Label(okno, text='Podaj zakres osi Y', bg='light blue', font = ("Calibri", 12))
label3.pack()
label3.place(x=250, y=10)
entry3 = Entry(okno)
entry3.pack()
entry3.place(x=250,y=30)

label4 = Label(okno, text='Podaj tytuł wykresu', bg='light blue', font = ("Calibri", 12))
label4.pack()
label4.place(x=400, y=10)
entry4 = Entry(okno) 
entry4.pack()
entry4.place(x=405,y=30)

label5 = Label(okno, text='Określ etykietę osi X', bg='light blue', font = ("Calibri", 12))
label5.pack()
label5.place(x=550, y=10)
entry5 = Entry(okno) 
entry5.pack()
entry5.place(x=555,y=30)

label6 = Label(okno, text='Określ etykietę osi Y', bg='light blue', font = ("Calibri", 12))
label6.pack()
label6.place(x=700, y=10)
entry6 = Entry(okno) 
entry6.pack()
entry6.place(x=705,y=30)

decyzja = BooleanVar() #wartość Bool
decyzja.set(False) #domyślnie ustawiamy False
check = Checkbutton(okno, text='legenda', bg='light blue', font = ("Calibri", 12), var=decyzja)   #tworzymy checkbutton odpowiadający za legendę 
check.pack()
check.place(x=850, y=30) 

nawias_lewy = Button(okno, text=' ( ', font = ("Calibri", 10), fg='black', bg='white',   #tworzymy przyciski z operatorami i funkcjami
                     height=1, width=8, command = lambda: przycisk('(')) 
nawias_lewy.pack() 
nawias_lewy.place(x=140,y=180)

nawias_prawy = Button(okno, text=' ) ', font = ("Calibri", 10), fg='black', bg='white',
                      height=1, width=8, command = lambda: przycisk(')')) 
nawias_prawy.pack() 
nawias_prawy.place(x=206,y=180)

plus = Button(okno, text=' + ', font = ("Calibri", 10), fg='black', bg='white',
              height=1, width=8, command = lambda: przycisk('+')) 
plus.pack() 
plus.place(x=140,y=206)

minus = Button(okno, text=' - ', font = ("Calibri", 10),fg='black', bg='white',
               height=1, width=8, command = lambda: przycisk('-')) 
minus.pack()
minus.place(x=206,y=206)

mnożenie = Button(okno, text=' * ', font = ("Calibri", 10), fg='black', bg='white',
                  height=1, width=8, command = lambda: przycisk('*')) 
mnożenie.pack()
mnożenie.place(x=140,y=232)

dzielenie = Button(okno, text=' / ', font = ("Calibri", 10), fg='black', bg='white',
                   height=1, width=8, command = lambda: przycisk('/')) 
dzielenie.pack()
dzielenie.place(x=206,y=232)

potęgowanie = Button(okno, text=' ^ ', font = ("Calibri", 10), fg='black', bg='white',
                     height=1, width=8, command = lambda: przycisk('**'))
potęgowanie.pack()
potęgowanie.place(x=140,y=258)

wartość_bezwzgl = Button(okno, text=' | | ', font = ("Calibri", 10), fg='black', bg='white',
                  height=1, width=8, command =lambda: przycisk('abs'))
wartość_bezwzgl.pack()
wartość_bezwzgl.place(x=206,y=258)

sinus = Button(okno, text=' sin ', font = ("Calibri", 10), fg='black', bg='white',
               height=1, width=8, command = lambda: przycisk('sin'))
sinus.pack()
sinus.place(x=140,y=284)

cosinus = Button(okno, text=' cos ', font = ("Calibri", 10), fg='black', bg='white',
                 height=1, width=8, command = lambda: przycisk('cos'))
cosinus.pack()
cosinus.place(x=206,y=284)

logarytm = Button(okno, text='log', font = ("Calibri", 10), fg='black', bg='white',
                     height=1, width=8, command = lambda: przycisk('log'))
logarytm.pack()
logarytm.place(x=140,y=310)

e = Button(okno, text=' e^', font = ("Calibri", 10), fg='black', bg='white',
                  height=1, width=8, command = lambda: przycisk('exp'))
e.pack()
e.place(x=206,y=310)


okno.mainloop()
