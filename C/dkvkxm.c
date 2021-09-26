#include <stdio.h>

int SquareByValue(int);

int main(void)
{
	int a;
	printf("양의 정수를 입력하시오 : ");
	scanf("%d", a);
	SquareByValue(a);
	return 0;
}

int SquareByValue(int x) {

	x *= x;

	printf("Value 함수 제곱 : %d", x);
}