#include<iostream>
#include<vector>
#include<stack>
using namespace std;

int neighborhood(int vertex, vector<vector<int>> edges, vector<bool> marked)
{
    for (vector i : edges)
    {
        if (i[0]==vertex)
        {
            if (!(marked[static_cast<size_t>(i[1])]))
            {
                return i[1];
            }
        }
        if (i[1]==vertex)
        {
            if (!(marked[static_cast<size_t>(i[0])]))
            {
                return i[0];
            }
        }
    }
    return -1;
}

vector<int> dfs(vector<int> vertices, vector<vector<int>> edges, int root)
{
    stack<int> s;
    vector<bool> marked(vertices.size(), false);
    vector<int> result;
    int current;
    int neighbor;

    marked[static_cast<size_t>(root)]=true;
    s.push(root);
    result.push_back(root);

    while (!s.empty())
    {
        current=s.top();
        neighbor=neighborhood(current, edges, marked);
        if (neighbor!=-1)
        {
            marked[static_cast<size_t>(neighbor)]=true;
            s.push(neighbor);
            result.push_back(neighbor);
        }
        else
        {
            s.pop();
        }

    } 
    return result;
}