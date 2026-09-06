import platform
import tkinter as tk
os = platform.system()
print('Hello user!')
print('Python:', f"You use OS: {os}")
print("Python:", "God choise!")
import subprocess
answer = input("Would you like to open a program or execute a command? (yes/y/no/n): ")
if answer in ("yes", "y"):
  command = input("Enter command: ")
  subprocess.run(command, shell=True )

if answer in ("no", "n"):
 print("Okay")


answer = input("Do you want to run fastfetch? (yes/y/no/n): ")
if answer in ("yes", "y"):
 window = tk.Tk()
 result = subprocess.run(["fastfetch"], capture_output=True, text=True)
 label = tk.Label(window, text=result.stdout, font=("monospace", 10), bg="#0d1117", fg="#58a6ff", justify="left", anchor="nw")
 label.pack(fill="both", expand=True)
 window.mainloop()

if answer in ("no", "n"):
 print("Okay!")

answer = input("You like this project? yes/y/no/n:")
if answer in ("yes", "y"):
 print("Thank you so much!")

if answer in ("no", "n"):
 print ("I'm sorry")