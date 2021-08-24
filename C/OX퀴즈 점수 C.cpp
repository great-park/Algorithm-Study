#include <stdio.h>
#include <string.h>


int main() {
	
	int i,j,n, cnt = 0, sum =0;
	scanf("%d", &n);
	char str[1000];
	for(i=0;i<n;i++){
		scanf("%s",str);
		for(j=0;j<strlen(str);j++){
			if(str[j]=='O'){
				while(str[j] != 'X'){
					cnt++;
					sum+=cnt;
					j++;
					if(j==strlen(str)) break;
				}
			} cnt = 0;
		} printf("%d\n", sum);
		sum=0;
	}

	return 0;

}
