import tkinter as tk
from tkmacosx import Button

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        # Initialize constants
        self.app_font = ("SF Pro Text Medium", 15)
        self.blue = '#0a84ff'
        self.grey = '#1b1b25'

        # Configure calculator window
        self.geometry("252x300")
        self.title("Calculator")
        self.resizable(False, False)

        # Initialize upper most Frame and add it to Tk
        self.master_frame = tk.Frame(self, bg="#1c1c1c")
        self.master_frame.grid(row=0, column=0)
        
        # Initialize calculator display and add it to master Frame
        self.display = tk.Label(self.master_frame, text='0', bg=self.grey, \
            fg="white", height=2, font=("SF Pro Text Medium", 22), \
                width=16, anchor="e", justify="right")
        self.display.grid(row=0, column=0,columnspan=4, sticky='we', pady=5)

        # Initialize Frame to enclose buttons
        self.digits_pad = tk.Frame(self.master_frame, bg="white")
        self.digits_pad.grid(row=1, column=0,pady=0)

        # Initialize buttons and add them to frame
        self.button_clear = Button(self.digits_pad, text='C',\
            activebackground=self.blue,font=self.app_font,height=46,width=63,\
                borderwidth=0,command=self.clear)
        self.button_clear.grid(row=0, column=0, sticky='WE', columnspan=1)

        self.button_pn = Button(self.digits_pad, text='±', \
            activebackground=self.blue, font=self.app_font,height=46,width=63,\
                command=self.pn)
        self.button_pn.grid(row=0, column=1, sticky='WE', columnspan=1)

        self.button_per = Button(self.digits_pad, text='%', \
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=self.perc)
        self.button_per.grid(row=0, column=2, sticky='WE', columnspan=1)

        self.button_div = Button(self.digits_pad, text='÷', \
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.set_op('/'))
        self.button_div.grid(row=0, column=3, sticky='WE', columnspan=1)

        self.button_7 = Button(self.digits_pad, text='7', \
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('7'))
        self.button_7.grid(row=1, column=0, sticky='WE', columnspan=1)

        self.button_8 = Button(self.digits_pad, text='8',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('8'))
        self.button_8.grid(row=1, column=1, sticky='WE', columnspan=1)

        self.button_9 = Button(self.digits_pad, text='9',\
            activebackground=self.blue, font=self.app_font, height=46,
                width=63, command=lambda: self.num_press('9'))
        self.button_9.grid(row=1, column=2, sticky='WE', columnspan=1)

        self.button_mul = Button(self.digits_pad, text='×',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.set_op('*'))
        self.button_mul.grid(row=1, column=3, sticky='WE', columnspan=1)

        self.button_4 = Button(self.digits_pad, text='4',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('4'))
        self.button_4.grid(row=2, column=0, sticky='WE', columnspan=1)

        self.button_5 = Button(self.digits_pad, text='5',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('5'))
        self.button_5.grid(row=2, column=1, sticky='WE', columnspan=1)

        self.button_6 = Button(self.digits_pad, text='6',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('6'))
        self.button_6.grid(row=2, column=2, sticky='WE', columnspan=1)

        self.button_sub = Button(self.digits_pad, text='-',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.set_op('-'))
        self.button_sub.grid(row=2, column=3, sticky='WE', columnspan=1)

        self.button_1 = Button(self.digits_pad, text='1',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('1'))
        self.button_1.grid(row=3, column=0, sticky='WE', columnspan=1)

        self.button_2 = Button(self.digits_pad, text='2',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('2'))
        self.button_2.grid(row=3, column=1, sticky='WE', columnspan=1)

        self.button_3 = Button(self.digits_pad, text='3',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('3'))
        self.button_3.grid(row=3, column=2, sticky='WE', columnspan=1)

        self.button_add = Button(self.digits_pad, text='+',
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.set_op('+'))
        self.button_add.grid(row=3, column=3, sticky='WE', columnspan=1)

        self.button_0 = Button(self.digits_pad, text='0',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=lambda: self.num_press('0'))
        self.button_0.grid(row=4, column=0, sticky='WE', columnspan=2)

        self.button_dot = Button(self.digits_pad, text='.',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=self.dot)
        self.button_dot.grid(row=4, column=2, sticky='WE', columnspan=1)

        self.button_eq = Button(self.digits_pad, text='=',\
            activebackground=self.blue, font=self.app_font, height=46,\
                width=63, command=self.eq)
        self.button_eq.grid(row=4, column=3, sticky='WE', columnspan=1)
        
        # Control booleans
        self.new_op = False
        self.pressed_eq = False

        # Operation elements
        self.ans = 0
        self.operation = ''
        self.arg2 = 0

    def clear(self):
        """ Clears calculator display """
        self.display.config(text='0')

    def num_press(self, key):
        """ Appends given number to displayed number """
        # If last key pressed was equal, clear display
        if self.pressed_eq:
            self.clear()
            self.pressed_eq = False
        
        # Append pressed key to number in display
        result_str = self.display.cget("text") + key

        # Convert to integer or decimal to remove leading zeros
        try:
            result = int(result_str)
        except ValueError:
            result = float(result_str)
        result_str = str(result)
        
        # Remove last character if string exceeds 17 characters
        if len(result_str)>16:
            result_str = result_str[:17]

        # Display new number
        self.display.config(text=result_str)
            
    def set_op(self, op):
        """ Sets current operation to be performed, saves and clears display """
        self.operation = op
        self.ans = self.display.cget("text")
        self.clear()
        self.new_op = True

    def perc(self):
        """ Converts percentage to decimal """
        perc = float(self.display.cget("text"))/100
        self.display.config(text=str(perc))
        self.pressed_eq = True

    def eq(self):
        """ Evaluates inputted expression making necessary adjustments """
        # If user is performing a new operation,
        if self.new_op:
            self.arg2 = self.display.cget("text")
        else:
            self.ans = self.display.cget("text")
        
        # Get, evaluate and convert expression to string
        expression = str(self.ans) + str(self.operation) + str(self.arg2)
        result = round(eval(expression),8)
        result_str = str(result)

        # Convert to scientific notation if result is too big for the screen
        if len(result_str)>16:
            result_str = "{:e}".format(float(result))

        self.ans = result
        self.display.config(text=result_str)

        self.new_op = False
        self.pressed_eq = True


    def pn(self):
        """ Changes displayed number to be negative or positive"""
        display_str = self.display.cget("text")
        if display_str[0] == '-':
            self.display.config(text=str(display_str[1:]))
        elif len(display_str)<17:
            self.display.config(text=str('-'+display_str))
    
    def dot(self):
        """ Adds '.' to displayed number if it does not have it already """
        if self.pressed_eq:
            self.clear()
            self.pressed_eq = False

        display_str = self.display.cget("text")
        if '.' not in display_str and len(display_str)<16:
             self.display.config(text=str(display_str+'.'))

def main():
    app = Calculator()
    app.mainloop()

if __name__ == '__main__':
    main()

