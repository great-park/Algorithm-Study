#include <stdio.h>

int SquareByValue(int);

int main(void)
{
	int a;
	printf("���� ������ �Է��Ͻÿ� : ");
	scanf("%d", a);
	SquareByValue(a);
	return 0;
}

int SquareByValue(int x) {

	x *= x;

	printf("Value �Լ� ���� : %d", x);
}