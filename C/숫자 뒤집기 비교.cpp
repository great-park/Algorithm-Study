#include <stdio.h>
#include <string.h>

int main(void) {
	
	// 012, 345, 678, 9 10 11,12 13 14, 15 16 17 18, 19 20 21, 22 23 24 25
	char word[16];
	gets(word);
	
	int len = strlen(word); 
	int total = 0;
	// 입력받고, 아스키코드로 변환, case 문으로 들어가서 total 계 산
	
	for(int i =0; i<len;i++)
	{
		int x = word[i]-'A';
		switch(x){
			case 0 ... 2:
				total+= 3;
				break;
			case 3 ... 5:
				total+=4;
				break;
			case 6 ... 8:
				total+=5;
				break;
			case 9 ... 11:
				total+=6;
				break;
			case 12 ... 14:
				total+=7;
				break;
			case 15 ... 18:
				total+=8;
				break;
			case 19 ... 21:
				total+=9;
				break;
			case 22 ... 25:
				total+=10;
				break;
		}
			
	}  
	
	printf("%d",total);
	
	return 0;
}


