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

	int front = 0, rear = 0; // front�� ���� ��ȣ, rear�� ��ȣǥ�� ������ �ް� �Ǵ� ��ȣ
	check[1] = 1;      // �湮�ߴ� ���� üũ
	queue[rear] = 1;  //BFS�� ���� ������ 1�� �����̴�.
	origin[rear] = -1; // ù origin�� -1
	rear++;

	printf("BFS : ");
	while (front < rear) {    // rear - front >0 �̾�� �� ť�� �ƴϴ�.
		int cur_vertex = queue[front];
		printf("%d ", cur_vertex);

		for (int x = 1; x <= N; x++) {
			if (graph[cur_vertex][x] == 1 && check[x] == 0) {
				queue[rear] = x;
				check[x] = 1;
				origin[rear] = front;
				rear++;
			} // ���� ���� �� �ִ� ���� ť�� �� ���
		}
		//���� ��ȣǥ
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
