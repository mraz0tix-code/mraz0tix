import os
import platform
import tkinter as tk
import subprocess
os = platform.system()
 
print("Wow your os is:", os)
print(os, "this is good choice!")

answer = input("Do you want to run fastfetch? (y/n): ")
if answer in ("yes", "y"):
    subprocess.run("fastfetch")

answer = input("Do you want to run Telegram? (y/n): ")
if answer in ("yes", "y"):
 subprocess.run("Telegram")

print("bye bye!")
