import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("252x300")
        self.title("Calculator")
        self.resizable(False, False)

        self.main_frame = tk.Frame(self, bg="red")
        self.main_frame.grid(row=0, column=0)

        view = tk.Label(self.main_frame, text='123455', bg="blue", fg="white",height= 6)
        view.grid(row=0, column=0,columnspan=4, sticky='e')

        self.create_pad()
        
    def create_pad(self):
        digits_pad = tk.Frame(self.main_frame, bg="red")
        digits_pad.grid(row=1, column=0,pady=12)
        
        buttons = [['7','8','9','x'],
                   ['4','5','6','-'],
                   ['1','2','3','+'],
                   ['0 ','.','=']]
        
        for row in range(len(buttons)):
            col = 0
            for ch in buttons[row]:
                button = tk.Button(digits_pad, text=ch, height= 2, width=3)
                button.grid(row=row, column=col, sticky='nsew', columnspan=len(ch))
                col += len(ch)
        
        
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()

