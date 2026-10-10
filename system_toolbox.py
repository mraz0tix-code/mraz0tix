#!/usr/bin/env python
import subprocess
import os
import webbrowser
import math
import shutil

def get_disk_progress_bar(path="/"):
    total, used, free = shutil.disk_usage(path)
    total_gb = total / (1024 ** 3)
    used_gb = used / (1024 ** 3)
    free_gb = free / (1024 ** 3)
    percent = (used / total) * 100
    
    bar_length = 20
    filled_length = int(round((bar_length * percent) / 100))
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    
    return f"[{path}]: {bar} {percent:.1f}% [Free: {free_gb:.1f} GB of {total_gb:.1f} GB]"

print("1. Toolbox (by mraz0tix)")
print("2. Open my site (mraz0tix-code.github.io)")
print("3. Exit the program")
main_choice = input("Select a menu option (1-4): ")

if main_choice == "1":
    os.system("clear || cls")
    
    print("=" * 40)
    print("          Toolbox by mraz0tix!")
    print("=" * 40)
    print("1. Check Internet Connection (Ping Google)")
    print("2. Show System Information (Uname)")
    print("3. Show Active Network Ports (ss)")
    print("4. Run Fastfetch")
    print("5. Disk Info")
    print("6. Exit")
    print("=" * 40)

    sub_choice = input("Select a menu option (1-6): ")

    if sub_choice == "1":
        print("\nChecking connection...")
        subprocess.run(["ping", "-c", "3", "8.8.8.8"])
        input("\nPress Enter to continue...")

    elif sub_choice == "2":
        print("\nKernel Information:")
        subprocess.run(["uname", "-a"])
        input("\nPress Enter to continue...")

    elif sub_choice == "3":
        print("\nListening ports in the system:")
        subprocess.run(["ss", "-tuln"])
        input("\nPress Enter to continue...")

    elif sub_choice == "4":
        try:
            subprocess.run(["fastfetch"])
        except FileNotFoundError:
            print("\nError: 'fastfetch' is not installed on your system.")
        input("\nPress Enter to continue...")
    
    elif sub_choice == "5":
        print("\n=== DISK STORAGE ANALYSIS ===")
        print(get_disk_progress_bar("/"))
        input("\nPress Enter to continue...")

    elif sub_choice == "6":
        print("bye bye!")

    else:
        print("\nInvalid choice. Please try again.")
        input("\nPress Enter to continue...")

elif main_choice == "2":
    webbrowser.open("https://mraz0tix-code.github.io/")
    input("\nPress Enter to continue...")

elif main_choice == "3":
    print("\nOkay! Goodbye!")

else:
    print("\nInvalid choice. Please try again.")
    input("\nPress Enter to continue...")
