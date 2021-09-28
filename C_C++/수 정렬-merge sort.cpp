#include <bits/stdc++.h>

using namespace std;

int a[1000000], tem[1000000];

void mergesort(int start, int end){

	if(start == end)return;

	int middle = (start + end)/2;

	mergesort(start,middle); mergesort(middle+1,end);

	int pointer1 = start, pointer2 = middle+1;
	int now = start;

// 정렬된 배열 두 개를 정렬하면서 합치는 과정
	while(pointer1<=middle && pointer2 <= end){
		int x =a[pointer1], y =a[pointer2];

		if(x<y){
			tem[now++]=x;
			pointer1++;
		}else{
			tem[now++]=y;
			pointer2++;
		}
	}
// 한 쪽 배열이 끝나면 나머지는 그대로 삽입 
	while(pointer1<=middle){
		tem[now++]=a[pointer1];
		pointer1++;
	}

	while(pointer2<=end){
		tem[now++]=a[pointer2];
		pointer2++;
	}
// 정렬된 배열 넘겨주기
	for(int i=start; i<=end; i++)a[i]=tem[i];
}

int main(){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++)scanf("%d",&a[i]);
	mergesort(0,n-1);

	for(int i=0;i<n;i++)printf("%d\n",a[i]);
}