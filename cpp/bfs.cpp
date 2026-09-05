#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

vector<vector<int>> get_adj(const vector<int>& vertices, const vector<vector<int>>& edges)
{
    int vertices_size=static_cast<int>(vertices.size());
    vector<vector<int>> adjacents(static_cast<size_t>(vertices_size));
    for (const vector<int>& i: edges)
    {
        adjacents[static_cast<size_t>(i[0])].push_back(i[1]);
        adjacents[static_cast<size_t>(i[1])].push_back(i[0]);
    }
    return adjacents;
}


vector<int> bfs(const vector<int>& vertices, const vector<vector<int>>& edges, int start, int target)
{
    if (start==target)
    {
        return {start};
    }
    queue<int> q;
    vector<int> parent(vertices.size(), -1);
    vector<bool> marked(vertices.size(), false);
    vector<int> result;
    vector<int> no_path_message{-1};
    int current;
    vector<vector<int>> adjacents=get_adj(vertices, edges);

    marked[static_cast<size_t>(start)]=true;
    q.push(start);

    while (!q.empty())
    {
        current=q.front();
        for (int i: adjacents[static_cast<size_t>(current)])
        {
            if (!marked[static_cast<size_t>(i)])
            {
                marked[static_cast<size_t>(i)]=true;
                parent[static_cast<size_t>(i)]=current;
                q.push(i);
                if (i==target)
                {
                    result.push_back(i);
                    while(current!=-1)
                    {
                        result.push_back(current);
                        current=parent[static_cast<size_t>(current)];
                    }
                    reverse(result.begin(), result.end());
                    return result;
                }
            }
        }
        q.pop();
    }
    return no_path_message;
}