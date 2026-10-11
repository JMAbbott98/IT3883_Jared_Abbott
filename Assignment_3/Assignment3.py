# Program Name: Assignment3.py (use the name the program is saved as)
# Course: IT3883/Section W01
# Student Name: Jared Abbott
# Assignment Number: Lab 3
# Due Date: 10/10/ 2026
# Purpose: It converts Miles per Gallon to Kilometers per Liter
# List: My mom
#Tutoring: Will Causey, Shaokun Weng, Deeric Burns,Dean Kwando Obeng Asante, Sawyer Strickland, Hentry Middlebrooks, and Luke Craven
#https://docs.python.org/3/library/tkinter.html
#https://www.geeksforgeeks.org/python/python-setting-and-retrieving-values-of-tkinter-variable/
#https://www.geeksforgeeks.org/python/python-grid-method-in-tkinter/
#https://www.geeksforgeeks.org/python/python-gui-tkinter/
#The four GUI coding examples
#https://www.geeksforgeeks.org/python/python-tkinter-entry-widget/
#https://www.geeksforgeeks.org/python/tracing-tkinter-variables-in-python/
#https://www.geeksforgeeks.org/python/python-tkinter-label/
#https://www.w3schools.com/python/ref_string_isdigit.asp
#https://www.w3schools.com/python/python_args_kwargs.asp
#https://docs.python.org/3/library/configparser.html
#https://www.geeksforgeeks.org/python/how-to-write-a-configuration-file-in-python/
#https://www.youtube.com/watch?v=D7VE_X_hZqw&t=87s
#https://www.youtube.com/watch?v=qjbj_pKsreE&t=179s
#https://www.youtube.com/watch?v=eyAOyAkbIdY&t=2s
#https://www.youtube.com/watch?v=jtM9RLAENVE
#https://www.youtube.com/watch?v=QF3HAzGp7FM
#https://www.youtube.com/watch?v=5RkkEGa-GG8&t=899s
import tkinter as tk
from tkinter import *
# Miles per Gallon = MPG or mpg
# Kilometers per Liter = KPL or kpl
def kilo(*args):
   kpl = 0.425143707
   mpg = 1.0
   # Retrieve entries from the entry fields
   mpg_text = mpgtextentry.get()
   kpl_text = kpltextentry.get()
   # Check to see if numbers are put into the code
   if mpg_text.isdigit() and kpl_text.isdigit():
        mpg = float(mpg_text)
        kpl = float(kpl_text)
        kplconverion = mpg * kpl
        # Update the rest of the program a.k.a update the pop-up window
        label_result.config(text=f"Result: {kplconverion:.2f} Gallons")
# The purpose of the function was to convert strings to floats.
def final_conversion():
    mpgtextconv = float(mpgtextentry.get())
    kplconversion1 = mpgtextconv * 0.425143707
    return kplconversion1
#this code is meant to take inputs and outputs. Plus, set the title and size of the pop-up window
conversion = tk.Tk()
conversion.title("Miles per Gallon to Kilometers per Liter Converter")
conversion.geometry("400x400")
conversion_var = tk.StringVar()
conversion_var.trace_add("write", kilo)
kpl=tk.StringVar()
#--------------------------------------------------------

#This code was meant to display outputs in the code and set how the textboxes and words were look in the pop-up window
#Moreover, display the main pop-up window
mpgLabel = tk.Label(conversion, text = "MPG")
kplLabel = tk.Label(conversion, text = "KPL")
mpgtextentry = tk.Entry(conversion, textvariable = conversion_var)
mpgtextentry.get()
mpgtextentry.grid(row = 1, column = 2, padx=10)
kpltextentry = tk.Entry(conversion, textvariable=conversion_var)
kpltextentry.get()
kpltextentry.grid(row=1, column=1, padx=10, pady=10)
label_result = tk.Label(conversion)
conversion.mainloop()









