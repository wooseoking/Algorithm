import java.util.*;

public class Main {
    public static final int INF = Integer.MAX_VALUE >> 1;
    public static class Edge{
        int num;
        int cost;

        public Edge(int num,int cost){
            this.num = num;
            this.cost = cost;
        }
    }
    public static int[] dijikstra(int n , int start,List<List<Edge>> graph){
        int[] d = new int[n+1];
        for(int i = 0 ;i<n+1;i++){
            d[i] = INF;
        }
        PriorityQueue<Edge> pq = new PriorityQueue<>(((o1, o2) -> Integer.compare(o1.cost,o2.cost)));
        pq.add(new Edge(start,0));
        d[start] = 0;
        while(!pq.isEmpty()){
            Edge cur = pq.poll();
            int curNode = cur.num;
            int curCost = cur.cost;

            if(d[curNode] < curCost)continue;


            for(Edge nextEdge : graph.get(curNode)){
                int nextCost = curCost + nextEdge.cost;
                int nextNode = nextEdge.num;
                if(nextCost < d[nextNode]){
                    d[nextNode] = nextCost;
                    pq.add(new Edge(nextNode,nextCost));
                }
            }
        }
        return d;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n,e;
        n = sc.nextInt();
        e = sc.nextInt();
        int start = sc.nextInt();

        List<List<Edge>> graph = new ArrayList<>();
        for(int i = 0 ;i<n+1;i++){
            graph.add(new ArrayList<>());
        }

        for(int i = 0 ;i<e;i++){
            int u,v,c;
            u = sc.nextInt();
            v = sc.nextInt();
            c = sc.nextInt();

            graph.get(u).add(new Edge(v,c));
        }

        int[] d = dijikstra(n,start,graph);
        for(int i = 1 ; i < n+ 1 ;i++){
            int cost = d[i];
            if(cost == INF) System.out.println("INF");
            else System.out.println(cost);
        }
    }
}