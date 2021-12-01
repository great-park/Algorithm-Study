#include <stdio.h>

int N, m;
int graph[105][105];
int check[105];
int queue[105];
int origin[105];

int stack[105];
int top = 0;

void dfs(int cur_vertex);

int main() {
	scanf("%d", &N);
	scanf("%d", &m);

	for (int i = 0; i < m; i++) {
		int s, e;
		scanf("%d %d", &s, &e);
		graph[s][e] = 1;
	}

	int front = 0, rear = 0; // front는 현재 번호, rear는 번호표를 뽑으면 받게 되는 번호
	check[1] = 1;      // 방문했던 정점 체크
	queue[rear] = 1;  //BFS의 시작 정점이 1번 정점이다.
	origin[rear] = -1; // 첫 origin은 -1
	rear++;

	printf("BFS : ");
	while (front < rear) {    // rear - front >0 이어야 빈 큐가 아니다.
		int cur_vertex = queue[front];
		printf("%d ", cur_vertex);

		for (int x = 1; x <= N; x++) {
			if (graph[cur_vertex][x] == 1 && check[x] == 0) {
				queue[rear] = x;
				check[x] = 1;
				origin[rear] = front;
				rear++;
			} // 뻗어 나갈 수 있는 정점 큐에 다 담기
		}
		//다음 번호표
		front++;
	}

	printf("\n");

	printf("DFS : ");
   
   int cur_vertex = 1;
   check[1] = 2;
   stack[top++] = cur_vertex;
   printf("%d ", cur_vertex);

   while (top >= 0) {
      TP:
      int cur_vertex = stack[top - 1];
      for (int x = 1; x <= N; x++) {
         if (graph[cur_vertex][x] == 1 && check[x] != 2) {
            stack[top++] = x;
            check[x] = 2;
            printf("%d ", x);
            goto TP;
         }
      }
      top--;
   }

	
	printf("DFS2 : ");
	dfs(1);
}

void dfs(int cur_vertex)
{
	check[cur_vertex] = 3;
	printf("%d ", cur_vertex);
	for (int x = 1; x <= N; x++) {
		if (graph[cur_vertex][x] == 1 && check[x] != 3) {
			dfs(x);
		}
	}
}
