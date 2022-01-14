#include <bits/stdc++.h>

using namespace std;

int a[1000000], tem[1000000];

void bubblesort(int start, int end){
	for(int j=0; j<end-1;j+=2)
	{
		if(a[j]>a[j+2]){
			swap(a[j],a[j+2]);
			swap(a[j+1],a[j+3]);
		}else if(a[j]==a[j+2]){
			if(a[j+1]>a[j+3]){
				swap(a[j+1],a[j+3]);
				swap(a[j],a[j+2]);
			}
		}
	}
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<2*n;i++)scanf("%d",&a[i]);
	bubblesort(0,2*n-1);

	for(int i=0;i<2*n;i+=2){
		printf("%d %d\n",a[i],a[i+1]);
	}
}
