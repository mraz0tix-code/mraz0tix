import subprocess

while True:
    print("\n" + "=" * 40)
    print("          Toolbox by mraz0tix!")
    print("=" * 40)

    print("1. Check internet connection (Ping Google)")
    print("2. Show system information (Uname)")
    print("3. Show active network ports (ss)")
    print("4. Exit program")
    print("=" * 40)

    choice = input("Choose a menu option (1-4): ").strip()

    if choice == "1":
        print("\nChecking connection...")
        subprocess.run(["ping", "-c", "3", "8.8.8.8"])

    elif choice == "2":
        print("\nKernel information:")
        subprocess.run(["uname", "-a"])

    elif choice == "3":
        print("\nListening ports in the system:")
        subprocess.run(["ss", "-tuln"])

    elif choice == "4":
        print("\nThank you for using Toolbox! Goodbye!")
        break

    else:
        print("\nInvalid input. Please try again.")
