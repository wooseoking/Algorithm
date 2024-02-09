#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int n, m;
vector<vector<int>> g, rg;
vector<bool> visited;
vector<int> finished, sccgroupNum;
vector<vector<int>> SCC;

void dfs(int cur) {
    visited[cur] = true;
    for (int nextNode : g[cur]) {
        if (!visited[nextNode]) dfs(nextNode);
    }
    finished.push_back(cur);
}

void rdfs(int cur, vector<int>& scc, int groupNum) {
    sccgroupNum[cur] = groupNum;
    scc.push_back(cur);
    visited[cur] = true;
    for (int nextNode : rg[cur]) {
        if (!visited[nextNode]) rdfs(nextNode, scc, groupNum);
    }
}

int main() {
    cin >> n >> m;
    g.resize(n);
    rg.resize(n);
    visited.assign(n, false);
    sccgroupNum.assign(n, 0);

    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        g[x].push_back(y);
        rg[y].push_back(x);
    }

    for (int i = 0; i < n; i++) {
        if (!visited[i]) dfs(i);
    }

    visited.assign(n, false);
    int groupNum = 0;

    while (!finished.empty()) {
        int top = finished.back();
        finished.pop_back();
        if (visited[top]) continue;
        vector<int> scc;
        rdfs(top, scc, groupNum++);
        SCC.push_back(scc);
    }

    vector<int> sccIndegree(SCC.size(), 0);
    for (int i = 0; i < n; i++) {
        for (int nextNode : g[i]) {
            if (sccgroupNum[i] != sccgroupNum[nextNode]) {
                int gNum = sccgroupNum[nextNode];
                sccIndegree[gNum]++;
            }
        }
    }

    int ans = 0;
    for (int i : sccIndegree) {
        if (i == 0) ans++;
    }
    cout << ans << endl;

    return 0;
}
