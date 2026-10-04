import subprocess
import os
import webbrowser

print("1. Toolbox(by mraz0tix)")
print("2. Open my site(mraz0tix-code.github.io/ ) ")
print("3. Exit the program")
choise = input("Select a menu option (1-5): ")

if choise in ("1"):
    os.system("clear || cls")
    
    print("=" * 40)
    print("          Toolbox by mraz0tix!")
    print("=" * 40)

    print("1. Check Internet Connection (Ping Google)")
    print("2. Show System Information (Uname)")
    print("3. Show Active Network Ports (ss)")
    print("4. Run Fastfetch")
    print("5. Exit")
    print("=" * 40)

    choice = input("Select a menu option (1-5): ")

    if choice == "1":
        print("\nChecking connection...")
        subprocess.run(["ping", "-c", "3", "8.8.8.8"])
        input("\nPress Enter to continue...")

    elif choice == "2":
        print("\nKernel Information:")
        subprocess.run(["uname", "-a"])
        input("\nPress Enter to continue...")

    elif choice == "3":
        print("\nListening ports in the system:")
        subprocess.run(["ss", "-tuln"])
        input("\nPress Enter to continue...")

    elif choice == "4":
        try:
            subprocess.run(["fastfetch"])
        except FileNotFoundError:
            print("\nError: 'fastfetch' is not installed on your system.")
        input("\nPress Enter to continue...")

    elif choise == "5":
            print("bye bye!")

    else:
        print("\nInvalid choice. Please try again.")
        input("\nPress Enter to continue...")

elif choise in ("2"):
 webbrowser.open("https://mraz0tix-code.github.io/")
 input("\nPress Enter to continue...")

elif choise in "3":
    print("\nOkay! Goodbye!")

else:
    print("\nInvalid choice. Please try again.")
    input("\nPress Enter to continue...")
