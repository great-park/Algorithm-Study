#include <stdio.h>
#include <string.h>
int main() {
	int A,B,C;
	int i,k=0,x=1;
	int cnt = 0;
	int num_cnt = 0;
	scanf("%d%d%d",&A,&B,&C);
	int prod = A*B*C;
	int temp = prod;
	char result[50] = {0};

	while ( (prod/x) !=0)
	{
		x *=10;
		cnt++;
	}
	x/=10;
	
	for (i=0;i<cnt;i++)
	{
		result[i] = (temp/x);
		temp = temp - (temp/x)*x;
		x /= 10;
	}
	i = 0;
	
	for(k=0;k<10;k++)
	{
		for(i=0;i<cnt;i++)
		{
			if(result[i]==k)
			{
				num_cnt++;
			}
		} printf("%d\n", num_cnt);
		num_cnt = 0;
	}
	
	
  return 0;
}

