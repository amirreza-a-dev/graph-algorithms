import ui, info
from bfs import bfs
from dfs import dfs

def main():
    if not info.GRAPH.exists():
        ui.clear()
        info.initialize()
    else:
        choice = ui.ask_graph_reset()
        if choice=='y':
            ui.clear()
            info.initialize()
            ui.clear()
        vertices, edges = info.information()
        while True:
            algorithm = ui.get_algorithms()
            if algorithm=='1':
            
                start, target = ui.get_vertices_bfs()
                result = bfs(vertices, edges, start, target)
                if isinstance(result, list):
                    print(ui.display(result))
                else:
                    print(result)
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue
            else:
            
                root = ui.get_root_dfs()
                result = dfs(vertices, edges, root)
                print(result)
                decision = ui.decide()
                if decision=='q':
                    break
                else:
                    continue

if __name__=="__main__":
    main()