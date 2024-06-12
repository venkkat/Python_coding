from tkinter import *

window = Tk()
window.title("Unit Converter")

def kg_to_g():
    kg = float(kg_entry.get())
    grams = kg * 1000
    result_label_kg.config(text=f"{kg} kg = {grams} g")

def km_to_m():
    km = float(km_entry.get())
    meters = km * 1000
    result_label_km.config(text=f"{km} km = {meters} m")

def ButtonClear():
    kg_entry.delete(0,END)
    km_entry.delete(0,END)


frame_kg = Frame(window, padding="5").grid(row=0, column=0, padx=10, pady=10)

kg_label = Label(frame_kg, text="Kilograms:").grid(row=0, column=0, padx=5, pady=5)

kg_entry = Entry(width=35,borderwidth=5).grid(row=0, column=1, padx=5, pady=5)

convert_button_kg = Button(frame_kg, text="Convert to Grams", command=kg_to_g).grid(row=1, column=0, columnspan=2, pady=5)

result_label_kg = Label(frame_kg, text="").grid(row=2, column=0, columnspan=2, pady=5)

frame_km = Frame(window, padding="5").grid(row=1, column=0, padx=10, pady=10)

km_label = Label(frame_km, text="Kilometers:").grid(row=0, column=0, padx=5, pady=5)

km_entry = Entry(width=35,borderwidth=5).grid(row=0, column=1, padx=5, pady=5)

convert_button_km = Button(frame_km, text="Convert to Meters", command=km_to_m).grid(row=1, column=0, columnspan=2, pady=5)
buttonclear = Button(text="Clear",padx=77,pady=20,command=ButtonClear)
buttonclear.grid(row=4,column=1,columnspan=2)


result_label_km = Label(frame_km, text="").grid(row=2, column=0, columnspan=2, pady=5)

window.mainloop()
