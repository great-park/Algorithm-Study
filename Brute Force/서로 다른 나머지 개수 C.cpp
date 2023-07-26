#include <stdio.h>
#include <string.h>
int main() {
	
	int str[11] ={0};
	int i,j, cnt = 0;
	
	for(i=0;i<10;i++){
		scanf("%d",&str[i]);
	}
	i=0;
	for(i=0;i<10;i++){
		str[i] = str[i]%42 ;
	}
	i=0;
	for(i=0;i<10;i++){
		for(j=i+1;j<10;j++){
			if(str[i]==str[j]){
				str[j]=99;
			}
		}
	}
	i=0;
	for(i=0;i<10;i++){
		if(str[i] != 99){
			cnt++;
		}
	}
	printf("%d", cnt);
  return 0;
}

