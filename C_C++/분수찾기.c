#include <stdio.h>

int main(void) {

	// 주어진 숫자의 row와 coulmn 인덱스를 구하면 됨
	// 등차수열의 합 n(n+1)/2 까지 각 층이 구성됨
	// ex 4층 =>(1,4) (2,3) (3,2) (4,1)
	// 짝수 층 -> 1행쪽에서 시작, 홀수 층 -> 1열쪽에서 시작

	int x;
	scanf("%d", &x);
	int f = 1, i = 1;
	while (1)
	{
		if (x == 1) break;
		else if (i + 1 <= x && x <= f * (f + 1) / 2) break;
		else
		{
			i = f * (f + 1) / 2;
			f += 1;
		}
	}
	//해당 층에서 몇번째인지 구하기
	if (f % 2 == 0) {
		int start = f * (f - 1) / 2 + 1;
		int cnt = 1;
		while (1)
		{
			if (start == x) break;
			else {
				cnt++;
				start++;
			}
		}
		int u = 1, d = f; // 짝수는 1행에서 시작하므로 분자가 1, 분모가 층수
		for (int a = 1; a < cnt; a++)
		{
			u++;
			d--;
		}
		printf("%d/%d", u, d);
	}
	else if (f % 2 != 0)
	{
		int start = f * (f - 1) / 2 + 1;
		int cnt = 1;
		while (1)
		{
			if (start == x) break;
			else {
				cnt++;
				start++;
			}
		}
		int u = f, d = 1; // 홀수는 1열에서 시작하므로 분자가 층수, 분모가 1
		for (int a = 1; a < cnt; a++)
		{
			u--;
			d++;
		}
		printf("%d/%d", u, d);
	}
	return 0;

}