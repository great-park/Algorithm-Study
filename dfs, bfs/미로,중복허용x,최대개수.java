import java.util.*;

import static java.util.Collections.max;

class Solution {
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();


        for (int test_case = 1; test_case <= T; test_case++) {
            int R, C;
            R = sc.nextInt();
            C = sc.nextInt();
            String[][] city = new String[R][C];
            int[][] dist = new int[R][C];

            // 초기화
            for (int i = 0; i < R; i++) {
                String input = sc.next();
                city[i] = input.split("");
                for (int j = 0; j < C; j++) {
                    dist[i][j] = -1;
                }
            }
            
            int final_result = 0;
                    int temp = bfs(R,C,dist,city,0,0);
                    if (temp >= final_result) final_result = temp;
                    for (int n = 0; n < R; n++) {
                        for (int k = 0; k < C; k++) {
                            dist[n][k] = -1;
                        }
                    }

            System.out.println("#"+test_case+" "+final_result);
        }
    }

    public static int bfs(int R, int C, int[][] dist, String[][] city, int start_x, int start_y){
        Stack<Pair> qu = new Stack<Pair>();
        qu.push(new Pair(start_x, start_y));
        dist[start_y][start_x] = 0;
        ArrayList<String> gift = new ArrayList<>();
        gift.add(city[start_y][start_x]);

        Set<Integer> counts = new HashSet<>();
        while (!qu.isEmpty()) {
            Pair p = qu.pop();

            for (int i = 0; i < 4; i++) {
                int nX = p.x + dx[i];
                int nY = p.y + dy[i];

                // 범위 아웃
                if (nX < 0 || nX >= C  || nY < 0 || nY >= R ) {
                    continue;
                }
                // 이미 방문
                if (dist[nY][nX] != -1) {
                    continue;
                }
                // 기념품 있음
                if (gift.contains(city[nY][nX])) {
                    continue;
                }
                qu.push(new Pair(nX, nY));
                dist[nY][nX] = dist[p.y][p.x] + 1;
                gift.add(city[nY][nX]);
            }
            counts.add(gift.size());
        }

        return max(counts);
    }

    // 큐에 좌표를 넣어주기 위한 클래스
    public static class Pair {
        int x, y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public void setX(int x) {
            this.x = x;
        }

        public void setY(int y) {
            this.y = y;
        }
    }
}