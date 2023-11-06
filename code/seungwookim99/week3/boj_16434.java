import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    int N, atk;
    ArrayList<Room> rooms = new ArrayList<>();

    class Room {
        public Room(long t, long a, long h) {
            this.t = t;
            this.a = a;
            this.h = h;
        }
        long t, a, h;
    }

    private boolean isPossible(long maxHP) {
        long currHP = maxHP, currAtk = atk;
        for(int i = 0 ; i < N ; i++) {
            if (rooms.get(i).t == 1) {
                // monster
                int my_atk_count = (int)(Math.ceil((double) rooms.get(i).h / currAtk));
                int monster_atk_count = (int)(Math.ceil((double) currHP / rooms.get(i).a));
                if (my_atk_count <= monster_atk_count) {
                    // win
                    currHP -= (my_atk_count - 1) * rooms.get(i).a;
                } else {
                    // lose
                    return false;
                }
            } else {
                // potion
                currAtk += rooms.get(i).a;
                if (currHP + rooms.get(i).h > maxHP)
                    currHP = maxHP;
                else
                    currHP += rooms.get(i).h;
            }
        }
        return true;
    }

    public void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // for input
        StringBuilder sb = new StringBuilder(); // for output
        StringTokenizer st = new StringTokenizer(br.readLine());

        // get input
        N = Integer.parseInt(st.nextToken());
        atk = Integer.parseInt(st.nextToken());
        for (int i = 0 ; i < N ; i++) {
            st = new StringTokenizer(br.readLine());
            rooms.add(new Room(
                    Long.parseLong(st.nextToken()),
                    Long.parseLong(st.nextToken()),
                    Long.parseLong(st.nextToken())
            ));
        }

        long left = 1, right = Long.MAX_VALUE - 1, mid, answer = 0;
        while (left <= right) {
            mid = (left + right) / 2;
            if (isPossible(mid)) {
                right = mid - 1;
                answer = mid;
            }
            else
                left = mid + 1;
        }
        sb.append(answer);
        System.out.println(sb);
    }
    public static void main(String[] args) throws Exception {
        new Main().solution();
    }
}