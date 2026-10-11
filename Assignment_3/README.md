# Program Name: Assignment3.py (use the name the program is saved as)
# Course: IT3883/Section W01
# Student Name: Jared Abbott
# Assignment Number: Lab 3
# Due Date: 10/10/ 2026
# Purpose: It converts Miles per Gallon to Kilometers per Liter
# List: My mom
#Tutoring: Will Causey, Shaokun Weng, Deeric Burns,Dean Kwando Obeng Asante, Sawyer Strickland, Hentry Middlebrooks, and Luke Craven
#The four GUI coding examples
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
<img width="1920" height="1080" alt="PycharmAssignment3OutputScreenshot" src="https://github.com/user-attachments/assets/01cb7b52-a483-40f6-a608-69ab24b28a31" />











