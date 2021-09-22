#include <stdio.h>

int main(void) {

	int a, b, v;
	scanf("%d%d%d", &a, &b, &v);
	int day = 1;
	// 성공한 시점에서는 v-b오르면 됨
	day =(v - b -1) / (a - b) + 1;

	printf("%d", day);
	return 0;

}