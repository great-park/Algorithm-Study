#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {

	char str[1000000];
	gets(str);
	
	int len = strlen(str);
	int cnt =1;



	for(int i=0;i<len;i++)
	{
		if(str[i]==' ')
		{
			cnt +=1;
		}
	}
	if(str[0] == ' ')
	{
		cnt -=1;
	}
	if(str[len-1] == ' ')
	{
		cnt -=1;
	}
	printf("%d",cnt);

    return 0;
}


