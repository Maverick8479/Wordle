import tkinter as tk
from tkinter import ttk

class KeyBoard(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.exp = " "
        self.style = ttk.Style()
        self.configure(bg='white')
        self.style.configure('TButton', background='white')
        self.style.configure('TButton', foreground='black')

        self.theme = "light"

        self.equation = tk.StringVar()
        Dis_entry = ttk.Entry(self, state='normal', textvariable=self.equation)
        Dis_entry.grid(rowspan=1, columnspan=100, ipadx=999, ipady=20)

        backspace = ttk.Button(
            self, text='<---', width=6, command=self.Backspace)
        backspace.grid(row=1, column=13, ipadx=6, ipady=10)

        # Second Line Buttons

        self.tab_button = ttk.Button(self, text='Tab', width=6,
                                command=lambda: self.press('\t'))
        self.tab_button.grid(row=2, column=0, columnspan=2, ipadx=55, ipady=10)

        self.Q = ttk.Button(self, text='Q', width=6, command=lambda: self.press('Q'))
        self.Q.grid(row=2, column=2, ipadx=6, ipady=10)

        self.W = ttk.Button(self, text='W', width=6, command=lambda: self.press('W'))
        self.W.grid(row=2, column=3, ipadx=6, ipady=10)

        self.E = ttk.Button(self, text='E', width=6, command=lambda: self.press('E'))
        self.E.grid(row=2, column=4, ipadx=6, ipady=10)

        self.R = ttk.Button(self, text='R', width=6, command=lambda: self.press('R'))
        self.R.grid(row=2, column=5, ipadx=6, ipady=10)

        self.T = ttk.Button(self, text='T', width=6, command=lambda: self.press('T'))
        self.T.grid(row=2, column=6, ipadx=6, ipady=10)

        self.Y = ttk.Button(self, text='Y', width=6, command=lambda: self.press('Y'))
        self.Y.grid(row=2, column=7, ipadx=6, ipady=10)

        self.U = ttk.Button(self, text='U', width=6, command=lambda: self.press('U'))
        self.U.grid(row=2, column=8, ipadx=6, ipady=10)

        self.I = ttk.Button(self, text='I', width=6, command=lambda: self.press('I'))
        self.I.grid(row=2, column=9, ipadx=6, ipady=10)

        self.O = ttk.Button(self, text='O', width=6, command=lambda: self.press('O'))
        self.O.grid(row=2, column=10, ipadx=6, ipady=10)

        self.P = ttk.Button(self, text='P', width=6, command=lambda: self.press('P'))
        self.P.grid(row=2, column=11, ipadx=6, ipady=10)

        self.curly_l = ttk.Button(
            self, text='{', width=6, command=lambda: self.press('{'))
        self.curly_l.grid(row=2, column=12, ipadx=6, ipady=10)

        self.curly_r = ttk.Button(self, text='}', width=6,
                             command=lambda: self.press('}'))
        self.curly_r.grid(row=2, column=13, ipadx=6, ipady=10)

        # Third Line Buttons

        self.A = ttk.Button(self, text='A', width=6, command=lambda: self.press('A'))
        self.A.grid(row=3, column=0, ipadx=6, ipady=10)

        self.S = ttk.Button(self, text='S', width=6, command=lambda: self.press('S'))
        self.S.grid(row=3, column=1, ipadx=6, ipady=10)

        self.D = ttk.Button(self, text='D', width=6, command=lambda: self.press('D'))
        self.D.grid(row=3, column=2, ipadx=6, ipady=10)

        self.F = ttk.Button(self, text='F', width=6, command=lambda: self.press('F'))
        self.F.grid(row=3, column=3, ipadx=6, ipady=10)

        self.G = ttk.Button(self, text='G', width=6, command=lambda: self.press('G'))
        self.G.grid(row=3, column=4, ipadx=6, ipady=10)

        self.H = ttk.Button(self, text='H', width=6, command=lambda: self.press('H'))
        self.H.grid(row=3, column=5, ipadx=6, ipady=10)

        self.J = ttk.Button(self, text='J', width=6, command=lambda: self.press('J'))
        self.J.grid(row=3, column=6, ipadx=6, ipady=10)

        self.K = ttk.Button(self, text='K', width=6, command=lambda: self.press('K'))
        self.K.grid(row=3, column=7, ipadx=6, ipady=10)

        self.L = ttk.Button(self, text='L', width=6, command=lambda: self.press('L'))
        self.L.grid(row=3, column=8, ipadx=6, ipady=10)

        # colon = ttk.Button(self, text=':', width=6,
        #    command=lambda: self.press(':'))
        # colon.grid(row=3, column=9, ipadx=6, ipady=10)

        # quotation = ttk.Button(self, text='"', width=6,
        #    command=lambda: self.press('"'))
        # quotation.grid(row=3, column=10, ipadx=6, ipady=10)

        # pipe = ttk.Button(self, text='|', width=6, command=lambda: self.press('|'))
        # pipe.grid(row=3, column=11, ipadx=6, ipady=10)

        # enter = ttk.Button(self, text='Enter', width=6,
        #    command=lambda: self.press('\n'))
        # enter.grid(row=3, column=12, columnspan=2, ipadx=55, ipady=10)

        # Fourth line Buttons

        # shift = ttk.Button(self, text='Shift', width=6, command=Shift)
        # shift.grid(row=4, column=0, columnspan=2, ipadx=55, ipady=10)

        self.Z = ttk.Button(self, text='Z', width=6, command=lambda: self.press('Z'))
        self.Z.grid(row=4, column=2, ipadx=6, ipady=10)

        self.X = ttk.Button(self, text='X', width=6, command=lambda: self.press('X'))
        self.X.grid(row=4, column=3, ipadx=6, ipady=10)

        self.C = ttk.Button(self, text='C', width=6, command=lambda: self.press('C'))
        self.C.grid(row=4, column=4, ipadx=6, ipady=10)

        self.V = ttk.Button(self, text='V', width=6, command=lambda: self.press('V'))
        self.V.grid(row=4, column=5, ipadx=6, ipady=10)

        self.B = ttk.Button(self, text='B', width=6, command=lambda: self.press('B'))
        self.B.grid(row=4, column=6, ipadx=6, ipady=10)

        self.N = ttk.Button(self, text='N', width=6, command=lambda: self.press('N'))
        self.N.grid(row=4, column=7, ipadx=6, ipady=10)

        self.M = ttk.Button(self, text='M', width=6, command=lambda: self.press('M'))
        self.M.grid(row=4, column=8, ipadx=6, ipady=10)

        # ang_l = ttk.Button(self, text='<', width=6, command=lambda: self.press('<'))
        # ang_l.grid(row=4, column=9, ipadx=6, ipady=10)
    #
        # ang_r = ttk.Button(self, text='>', width=6, command=lambda: self.press('>'))
        # ang_r.grid(row=4, column=10, ipadx=6, ipady=10)
    #
        # question = ttk.Button(self, text='?', width=6,
        #   command=lambda: self.press('?'))
        # question.grid(row=4, column=11, ipadx=6, ipady=10)

        self.clear = ttk.Button(self, text='Clear', width=6, command=self.Clear)
        self.clear.grid(row=4, column=12, columnspan=2, ipadx=55, ipady=10)

        # Fifth Line Buttons

        self.space = ttk.Button(self, text='Space', width=6,
                           command=lambda: self.press(' '))
        self.space.grid(row=5, column=2, columnspan=8, ipadx=350, ipady=10)

        self.theme = ttk.Button(self, text='Theme', width=6, command=self.Theme)
        self.theme.grid(row=5, column=12, columnspan=2, ipadx=55, ipady=10)

    def press(self, num):
        self.exp = self.exp + str(num)
        self.equation.set(self.exp)


    def Backspace(self):
        self.exp = self.exp[:-1]
        self.equation.set(self.exp)


    # def Shift():
    #     global is_shift
    #     is_shift = not is_shift
    #     display()


    def Clear(self):
        self.exp = " "
        self.equation.set(self.exp)


    def Theme(self):
        if self.theme == "dark":
            self.configure(bg='gray27')
            self.style.configure('TButton', background='gray21')
            self.style.configure('TButton', foreground='white')
            self.theme = "light"
        elif self.theme == "light":
            self.configure(bg='gray99')
            self.style.configure('TButton', background='azure')
            self.style.configure('TButton', foreground='black')
            self.theme = "dark"


root = tk.Tk()
root.title('On Screen Keyboard')


root.geometry('1385x320')  # Window size
root.maxsize(width=1385, height=320)
root.minsize(width=1385, height=320)

keybboard = KeyBoard(root)
keybboard.grid()

root.mainloop()
