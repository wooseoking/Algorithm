import java.util.*;

class Solution {
    
    static Map<String,List<String>> graph;
    static List<String> res;
    static boolean[] v;
    static int n;
    
    //                     티켓 사용 횟수 , 현재 위치
    public static Boolean dfs(int cnt,String cur,String[][] tickets){
        // 다 사용했으면 끝
        if(cnt == n) return true;
        
        if(!graph.containsKey(cur)) return false;
        
        // 다음 위치 찾기
        for(String nextCity : graph.get(cur)){
            
            for(int i = 0 ;i<n;i++){
                String from = tickets[i][0];
                String to = tickets[i][1];
                
                if(!v[i] && cur.equals(from) && nextCity.equals(to)){
                    v[i] = true;
                    res.add(nextCity);
                    if(dfs(cnt + 1,nextCity,tickets)) return true;
                    res.remove(res.size()-1);
                    v[i] = false;
                }
            }
        }
        return false;
    }
    public String[] solution(String[][] tickets) {
        n = tickets.length;
        graph = new HashMap();
        res = new ArrayList<>();
        v = new boolean[n];
        
        for(String[] t : tickets){
            String from = t[0];
            String to = t[1];
            
            if(!graph.containsKey(from)){
                graph.put(from,new ArrayList<>());
            }
            graph.get(from).add(to);
        }
        
        // 공항 정렬
        for(String from : graph.keySet()){
            Collections.sort(graph.get(from));
        }
        
        String start = "ICN";
        res.add(start);
        
        dfs(0,start,tickets);
        
        for(String r : res){
            System.out.println(r);
        }
        
        String[] answer = res.toArray(new String[0]);
        return answer;
    }
}