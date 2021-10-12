#include <bits/stdc++.h>

using namespace std;
const int MAXN=100;

vector<int> v[MAXN];
bool visited[MAXN];

int main(){
	queue<int> q;
	q.push(1);
	visited[1]=true;

	while(!q.empty()){
		int cur=q.front();
		q.pop();
		for(int i=0;i<v[cur].size();i++){
			int next=v[cur][i];
			if(!visited[next]){
				q.push(next);
				visited[next]=true;
			}
		}
	}

	
}