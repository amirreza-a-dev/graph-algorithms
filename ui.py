import os

def clear():
    os.system("cls") if os.name=="nt" else os.system("clear")

def pause():
    input("Press Enter to continue...")
    clear()

def display(result):
    result.reverse()
    path=""
    path+=str(result[0])
    for i in range(1, len(result)):
        path+=f" --- {result[i]}"
    clear()
    return path

def ask_graph_reset():
    clear()
    while True:
        print("""
Do you want to define the graph from scratch? [y/n]
        """)
        choice=input(">> ")
        if choice.lower() in ("y", "n"):
            return choice.lower()
        else:
            wrong_input()

def get_vertices():
    while True:
        try:
            start = int(input("From: "))
            target = int(input("To: "))
            return start, target
        except ValueError:
            wrong_input()

def decide():
    while True:
        print("""
- Press Enter to continue
- Enter 'Q' to quit
        """)
        decision=input(">> ")
        clear()
        if decision=="" or decision.lower()=="q":
            return decision.lower()
        else:
            wrong_input()
def wrong_input():
    clear()
    print("Wrong input.\nTry again.")
    pause()
