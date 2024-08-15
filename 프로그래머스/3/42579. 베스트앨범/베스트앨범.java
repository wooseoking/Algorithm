import java.util.*;

class Solution {
    public static class Music implements Comparable<Music>{
        
        public int index;
        public String generes;
        int totalPlays;
        int plays;
        
        public Music(int index,String generes,int totalPlays ,int plays){
            this.index = index;
            this.generes = generes;
            this.plays = plays;
            this.totalPlays = totalPlays;
        }
        
        public void setTotalPlays(int totalPlays){
            this.totalPlays = totalPlays;
        }
        
        @Override
        public int compareTo(Music other){
            if(this.totalPlays == other.totalPlays){
                if(this.plays == other.plays){
                    return this.index - other.index;
                }else{
                    return other.plays - this.plays;
                }
            }else{
                return other.totalPlays - this.totalPlays;
            }
        }
    }
    
    public int[] solution(String[] genres, int[] plays) {
        int n = plays.length;
        
        List<Music> musics = new ArrayList<>();
        Map<String,Integer> map = new HashMap<>();
        
        Map<String,Integer> songsIn = new HashMap<>();
        
        for(int i = 0 ;i<n;i++){
            String genre = genres[i];
            int play = plays[i];
            
            if(!map.containsKey(genre)){
                map.put(genre,play);
                songsIn.put(genre,0);
            }else{
                map.put(genre,map.get(genre) + play);
            }
        }
        
        for(int i = 0 ;i<n;i++){
            
            String genre = genres[i];
            int play = plays[i];
            int totalPlay = map.get(genre);
            
            Music music = new Music(i,genre,totalPlay,play);
            musics.add(music);
        }
        
        Collections.sort(musics);
        List<Integer> answer = new ArrayList<>();
        
        for(int i = 0 ;i<n;i++){
            String genre = musics.get(i).generes;
            if(songsIn.get(genre) < 2){
                songsIn.put(genre,songsIn.get(genre) + 1);
                answer.add(musics.get(i).index);
            }
        }
        
        int[] output = new int[answer.size()];
        for(int i = 0 ;i<answer.size();i++){
            output[i] = answer.get(i);
        }
        return output;
    }
}