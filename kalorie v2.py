import tkinter as tk
master = tk.Tk()

def show_entry_fields():
    print((name.get(), weight.get(), height.get(), age.get(), rb_sex.get(), opt_activ.get()))
    l_weight = tk.Label(master, text = float(weight)**10.0)
    l_height = tk.Label(master, text = float(height)**6.25)
    l_age = tk.Label(master, text = float(height)**5.0)

""" this line need some changes
ppm = l_weight + l_height -  age + rb.sex
print("Dzienne zapotrzebowanie kaloryczne wynosi:", ppm * opt_activ, "kcal")
"""

tk.Label(master, text="Podaj swoje imię").grid(row=0)
tk.Label(master, text="Podaj swój wzrost").grid(row=1)
tk.Label(master, text="Podaj swoją wagę").grid(row=2)
tk.Label(master, text="Podaj ile masz lat").grid(row=3)

name = tk.Entry (master)
height = tk.Entry(master)
weight = tk.Entry(master)
age = tk.Entry(master)

name.grid(row=0, column=1)
height.grid(row=1, column=1)
weight.grid(row=2, column=1)
age.grid(row=3, column=1)

rb_sex = tk.StringVar()
rb_female = tk.Radiobutton(master, variable = rb_sex, value = -161, text = "kobieta")
rb_male = tk.Radiobutton(master, variable = rb_sex, value = +5, text = "mężczyzna")
rb_sex.set("k")
rb_female.grid()
rb_male.grid()


opt_activ = tk.StringVar()
opt1 = tk.Radiobutton(master, variable = opt_activ, value = 1.2, text = "Praca siedząca, brak dodatkowej aktywności fizycznej")
opt2 = tk.Radiobutton(master, variable = opt_activ, value = 1.4, text = "Praca niefizyczna, mało aktywny tryb życia")
opt3 = tk.Radiobutton(master, variable = opt_activ, value = 1.6, text = "Lekka praca fizyczna, regularne ćwiczenia 3-4 razy print(ok. 5h) w tygodniu")
opt4 = tk.Radiobutton(master, variable = opt_activ, value = 1.8, text = "Praca fizyczna, regularne ćwiczenia od 5razy (ok. 7h) w tygodniu")
opt5 = tk.Radiobutton(master, variable = opt_activ, value = 2.0, text = "Praca fizyczna ciężka, regularne ćwiczenia 7 razy w tygodniu ")

opt_activ.set("opt1")
opt1.grid()
opt2.grid()
opt3.grid()
opt4.grid()
opt5.grid()

tk.Button(master, text="Wyjście",command=master.quit).grid(row=15, column=0, pady=4)
tk.Button(master, text="Oblicz", command=show_entry_fields).grid(row=15, column=1, pady=4)

tk.mainloop()
