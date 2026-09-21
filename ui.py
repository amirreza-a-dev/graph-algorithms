import os

def clear():
    os.system("cls") if os.name=="nt" else os.system("clear")

def pause():
    input("Press Enter to continue...")
    clear()

def display_bfs(result):
    if result==["-1"]:
        return "No path was found."
    path=""
    path+=result[0]
    for i in range(1, len(result)):
        path+=f" --- {result[i]}"
    clear()
    return path

def display_dfs(result):
    path=""
    path+=result[0]
    for i in range(1, len(result)):
        path+=f", {result[i]}"
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
            start = input("From: ")
            target = input("To: ")
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
        if decision.lower() in ("", "q"):
            clear()
            return decision.lower()
        else:
            wrong_input()
def wrong_input():
    clear()
    print("Wrong input.\nTry again.")
    pause()

def get_algorithms_menu():
    while True:
        print("""
--< Main Menu >--
1. BFS Algorithm
2. DFS Algorithm
3. Exit Program
-----------------
            """)
        choice=input(">> ")
        if choice in ('1', '2', '3'):
            clear()
            return choice
        else:
            wrong_input()

def get_root_dfs():
    while True:
        try:
            root = input("Specify the root vertex: ")
            clear()
            return root
        except ValueError:
            wrong_input()

def broken_graph():
    print("The graph file contains invalid data.\n")
    dec=decide()
    return dec