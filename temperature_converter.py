import tkinter as tk
from tkinter import ttk


def convert_celsius_to_fahrenheit(*args):
    try:
        celsius_value = float(celsius.get())
        fahrenheit_value = celsius_value * 1.8 + 32
        fahrenheit.set(f'{fahrenheit_value:.3f}')
    except ValueError:
        pass


root = tk.Tk()
root.title('Temperature converter')
root.resizable(False, False)

frame = ttk.Frame(root, padding=(20, 10))
frame.grid()

celsius_label = ttk.Label(frame, text='Celsius:')
celsius_label.grid(row=0, column=0, sticky='W', padx=5, pady=5)

fahrenheit_label = ttk.Label(frame, text='Fahrenheit:')
fahrenheit_label.grid(row=1, column=0, sticky='W', padx=5, pady=5)

celsius = tk.StringVar()
celsius_entry = ttk.Entry(frame, width=10, textvariable=celsius)
celsius_entry.grid(row=0, column=1, sticky='EW', padx=5, pady=5)
celsius_entry.focus()

fahrenheit = tk.StringVar(value='Temperature in fahrenheits')
fahrenheit_output = ttk.Label(frame, textvariable=fahrenheit)
fahrenheit_output.grid(row=1, column=1, sticky='EW', padx=5, pady=5)

calculate_button = ttk.Button(frame, text='Convert', command=convert_celsius_to_fahrenheit)
calculate_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=5, pady=5)

root.bind("<Return>", convert_celsius_to_fahrenheit)

root.mainloop()
