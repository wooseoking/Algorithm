import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
 TreeSet<Integer> tree = new TreeSet<>();

        for(String op : operations){
            String[] s = op.split(" ");
            String o1 = s[0];
            String o2 = s[1];

            if(o1.equals("I")){
                int number = Integer.parseInt(o2);
                tree.add(number);
            }else{
                if(o2.equals("-1")){
                    if(!tree.isEmpty()){
                        tree.pollFirst();
                    }
                }else{
                    if(!tree.isEmpty()){
                        tree.pollLast();
                    }
                }
            }
        }
        int[] answer = new int[2];
        if(!tree.isEmpty()){
            answer[0] = tree.last();
            answer[1] = tree.first();
        }
        return answer;
    }
}