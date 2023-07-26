#include <stdio.h>
#include <string.h>

int main() {
    
    int n = 0;
    scanf("%d",&n);

    for(int i=0; i<n; i++)
    {
    	int b = 0;
    	char cases[20] = {0, };
    	
    	scanf("%d %s", &b, cases);
    	
    	char tot[160];
    	
    	
		for(int j=0; j<strlen(cases); j++)
		{
			for(int x =0; x<b;x++)
			{
				printf("%c", cases[j]);
			}
		} 
		printf("\n");
	}
    return 0;
}
