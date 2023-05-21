#include <iostream>
#include <vector>
#include <queue>
#include <cmath>

using namespace std;

vector<int> parent;
vector<int> r;

struct Node {
    int id, x, y;
};

struct Edge {
    int cost, node1, node2;
};

struct CompareEdges {
    bool operator()(const Edge& e1, const Edge& e2) {
        return e1.cost > e2.cost; // Min-heap based on cost
    }
};


int getParent(int x) {
    if (parent[x] == x)
        return x;
    parent[x] = getParent(parent[x]);
    return parent[x];
}

void unionNodes(int x, int y) {
    x = getParent(x);
    y = getParent(y);

    if (x == y)
        return;

    if (r[x] < r[y])
        parent[x] = y;
    else {
        parent[y] = x;
        if (r[x] == r[y])
            r[x]++;
    }
}

int main() {
    int n, c;
    cin >> n >> c;

    vector<Node> nodes(n);
    vector<Edge> edges;

    for (int i = 0; i < n; i++) {
        cin >> nodes[i].x >> nodes[i].y;
        nodes[i].id = i;
    }

    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            int x1 = nodes[i].x;
            int y1 = nodes[i].y;
            int x2 = nodes[j].x;
            int y2 = nodes[j].y;
            int cost = pow(x1 - x2, 2) + pow(y1 - y2, 2);
            if (cost >= c) {
                edges.push_back({ cost, i, j });
            }
        }
    }

    parent.resize(n);
    r.resize(n, 0);
    for (int i = 0; i < n; i++)
        parent[i] = i;

    int minCost = 0;
    int edgeCnt = 0;
    priority_queue<Edge, vector<Edge>, CompareEdges> minHeap;

    for (const auto& edge : edges)
        minHeap.push(edge);

    while (!minHeap.empty()) {
        Edge currentEdge = minHeap.top();
        minHeap.pop();

        int cost = currentEdge.cost;
        int n1 = currentEdge.node1;
        int n2 = currentEdge.node2;

        if (getParent(n1) != getParent(n2)) {
            unionNodes(n1, n2);
            minCost += cost;
            edgeCnt++;
        }
    }

    if (edgeCnt == n - 1)
        cout << minCost << endl;
    else
        cout << -1 << endl;

    return 0;
}