import tkinter as tk
RED=("#E20A0A")
GREEN=("#0AEE25")
WHITE=("#FFFFFF")
BLACK=("#000000")
LARGE_FONT_STYLE= ("Arial", 40, "bold")
DIGITS_FONT_STYLE= ("Arial", 24 , "bold")
class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()
        self.total_expression=""
        self.curnent_expression=""
        self.digits={7:(1,1), 8:(1,2), 9:(1,3), 
                     4:(2,1), 5:(2,2), 6:(2,3),
                     1:(3,1), 2:(3,2), 3:(3,3),
                     0:(4,1), ".":(4,2)}
        self.operators={"/":"\u00F7", "*":"\u00D7", "-":"-", "+":"+"}
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_sqrt_button()
        self.create_square_button()
        self.create_clear_button()
        self.create_equal_button()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)
        self.total_label, self.label=self.create_display_label()
    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221)
        frame.pack(expand=True,fill="both")
        return frame
    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame, text=str(digit), bg=RED, font= DIGITS_FONT_STYLE, command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)
    def create_operator_buttons(self):
        i=0
        for operator, symbol in self.operators.items():
            button=tk.Button(self.buttons_frame, text=operator, bg=RED, font= DIGITS_FONT_STYLE, command=lambda x=operator:self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i+=1
    def create_sqrt(self):
        self.curnent_expression=str(eval(f"{self.curnent_expression}**0.5"))
        self.update_label()
    def create_sqrt_button(self):
        button=tk.Button(self.buttons_frame, text="\u221ax", bg=RED, font=DIGITS_FONT_STYLE,command=self.create_sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)
    def create_square(self):
        self.curnent_expression=str(eval(f"{self.curnent_expression}**2"))
        self.update_label()
    def create_square_button(self):
        button=tk.Button(self.buttons_frame, text="x\u00b2", bg=RED, font=DIGITS_FONT_STYLE, command=self.create_square)
        button.grid(row=0, column=2, sticky=tk.NSEW)
    def create_clear(self):
        self.total_expression=""
        self.curnent_expression=""
        self.update_label()
        self.update_total_label()
    def create_clear_button(self):
        button=tk.Button(self.buttons_frame, text="del", bg=RED, font=DIGITS_FONT_STYLE, command= self.create_clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
    def create_equal_button(self):
        button=tk.Button(self.buttons_frame, text="=", bg=GREEN, font=DIGITS_FONT_STYLE, command= self.create_evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)
    def create_evaluate(self):
        self.total_expression+=self.curnent_expression
        self.update_total_label()
        try:
            self.curnent_expression=str(eval(self.total_expression))
            self.total_expression=""
        except Exception:
            self.curnent_expression="Err"
        finally:
            self.update_label()
    def append_operator(self, operator):
        self.curnent_expression+=operator
        self.total_expression+=self.curnent_expression
        self.curnent_expression=""
        self.update_label()
        self.update_total_label()
    def create_display_label(self):
        total_label=tk.Label(self.display_frame, text= self.total_expression, bg=BLACK, fg=WHITE, font= LARGE_FONT_STYLE)
        total_label.pack(expand=True,fill="both")
        label=tk.Label(self.display_frame, text= self.curnent_expression, bg=BLACK, fg=WHITE, font=LARGE_FONT_STYLE)
        label.pack (expand=True,fill="both")
        return total_label, label
    def add_to_expression(self, value):
        self.curnent_expression+=str(value)
        self.update_label()
    def update_total_label(self):
        expression=self.total_expression
        for operator, symbol in self.operators.items():
            expression=expression.replace(operator, f"{symbol}")
        self.total_label.config(text=expression)
    def update_label(self):
        self.label.config(text=self.curnent_expression [:13])
    def run(self):
        self.window.mainloop()
calculator=Calculator()
calculator.run()
