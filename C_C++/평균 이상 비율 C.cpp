#include <stdio.h>
#include <string.h>


int main() {
	int case_num;
	scanf("%d",&case_num);
	int str[1000]={0};

	for(int i =0; i<case_num; i++){
		int stu_num, sum = 0;
		scanf("%d", &stu_num);
		for(int j=0; j<stu_num; j++){
			scanf("%d", &str[j]);
			sum += str[j];
		}
	
		double avg = (double)sum/stu_num;
		int over_num=0;
		for (int k =0; k<stu_num; k++){
			if(str[k]>avg){
				over_num++;
			}
		}
		double ratio = ((double)over_num/stu_num) * 100;
		
		printf("%.3f%%\n", ratio);
		
		
	}

	return 0;

}

