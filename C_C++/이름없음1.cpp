#include<stdio.h>

int main(){
	
	int weekday;
	printf("요일 입력\n");
	scanf("%d", &weekday);
	switch(weekday){
		case 1 :
			printf("월요일");
			break;
		case 2 :
			printf("화요일");
			break; 
		case 3 :
			printf("수요일");
			break;
		case 4 :
			printf("목요일");
			break;  
		case 5 :
			printf("금요일");
			break; 	
		case 6 :
			printf("토요일");
			break; 
		case 7 :
			printf("일요일");
			break;
		default :
			printf("1~7 입력");
			break; 
	} 
}
