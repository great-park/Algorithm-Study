#include <bits/stdc++.h>

using namespace std;

char str[55];
int main(){
	int tc;
	scanf("%d",&tc);

	while(tc--){
		scanf("%s",str);
		int n = strlen(str);

		stack<int> st;
		bool ok=1;

		for(int i=0;i<n;i++){
			if(str[i]=='('){
				st.push(1);
			}else{
				if(st.empty()){
					ok=0;
					break;
				}else{
					st.pop();
				}
			}
		}
		if(!st.empty())ok=0;

		puts(ok?"YES":"NO");
	}
}