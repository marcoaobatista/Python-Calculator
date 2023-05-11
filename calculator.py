import tkinter as tk
from tkmacosx import Button

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        app_font = ("SF Pro Text Medium", 15)
        active_bg = '#0a84ff'
        self.geometry("252x300")
        self.title("Calculator")
        self.resizable(False, False)

        self.main_frame = tk.Frame(self, bg="#1c1c1c")
        self.main_frame.grid(row=0, column=0)

        self.view = tk.Label(self.main_frame, text='0', bg='#1c1c1c', fg="white", height=2, font=("SF Pro Text Medium", 22), width=16, anchor="e", justify="right")
        self.view.grid(row=0, column=0,columnspan=4, sticky='we', pady=5)

        digits_pad = tk.Frame(self.main_frame, bg="white")
        digits_pad.grid(row=1, column=0,pady=0)

        

        button_clear = Button(digits_pad, text='C',activebackground=active_bg,font=app_font,height=46,width=63,borderwidth=0,command=self.clear)
        button_clear.grid(row=0, column=0, sticky='WE', columnspan=1)

        button_pn = Button(digits_pad, text='±', activebackground=active_bg,font=app_font,height=46,width=63, command=self.pn)
        button_pn.grid(row=0, column=1, sticky='WE', columnspan=1)

        button_per = Button(digits_pad, text='%', activebackground=active_bg,font=app_font, height=46,width=63, command=self.perc)
        button_per.grid(row=0, column=2, sticky='WE', columnspan=1)

        button_div = Button(digits_pad, text='÷', activebackground=active_bg,font=app_font, height=46,width=63, command=self.div)
        button_div.grid(row=0, column=3, sticky='WE', columnspan=1)

        button_7 = Button(digits_pad, text='7', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('7'))
        button_7.grid(row=1, column=0, sticky='WE', columnspan=1)

        button_8 = Button(digits_pad, text='8', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('8'))
        button_8.grid(row=1, column=1, sticky='WE', columnspan=1)

        button_9 = Button(digits_pad, text='9', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('9'))
        button_9.grid(row=1, column=2, sticky='WE', columnspan=1)

        button_mul = Button(digits_pad, text='×', activebackground=active_bg,font=app_font, height=46,width=63, command=self.mul)
        button_mul.grid(row=1, column=3, sticky='WE', columnspan=1)

        button_4 = Button(digits_pad, text='4', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('4'))
        button_4.grid(row=2, column=0, sticky='WE', columnspan=1)

        button_5 = Button(digits_pad, text='5', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('5'))
        button_5.grid(row=2, column=1, sticky='WE', columnspan=1)

        button_6 = Button(digits_pad, text='6', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('6'))
        button_6.grid(row=2, column=2, sticky='WE', columnspan=1)

        button_sub = Button(digits_pad, text='-', activebackground=active_bg,font=app_font, height=46,width=63, command=self.sub)
        button_sub.grid(row=2, column=3, sticky='WE', columnspan=1)

        button_1 = Button(digits_pad, text='1', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('1'))
        button_1.grid(row=3, column=0, sticky='WE', columnspan=1)

        button_2 = Button(digits_pad, text='2', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('2'))
        button_2.grid(row=3, column=1, sticky='WE', columnspan=1)

        button_3 = Button(digits_pad, text='3', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('3'))
        button_3.grid(row=3, column=2, sticky='WE', columnspan=1)

        button_add = Button(digits_pad, text='+', activebackground=active_bg,font=app_font, height=46,width=63, command=self.add)
        button_add.grid(row=3, column=3, sticky='WE', columnspan=1)

        button_0 = Button(digits_pad, text='0', activebackground=active_bg,font=app_font, height=46,width=63, command=lambda: self.num_press('0'))
        button_0.grid(row=4, column=0, sticky='WE', columnspan=2)

        button_dot = Button(digits_pad, text='.', activebackground=active_bg,font=app_font, height=46,width=63, command=self.dot)
        button_dot.grid(row=4, column=2, sticky='WE', columnspan=1)

        button_eq = Button(digits_pad, text='=',activebackground=active_bg,font=app_font, height=46,width=63, command=self.eq)
        button_eq.grid(row=4, column=3, sticky='WE', columnspan=1)
        
        self.operation = ''
        self.new_op = False
        self.pressed_eq = False
        self.ans = 0
        self.arg2 = 0

    def clear(self):
        """ clear view """
        self.view.config(text='0')

    def num_press(self, key):
        """ Append given number to view """
        if self.pressed_eq:
            self.clear()
            self.pressed_eq = False
        result_str = self.view.cget("text") + key
        try:
            result = int(result_str)
        except ValueError:
            result = float(result_str)

        result_str = str(result)
        
        if len(result_str)>16:
            result_str = result_str[:17]

        self.view.config(text=result_str)
        print()
        print("ans:", self.ans)
        print("op:", self.operation)
        print("arg2:", self.arg2)
            

    def add(self):
        self.operation = '+'
        self.ans = self.view.cget("text")
        self.clear()
        self.new_op = True
    
    def sub(self):
        self.operation = '-'
        self.ans = self.view.cget("text")
        self.clear()
        self.new_op = True
    
    def mul(self):
        self.operation = '*'
        self.ans = self.view.cget("text")
        self.clear()
        self.new_op = True

    def perc(self):
        perc = float(self.view.cget("text"))/100
        self.view.config(text=str(perc))
        self.pressed_eq = True

    def eq(self):
        if self.new_op:
            self.arg2 = self.view.cget("text")
        else:
            self.ans = self.view.cget("text")

        print()
        print("ans:", self.ans)
        print("op:", self.operation)
        print("arg2:", self.arg2)

        expression = str(self.ans) + str(self.operation) + str(self.arg2)
        result = round(eval(expression),8)
        result_str = str(result)

        if len(result_str)>16:
            result_str = "{:e}".format(float(result))

        print(expression, result_str)
        self.ans = result
        self.view.config(text=result_str)
        self.new_op = False

        self.pressed_eq = True


    def pn(self):
        result = self.view.cget("text")
        if result[0] == '-':
            self.view.config(text=str(result[1:]))
        else:
            self.view.config(text=str('-'+result))
    
    def dot(self):
        if self.pressed_eq:
            self.clear()
            self.pressed_eq = False

        result = self.view.cget("text")
        
        if '.' not in result and len(result)<16:
             self.view.config(text=str(result+'.'))

    def div(self):
        self.operation = '/'
        self.ans = self.view.cget("text")
        self.clear()
        self.new_op = True


    def do_nothing(self):
        pass

def main():
    app = Calculator()
    app.mainloop()

if __name__ == '__main__':
    main()

