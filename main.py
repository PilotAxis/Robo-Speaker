import os
if __name__ == "__main__":
    name = input("What is your name? ")
    print("Welcome to the Robo Speaker", name, "!")
    while True:
        print("What would you like me to say?")
        print("Enter 'q' to quit.")
        x = input()
        if x == 'q':
            print("Bye!")
            break
        command = f"say {x}"
        os.system(command)