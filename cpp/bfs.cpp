#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>

using namespace std;

vector<int> neighborhood(int vertex, const vector<vector<int>>& edges, const vector<bool>& marked)
{
    vector<int> neighbors;
    for (const vector<int>& i : edges)
    {
        if (i[0]==vertex)
        {
            if (!(marked[static_cast<size_t>(i[1])]))
            {
                neighbors.push_back(i[1]);
            }
        }
        if (i[1]==vertex)
        {
            if (!(marked[static_cast<size_t>(i[0])]))
            {
                neighbors.push_back(i[0]);
            }
        }
    }
    return neighbors;
}


vector<int> bfs(const vector<int>& vertices, const vector<vector<int>>& edges, int start, int target)
{
    queue<int> q;
    vector<int> parent(vertices.size(), -1);
    vector<bool> marked(vertices.size(), false);
    vector<int> result;
    vector<int> no_path_message{-1};

    if (start==target)
    {
        vector<int> s;
        s.push_back(start);
        return s;
    }
    marked[static_cast<size_t>(start)]=true;
    q.push(start);

    while(!q.empty())
    {
        int current=q.front();
        vector<int> neighbors=neighborhood(current, edges, marked);
        for (int i: neighbors)
        {
            parent[static_cast<size_t>(i)]=current;
            marked[static_cast<size_t>(i)]=true;
            if (i==target)
            {
                int subject=i;
                while(subject!=-1)
                {
                    result.push_back(subject);
                    subject=parent[static_cast<size_t>(subject)];
                }
                reverse(result.begin(), result.end());
                return result;
            }
            q.push(i);
        }
        q.pop();
    }
    return no_path_message;
}