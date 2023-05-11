import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("252x300")
        self.title("Calculator")
        self.resizable(False, False)

        self.main_frame = tk.Frame(self, bg="red")
        self.main_frame.grid(row=0, column=0)

        self.view = tk.Label(self.main_frame, text='0', bg="blue", fg="white",height= 4)
        self.view.grid(row=0, column=0,columnspan=4, sticky='e')

        digits_pad = tk.Frame(self.main_frame, bg="red")
        digits_pad.grid(row=1, column=0,pady=10)

        button_clear = tk.Button(digits_pad, text='C', height=2,width=3, command=self.clear)
        button_clear.grid(row=0, column=0, sticky='WE', columnspan=1)

        button_pn = tk.Button(digits_pad, text='±', height=2,width=3, command=lambda: self.button_press(''))
        button_pn.grid(row=0, column=1, sticky='WE', columnspan=1)

        button_per = tk.Button(digits_pad, text='%', height=2,width=3, command=lambda: self.button_press(''))
        button_per.grid(row=0, column=2, sticky='WE', columnspan=1)

        button_div = tk.Button(digits_pad, text='÷', height=2,width=3, command=lambda: self.button_press)
        button_div.grid(row=0, column=3, sticky='WE', columnspan=1)

        button_7 = tk.Button(digits_pad, text='7', height=2,width=3, command=lambda: self.num_press('7'))
        button_7.grid(row=1, column=0, sticky='WE', columnspan=1)

        button_8 = tk.Button(digits_pad, text='8', height=2,width=3, command=lambda: self.num_press('8'))
        button_8.grid(row=1, column=1, sticky='WE', columnspan=1)

        button_9 = tk.Button(digits_pad, text='9', height=2,width=3, command=lambda: self.num_press('9'))
        button_9.grid(row=1, column=2, sticky='WE', columnspan=1)

        button_mul = tk.Button(digits_pad, text='×', height=2,width=3, command=lambda: self.button_press(''))
        button_mul.grid(row=1, column=3, sticky='WE', columnspan=1)

        button_4 = tk.Button(digits_pad, text='4', height=2,width=3, command=lambda: self.num_press('4'))
        button_4.grid(row=2, column=0, sticky='WE', columnspan=1)

        button_5 = tk.Button(digits_pad, text='5', height=2,width=3, command=lambda: self.num_press('5'))
        button_5.grid(row=2, column=1, sticky='WE', columnspan=1)

        button_6 = tk.Button(digits_pad, text='6', height=2,width=3, command=lambda: self.num_press('6'))
        button_6.grid(row=2, column=2, sticky='WE', columnspan=1)

        button_sub = tk.Button(digits_pad, text='-', height=2,width=3, command=lambda: self.set_op(self.sub))
        button_sub.grid(row=2, column=3, sticky='WE', columnspan=1)

        button_1 = tk.Button(digits_pad, text='1', height=2,width=3, command=lambda: self.num_press('1'))
        button_1.grid(row=3, column=0, sticky='WE', columnspan=1)

        button_2 = tk.Button(digits_pad, text='2', height=2,width=3, command=lambda: self.num_press('2'))
        button_2.grid(row=3, column=1, sticky='WE', columnspan=1)

        button_3 = tk.Button(digits_pad, text='3', height=2,width=3, command=lambda: self.num_press('3'))
        button_3.grid(row=3, column=2, sticky='WE', columnspan=1)

        button_add = tk.Button(digits_pad, text='+', height=2,width=3, command=self.add)
        button_add.grid(row=3, column=3, sticky='WE', columnspan=1)

        button_0 = tk.Button(digits_pad, text='0', height=2,width=3, command=lambda: self.num_press('0'))
        button_0.grid(row=4, column=0, sticky='WE', columnspan=2)

        button_dot = tk.Button(digits_pad, text='.', height=2,width=3, command=lambda: self.button_press(''))
        button_dot.grid(row=4, column=2, sticky='WE', columnspan=1)

        button_eq = tk.Button(digits_pad, text='=', height=2,width=3, command=self.eq)
        button_eq.grid(row=4, column=3, sticky='WE', columnspan=1)
        
        self.operation = self.do_nothing
        self.new_op = False
        self.pressed_eq = False

    def clear(self):
        """ clear view """
        self.view.config(text='0')

    def num_press(self, key):
        """ Append given number to view """
        if self.pressed_eq:
            self.clear()
            self.ans = self.arg2
            self.pressed_eq = False
        result_str = self.view.cget("text") + key
        result_str = str(int(result_str))
        self.view.config(text=result_str)
            

    def add(self):
        self.operation = '+'
        self.ans = self.view.cget("text")
        self.clear()
        self.new_op = True
    
    

    def eq(self):
        if self.new_op:
            self.arg2 = self.view.cget("text")
        else:
            self.ans = self.view.cget("text")
        expression = str(self.ans) + str(self.operation) + str(self.arg2)
        result = eval(expression)
        print(expression, result)
        self.ans = result
        self.view.config(text=str(result))
        self.new_op = False

        self.pressed_eq = True

    # def sub(self):
    #     result = self.ans - self.arg2
    #     result_str = str(result)
    #     self.ans = result
    #     self.view.config(text=result_str)

    def button_press(self,x):
        pass


    def do_nothing(self):
        pass

def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()

