import tkinter as tk
from tkinter import colorchooser
import analiz

color = ""  # Variable to store the selected color

def show_color_picker():
    global color
    color = colorchooser.askcolor(title="Выберите цвет")
    if color[1]:
        print("Выбранный цвет:", color[1])

def run():
    pos_list = []
    if noun_var.get():  # If Noun checkbox is selected
        pos_list.append('NOUN')
    if verb_var.get():  # If Verb checkbox is selected
        pos_list.append('VERB')
    
    analiz.TextAnalyser(
        file_name='text.txt',
        pos_list=pos_list,
        chislo=int(entry.get()),
        background=color[1],
        width=int(entry2.get()),
        height=int(entry3.get())
    )

window = tk.Tk()
label = tk.Label(window, text="Анализатор текста", font=("Impact", 19), background="#c7730c")
noun_var = tk.BooleanVar()  # Variable to store the state of Noun checkbox
verb_var = tk.BooleanVar()  # Variable to store the state of Verb checkbox
cb_noun = tk.Checkbutton(window, text="Включить Noun", font=("Impact", 19), variable=noun_var)
cb_verb = tk.Checkbutton(window, text="Включить Verb", font=("Impact", 19), variable=verb_var)
label2 = tk.Label(window, text="Ширина:", font=("Impact", 19))
label3 = tk.Label(window, text="Высота:", font=("Impact", 19))
button = tk.Button(window, font=("Impact", 17), background="#DAA520", text="сделать вордклауд", command=run)
button2 = tk.Button(window, font=("Impact", 17), background="#59c977", text="выбрать цвет", command=show_color_picker)
entry = tk.Entry(window, font=("Impact", 18))
entry2 = tk.Entry(window, font=("Impact", 18))
entry3 = tk.Entry(window, font=("Impact", 18))

label.pack(anchor="nw", padx=6, pady=6)
entry.pack(anchor="nw", padx=6, pady=6)
button.pack(anchor="nw", padx=6, pady=6)
button2.pack(anchor="nw", padx=6, pady=6)
label2.pack(anchor="nw", padx=6, pady=6)
entry2.pack(anchor="nw", padx=6, pady=6)
label3.pack(anchor="nw", padx=6, pady=6)
entry3.pack(anchor="nw", padx=6, pady=6)
cb_noun.pack(anchor="nw", padx=6, pady=6)  # Display Noun checkbox
cb_verb.pack(anchor="nw", padx=6, pady=6)  # Display Verb checkbox

window.mainloop()

