#include<stdio.h>

int main(){
	
	int weekday;
	printf("���� �Է�\n");
	scanf("%d", &weekday);
	switch(weekday){
		case 1 :
			printf("������");
			break;
		case 2 :
			printf("ȭ����");
			break; 
		case 3 :
			printf("������");
			break;
		case 4 :
			printf("�����");
			break;  
		case 5 :
			printf("�ݿ���");
			break; 	
		case 6 :
			printf("�����");
			break; 
		case 7 :
			printf("�Ͽ���");
			break;
		default :
			printf("1~7 �Է�");
			break; 
	} 
}
