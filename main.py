import ui, info
from bfs import bfs

def main():
    if not info.GRAPH.exists():
        ui.clear()
        info.initialize()
    else:
        choice = ui.ask_graph_reset()
        if choice=='y':
            ui.clear()
            info.initialize()
    vertices, edges = info.information()
    while True: 
            ui.clear()
            start, target = ui.get_vertices()
            if start not in vertices or target not in vertices:
                ui.wrong_input()
                decision=ui.decide()
                if decision=="q":
                    break
                else: continue
            result=bfs(vertices, edges, start, target)
            if isinstance(result, list):
                print(ui.display(result))
            else:
                ui.clear()
                print(result)
            decision=ui.decide()
            if decision=="q":
                break

if __name__=="__main__":
    main()