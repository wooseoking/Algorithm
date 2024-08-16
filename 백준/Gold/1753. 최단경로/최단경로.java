import java.util.*;

public class Main {
    static int n,m;
    static int start;
    static Scanner sc = new Scanner(System.in);
    static List<List<Point>> g = new ArrayList<>();

    static class Point implements Comparable<Point>{
        public int to;
        public int cost;

        public Point(int to, int cost){
            this.to = to;
            this.cost = cost;
        }

        @Override
        public int compareTo(Point other){
            return this.cost - other.cost;
        }
    }

    public static int[] Dijikstra(int start){
        int[] d = new int[n + 1];
        for(int i = 0 ;i<n + 1;i++){
            d[i] = Integer.MAX_VALUE;
        }
        d[start] = 0;
        Queue<Point> pq = new PriorityQueue<>();
        pq.add(new Point(start,0));

        while(!pq.isEmpty()){
            Point curPoint = pq.poll();
            int cur = curPoint.to;
            int cost = curPoint.cost;

            if(d[cur] < cost)continue;

            for(Point nextPoint : g.get(cur)){
                int nextCost = cost + nextPoint.cost;
                int next = nextPoint.to;

                if(nextCost < d[next]){
                    d[next] = nextCost;
                    pq.add(new Point(next,nextCost));
                }
            }
        }

        return d;
    }
    public static void main(String[] args) {
        n = sc.nextInt();
        m = sc.nextInt();
        start = sc.nextInt();

        for(int i = 0 ;i<n + 1;i++){
            g.add(new ArrayList<>());
        }
        for(int i = 0 ;i<m;i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            int c = sc.nextInt();

            g.get(x).add(new Point(y,c));
        }

        int[] d = Dijikstra(start);

        for(int i = 1;i<d.length;i++){
            if(d[i] == Integer.MAX_VALUE) System.out.println("INF");
            else System.out.println(d[i]);
        }
    }
}
