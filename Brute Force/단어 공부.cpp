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
���ĺ� �迭�� �� �� - �ε��� 0������ a ������ z�� ���� ���� 
���ڿ� �Է� �� ù ��Һ��� �۾�

�ش� ���ڸ� �ƽ�Ű �ڵ�� ��ȯ�Ͽ� ���� �� -'a'�� �ؼ�
�ش� ��ġ�� 1�� �߰��ϵ��� �Ѵ�.

�빮�ڿ� �ҹ����� ������ �ٲ�� �ϴµ�, �̴� if������ �ƽ�Ű �ڵ���
������ ������� �з��Ѵ�.  

*/  

// strlen() ��ü�� O(n)�̹Ƿ� for�� �ۿ��� ����Ͽ� ����� ��
// char ans -> int ans�� overflow �ذ� 
