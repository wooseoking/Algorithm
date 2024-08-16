import java.util.*;

public class Main {

    static int n,m;
    static Scanner sc = new Scanner(System.in);
    static List<Edge> edges = new ArrayList<>();
    static int[] parent;
    static int[] rank;

    public static class Edge implements Comparable<Edge>{
        int x;
        int y;
        int cost;

        public Edge(int x, int y,int cost){
            this.y =y;
            this.x = x;
            this.cost = cost;
        }
        @Override
        public int compareTo(Edge other){
            return this.cost - other.cost;
        }
    }

    public static int getParent(int x){
        if(x == parent[x]) return x;
        return parent[x] = getParent(parent[x]);
    }

    public static void union(int x,int y){
        x = getParent(x);
        y = getParent(y);

        if(x == y)return;

        if(rank[x] < rank[y]){
            parent[x] = y;
        }else{
            parent[y] = x;
            if(rank[x] == rank[y]){
                rank[x]++;
            }
        }
    }
    public static void main(String[] args) {
        n = sc.nextInt();
        m = sc.nextInt();
        parent = new int[n + 1];
        rank = new int[n + 1];

        for(int i = 0 ;i<n+1;i++){
            parent[i] = i;
        }
        for(int i = 0 ;i<m;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            int c = sc.nextInt();
            edges.add(new Edge(x,y,c));
        }

        Collections.sort(edges);

        int ans = 0;
        for(Edge edge : edges){
            // 부모가 하나의 그룹이 아니면 추가 하기
            int x = edge.x;
            int y = edge.y;
            if(getParent(x) != getParent(y)){
                union(x,y);
                ans += edge.cost;
            }
            // 하나의 그룹이라면 넘어가기
        }

        System.out.println(ans);
    }
}
