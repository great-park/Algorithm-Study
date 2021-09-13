#include <stdio.h>
#include <stdlib.h>
//int main()
//{
//	int n = 0;
//	char s[50];
//	int sum = 0;
//
//	scanf_s("%d", &n);
//	scanf_s("%s", s, 50); 
//	for (int i = 0; i < n; i++)
//	{
//		sum += s[i] - '0';
//	}
//	printf("%d", sum);
//	return 0;
//}

int main(){
	int x =0;
	char y[200];
	int sum =0;
	
	scanf("%d\n",&x);
	scanf("%s",y);
	
	for(int j=0; j<x; j++){
		sum += y[j] - '0';
	}
	
	printf("%d",sum);
	return 0;
	
	
}
