#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char cases[1000000] = {0, };
	scanf("%s", cases);
	
	int ans[26]= {0, };
	
	int a = 'a', z = 'z';
	int cap_a = 'A', cap_z = 'Z';
	int len = strlen(cases);
	
	for(int j=0; j<len; j++)
	{
		int x = cases[j];
		
		if(a<= x && x <=z)
		{
			ans[x-a] += 1;
		}
		else if(cap_a <= x && x <= cap_z)
		{
			ans[x-cap_a] += 1;
		}
	}
	
	int max_index = 0;
	int indicator = 0;
	for(int i =1; i<26;i++)
	{
		if(ans[i] > ans[max_index])
		{
			max_index = i;
			indicator = 0;
		}	
		else if(ans[i] == ans[max_index])
		{
			indicator = 1;
		}
	}
	
	if(indicator == 1)
	{
		printf("?");
	} 
	else 
	{
		printf("%c", max_index + 'A');
	}
	
	
	
    return 0;
}

/*
알파벳 배열을 준 비 - 인덱스 0번에는 a 끝에는 z에 대한 정보 
문자열 입력 후 첫 요소부터 작업

해당 문자를 아스키 코드로 변환하여 받은 후 -'a'를 해서
해당 위치에 1를 추가하도록 한다.

대문자와 소문자의 구분을 바꿔야 하는데, 이는 if문으로 아스키 코드의
범위를 구분지어서 분류한다.  

*/  

// strlen() 자체가 O(n)이므로 for문 밖에서 계산하여 사용할 것
// char ans -> int ans로 overflow 해결 
