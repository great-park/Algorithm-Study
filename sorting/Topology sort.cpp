#include <stdio.h>

int N, m;
int graph[105][105];
int check[105];
int queue[105];
int indegree[105];

int main()
{
   scanf("%d", &N); // 정점 번호는 1~N까지 존재한다.
   scanf("%d", &m);

   for (int i = 0; i < m; i++) {
      int s, e;
      scanf("%d %d", &s, &e);
      graph[s][e] = 1;
      indegree[e]++;
   }

   int front = 0, rear = 0;
   for (int i = 1; i <= N; i++) {
      if (indegree[i] == 0) {
         queue[rear++] = i;
      }
   }

   while (front < rear) {
      int cur_node = queue[front];

      for (int i = 1; i <= N; i++) {
         if (graph[cur_node][i] == 1) {
            indegree[i]--;

            if (indegree[i] == 0) {
               queue[rear++] = i;
            }
         }
      }

      front++;
   }

   for (int i = 0; i < N; i++) {
      printf("%d ", queue[i]);
   }
}
