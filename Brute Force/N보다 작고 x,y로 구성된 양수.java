import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

class Solution {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        for (int test_case = 1; test_case <= T; test_case++) {
            String N;
            int x, y;
            N = sc.next();
            x = sc.nextInt();
            y = sc.nextInt();

            // N이 한자리 수인 경우
            if (N.length() == 1) {
                if (Integer.parseInt(N) > y && x == 0) { // 8, 0, 5
                    System.out.println("#" + test_case + " " + y);
                    continue;
                } else { // 2, 0, 9 or 2, 6, 9
                    System.out.println("#" + test_case + " " + -1);
                    continue;
                }
            }

            // N이 두자리 이상
            boolean end_flag = false;
            String final_result = "";
            int digit = N.length(); // 최초 길이
            int count = digit;

            for (int i = 0; i < count; i++) {
                // 현 시점 최상위 숫자
                int firstNum = Integer.parseInt(String.valueOf(N.charAt(0)));

                // 최상위 숫자가 y보다 큰 경우 digit만큼 전부 y로 채우고 해당 test case를 종료한다.
                if (firstNum > y) {
                    for (int j = 0; j < digit; j++) {
                        final_result += String.valueOf(y);
                    }
                    break;
                }

                // 최상위 숫자가 x,y보다 작으면 digit - 1 만큼 전부 y로 채우고 해당 test case를 끝낸다.
                else if (firstNum < x && firstNum < y) {
                    for (int j = 0; j < digit - 1; j++) {
                        final_result += String.valueOf(y);
                    }
                    break;
                }

                // 최상위 숫자가 x,y 사이인 경우 앞에 x를 두고 digit - 1 만큼 y를 채우고 종료한다.
                else if (y > firstNum && firstNum > x) {
                    final_result += String.valueOf(x);
                    for (int j = 0; j < digit - 1; j++) {
                        final_result += String.valueOf(y);
                    }
                    break;
                }

                // 최상위 숫자가 x와 같은 경우 x를 더하고 다음 숫자로 넘긴다.
                else if (firstNum == x) {
                    final_result += String.valueOf(x);
                    digit -= 1;
                }
                // 최상위 숫자가 y와 같은 경우 y를 추가하고 다음 숫자로 넘어간다.
                else if (firstNum == y) {
                    final_result += String.valueOf(y);
                    digit -= 1;
                }

                N = N.substring(1);
            }
            System.out.println("#" + test_case + " " + final_result);

        }
    }
}