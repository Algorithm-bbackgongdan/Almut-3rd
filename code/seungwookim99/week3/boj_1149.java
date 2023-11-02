// 백준 1149 : RGB거리
// Java 풀이
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    int N;
    ArrayList<House> house = new ArrayList<>();

    class House {
        int R,G,B;
        House (int R, int G, int B) {
            this.R = R;
            this.G = G;
            this.B = B;
        }
    }
    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // for read
        StringBuilder sb = new StringBuilder(); // for output

        /* get input */
        N = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < N ; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            house.add(new House(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            ));
        }

        /* initialize */
        House dp[] = new House[N];
        for (int i = 0 ; i < N ; i++)
            dp[i] = new House(0, 0, 0);
        dp[0].R = house.get(0).R;
        dp[0].G = house.get(0).G;
        dp[0].B = house.get(0).B;

        /* dp */
        for (int i = 1 ; i < N ; i++) {
            dp[i].R = house.get(i).R + Math.min(dp[i-1].G, dp[i-1].B);
            dp[i].G = house.get(i).G + Math.min(dp[i-1].R, dp[i-1].B);
            dp[i].B = house.get(i).B + Math.min(dp[i-1].R, dp[i-1].G);
        }

        sb.append(Math.min(dp[N-1].R, Math.min(dp[N-1].G, dp[N-1].B)));
        System.out.println(sb);
    }

    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}