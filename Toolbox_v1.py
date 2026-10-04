import subprocess
import os

while True:
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

    elif choice == "5":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")
        input("\nPress Enter to continue...")
