#include<iostream>
#include<vector>
#include<stack>
#include<sstream>

using namespace std;

vector<vector<int>> get_adj(const vector<int>& vertices, const vector<vector<int>>& edges)
{
    int vertices_size=static_cast<int>(vertices.size());
    vector<vector<int>> adjacents(static_cast<size_t>(vertices_size));
    for (const auto& i: edges)
    {
        adjacents[static_cast<size_t>(i[0])].push_back(i[1]);
        if (i[2]==1)
            adjacents[static_cast<size_t>(i[1])].push_back(i[0]);
    }
    return adjacents;
}

vector<int> dfs(const vector<int>& vertices, const vector<vector<int>>& edges, int root)
{
    stack<int> s;
    vector<bool> marked(vertices.size(), false);
    vector<int> result;
    int current;
    bool adj_flag;
    vector<vector<int>> adjacents=get_adj(vertices, edges);
    
    marked[static_cast<size_t>(root)]=true;
    s.push(root);
    result.push_back(root);

    while (!s.empty())
    {
        adj_flag=false;
        current=s.top();
        for (int i: adjacents[static_cast<size_t>(current)])
        {
            if (!marked[static_cast<size_t>(i)])
            {
                marked[static_cast<size_t>(i)]=true;
                s.push(i);
                result.push_back(i);
                adj_flag=true;
                break;
            }
        }
        if (!adj_flag)
        {
            s.pop();
        }
    } 
    return result;
}

int main(int argc, char* argv[])
{
    if (argc<4)
    {
        cerr<<"Missing parameters\n";
        return 1;
    }

    string v=argv[1], e=argv[2], r=argv[3];
    vector<int> vertices;
    vector<vector<int>> edges;
    int root= stoi(r);

    istringstream s1(v);
    istringstream s2(e);

    int n,m,k;

    while (s1>>n)
        vertices.push_back(n);
    
    while (s2>>n>>m>>k)
        edges.push_back({n, m, k});

    vector<int> result = dfs(vertices, edges, root);
    for (auto i:result)
        cout<<i<<" ";

    return 0;
}