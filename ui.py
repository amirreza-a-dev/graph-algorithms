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
            clear()
            return choice.lower()
        else:
            wrong_input()

def get_vertices_bfs():
    while True:
        try:
            start = int(input("From: "))
            target = int(input("To: "))
            clear()
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
            clear()
            return decision.lower()
        else:
            wrong_input()
def wrong_input():
    clear()
    print("Wrong input.\nTry again.")
    pause()

def get_algorithms():
    while True:
        print("""
Choose one of these algorithms:
1. BFS
2. DFS
            """)
        choice=input(">> ")
        if choice in ('1', '2'):
            clear()
            return choice
        else:
            wrong_input()

def get_root_dfs():
    while True:
        try:
            root = int(input("Specify the root vertex: "))
            clear()
            return root
        except ValueError:
            wrong_input()