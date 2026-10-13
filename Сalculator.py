import os

def Calculator():
    print("Welcome!")
    os.system("clear || cls")
    print("\n")
    print("=" * 40)
    print("             Calculator_V1")
    print("=" * 40)
    input("\nPlease click the button enter!")

    os.system("clear || cls")

    print("=" * 40, "      Calculator_V1")

    a = float(input("a = ?: "))
    b = float(input("b = ?: "))
    
    print("=" * 40, "      Calculator_V1")

    print(f"a + b = {a + b}")
    print(f"a - b = {a - b}")
    print(f"a * b = {a * b}")
    
    if b == 0:
        print("0 / 0 == ERROR!") 

    else:
        print(f"a / b = {a / b}")

    print("=" * 40, "       Calculator_V1")

if __name__ == "__main__":
    Calculator()
