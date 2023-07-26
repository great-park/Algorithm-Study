#include<stdio.h>

int main(void) {
	int a[100000] = {0}, i, test, x;
	for(i=1;i<=10000;i++) {
		if(a[i]==0) 
			printf("%d\n", i);
		test = x = i;
		for(;test!=0;test/=10)
			x += test%10;
		a[x] = 1;
	}
}
