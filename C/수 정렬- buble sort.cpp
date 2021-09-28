# include <bits/stdc++.h>

using namespace std;

int a[1000];
int main(){

    int x;
    scanf("%d",&x);
    for(int i=0;i<x;i++)scanf("%d",a+i);

    for(int i =1; i<x; i++){
        for(int j=0;j<x-1;j++){
            if(a[j]>a[j+1])swap(a[j],a[j+1]);
        }
    }

    for(int i=0;i<x;i++)printf("%d\n",a[i] );

    return 0;
}
