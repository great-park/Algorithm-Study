#include <stdio.h>

int heap[100000];
int n;
int hsize = 0;

void insert_heap(int value)
{
	//맨 마지막에 넣 기 
	heap[++hsize] = value;

	int x = hsize;
	while (x > 1) {
		if (heap[x] < heap[x / 2]) {
			int t = heap[x];
			heap[x] = heap[x / 2];
			heap[x / 2] = t;
			x = x / 2;
		}
		else {
			break;
		}
	}
}

int pop_heap()
{
	int pop = heap[1];

	heap[1] = heap[hsize--];

	int x = 1;
	while (x*2 <= hsize) {
		int small_child;
		if (heap[x * 2] < heap[x * 2 + 1] || x*2+1 > hsize) {
			small_child = x * 2;
		}
		else {
			small_child = x * 2 + 1;
		}
		if (heap[x] > heap[small_child]) {
			int t = heap[x];
			heap[x] = heap[small_child];
			heap[small_child] = t;

			x = small_child;
		}
		else
		{
			break;
		}
	}

	return pop;
}

int main()
{
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		int t;
		scanf("%d", &t);
		insert_heap(t);
	}
	while (hsize > 0) {
		printf("%d ", pop_heap());
	}
}
