import java.util.Scanner;
import static java.lang.Integer.max;


public class Main {
    public static Scanner sc = new Scanner(System.in);
    public static int n;
    public static int[][] board;
    public static int[] dy = {-1,1,0,0};
    public static int[] dx = {0,0,-1,1};
    public static boolean[] l;
    public static boolean[] r;

    public static int backTracking(int y, int x, int cnt){
        if(x >= n){
            y++;
            if(x%2 == 0){
                x = 1;
            }else{
                x = 0;
            }
        }
        if(y>=n){
            return cnt;
        }
        int count = 0;

        if(board[y][x] == 1 && !l[y - x + n - 1] && !r[y + x]){
            l[y - x + n - 1] = true;
            r[y + x] = true;
            count = max(count,backTracking(y,x + 2 , cnt + 1));
            l[y - x + n - 1] = false;
            r[y + x] = false;
        }
        return max(count,backTracking(y,x+2,cnt));
    }
    public static void main(String[] args) {
        n = sc.nextInt();
        board = new int[n][n];
        l = new boolean[2 * n];
        r = new boolean[2 * n];

        for(int i = 0 ;i<n;i++){
            for(int j = 0 ;j<n;j++){
                board[i][j] = sc.nextInt();
            }
        }
        int ans = backTracking(0,0,0) + backTracking(0,1,0);
        System.out.println(ans);
    }
}