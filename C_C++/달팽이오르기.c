#include <stdio.h>

int main(void) {

	int a, b, v;
	scanf("%d%d%d", &a, &b, &v);
	int day = 1;
	// ������ ���������� v-b������ ��
	day =(v - b -1) / (a - b) + 1;

	printf("%d", day);
	return 0;

}