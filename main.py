import json
import math
import os
import re
import tkinter as tk
from tkinter import messagebox

CF = "calc_user.settings"

def load_s():
    if not os.path.exists(CF):
        return {"t": "light", "l": 0.0}
    try:
        with open(CF, "r") as f:
            d = json.load(f)
            d['l'] = float(d.get('l', 0.0))
            return d
    except Exception:
        print("W: FTL. UD.")
        return {"t": "light", "l": 0.0}

def save_s(s):
    try:
        with open(CF, "w") as f:
            json.dump(s, f, indent=4)
    except Exception as e:
        print(f"E: {e}")

class Calc:
    def __init__(self, m):
        self.m = m
        m.title("S C")
        
        self.s = load_s()
        self.ans = self.s['l']
        
        if self.s["t"] == "dark":
            self.bg = "#2c2c2c"
            self.fg = "white"
            self.bbg = "#454545"
            self.ebg = "#008800"
            self.cbg = "#aa0000"
        else:
            self.bg = "white"
            self.fg = "black"
            self.bbg = "lightgray"
            self.ebg = "lightgreen"
            self.cbg = "#ff8888"

        m.configure(bg=self.bg)
        
        for i in range(6):
            m.grid_columnconfigure(i, weight=1)
            m.grid_rowconfigure(i, weight=1)
            
        self._c_w()

    def _c_w(self):
        self.d = tk.Entry(self.m, font=("V", 22), 
                                bd=5, relief=tk.SUNKEN, 
                                justify=tk.RIGHT, 
                                bg="white", fg="black")

        self.d.grid(row=0, column=0, columnspan=6, 
                          sticky="nsew", padx=4, pady=4)
        
        b_map = [
            ("7", self.add, self.bbg), ("8", self.add, self.bbg), 
            ("9", self.add, self.bbg), ("sin", self.add, self.bbg), 
            ("cos", self.add, self.bbg), ("tan", self.add, self.bbg),
            
            ("4", self.add, self.bbg), ("5", self.add, self.bbg), 
            ("6", self.add, self.bbg), ("×", self.add, self.bbg), 
            ("÷", self.add, self.bbg), ("√", self.add, self.bbg),
            
            ("1", self.add, self.bbg), ("2", self.add, self.bbg), 
            ("3", self.add, self.bbg), ("^", self.add, self.bbg), 
            ("π", self.add, self.bbg), ("e", self.add, self.bbg),
            
            ("0", self.add, self.bbg), (".", self.add, self.bbg), 
            ("(", self.add, self.bbg), (")", self.add, self.bbg), 
            ("log", self.add, self.bbg), ("!", self.add, self.bbg)
        ]
        
        r, c = 1, 0
        for t, f, color in b_map:
            tk.Button(self.m, text=t, font=("V", 14), 
                      bg=color, fg=self.fg,
                      command=lambda t=t, f=f: f(t)
            ).grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
            
            c += 1
            if c > 5:
                c = 0
                r += 1
                
        tk.Button(self.m, text="C", font=("V", 14), bg=self.cbg, fg=self.fg,
                  command=self.clear_d).grid(row=5, column=0, sticky="nsew", padx=2, pady=2)
                  
        tk.Button(self.m, text="DEL", font=("V", 14), bg=self.cbg, fg=self.fg,
                  command=self.del_l).grid(row=5, column=1, sticky="nsew", padx=2, pady=2)
                  
        tk.Button(self.m, text="Ans", font=("V", 14), bg=self.bbg, fg=self.fg,
                  command=lambda: self.add("Ans")).grid(row=5, column=2, sticky="nsew", padx=2, pady=2)
                  
        tk.Button(self.m, text="+", font=("V", 14), bg=self.bbg, fg=self.fg,
                  command=lambda: self.add("+")).grid(row=5, column=3, sticky="nsew", padx=2, pady=2)
                  
        tk.Button(self.m, text="-", font=("V", 14), bg=self.bbg, fg=self.fg,
                  command=lambda: self.add("-")).grid(row=5, column=4, sticky="nsew", padx=2, pady=2)
                  
        tk.Button(self.m, text="=", font=("V", 14), bg=self.ebg, fg="white",
                  command=self.calc).grid(row=5, column=5, sticky="nsew", padx=2, pady=2)

    def add(self, t):
        self.d.insert(tk.END, t)

    def clear_d(self):
        self.d.delete(0, tk.END)

    def del_l(self):
        cur_t = self.d.get()
        if cur_t:
            self.d.delete(0, tk.END)
            self.d.insert(0, cur_t[:-1])

    def calc(self):
        exp = self.d.get()
        if not exp.strip():
            return
            
        exp = exp.replace("×","*").replace("÷","/")
        exp = exp.replace("^","**")
        exp = exp.replace("√","math.sqrt")
        exp = exp.replace("π","math.pi")
        exp = exp.replace("Ans", f"({self.ans})")
        
        def r_fact(m):
            return f"math.factorial({m.group(1)})"
            
        exp = re.sub(r"(\d+)\s*!", r_fact, exp)
        
        exp = re.sub(r'(sin|cos|tan|log)', r'math.\1', exp)

        try:
            res = eval(exp, {"__builtins__": None, "math": math}, {})
            
            if res == int(res):
                out = str(int(res))
            else:
                out = f"{res:.10g}"
                
            self.ans = res
            self.s['l'] = self.ans
            save_s(self.s)
            
            self.d.delete(0, tk.END)
            self.d.insert(0, out)
            
        except (NameError, TypeError, SyntaxError, ValueError):
            messagebox.showerror("E!", "IE. CI!")
            
        except Exception as e:
            messagebox.showerror("UE", f"SWW: {e}")


if __name__ == '__main__':
    w = tk.Tk()
    app = Calc(w)
    w.mainloop()
