from tkinter import *

window = Tk()
window.title("Unit Converter")
#window.iconbitmap("C:\Users\kisho\Downloads")

e = Entry(width=40,borderwidth=5)

def ButtonClear():
    e.delete(0,END)

def kg_to_g():
    kg = float(kg_entry.get())
    grams = kg * 1000
    result_label_kg.config(text=f"{kg} kg = {grams} g")

def km_to_m():
    km = float(km_entry.get())
    meters = km * 1000
    result_label_km.config(text=f"{km} km = {meters} m")


frame_kg = Tk.Frame(window, padding="10").grid(row=0, column=0, padx=10, pady=10)

kg_label = Tk.Label(frame_kg, text="Kilograms:").grid(row=0, column=0, padx=5, pady=5)

kg_entry = Entry(width=40,borderwidth=5).grid(row=0, column=1, padx=5, pady=5)

convert_button_kg = Tk.Button(frame_kg, text="Convert to Grams", command=kg_to_g).grid(row=1, column=0, columnspan=2, pady=5)

result_label_kg = Tk.Label(frame_kg, text="").grid(row=2, column=0, columnspan=2, pady=5)

frame_km = Tk.Frame(window, padding="10").grid(row=1, column=0, padx=10, pady=10)

km_label = Tk.Label(frame_km, text="Kilometers:").grid(row=0, column=0, padx=5, pady=5)

km_entry = Entry(width=40,borderwidth=5).grid(row=0, column=1, padx=5, pady=5)

convert_button_km = Tk.Button(frame_km, text="Convert to Meters", command=km_to_m).grid(row=1, column=0, columnspan=2, pady=5)
buttonclear = Button(text="Clear",padx=77,pady=20,command=ButtonClear).grid(row=6,column=1,columnspan=2)

result_label_km = Tk.Label(frame_km, text="").grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
