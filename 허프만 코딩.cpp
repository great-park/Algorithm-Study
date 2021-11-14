#include<stdio.h>
#include<stdlib.h>
#include<string.h>

typedef struct node
{
	int freq;
	struct node* left;
	struct node* right;
}Node;

struct node** heap;
int maxId = 0;

char str[10000];
int strId = -1;

void insertHeap(Node* cur)
{
	maxId++;
	heap[maxId] = cur;

	int id = maxId;
	int parent = id / 2;
	
	while (parent >= 1)
	{
		if (heap[parent]->freq > heap[id]->freq)
		{
			Node* t = heap[parent];
			heap[parent] = heap[id];
			heap[id] = t;

			id = parent;
			parent = id / 2;
		}
		else
		{
			break;
		}
	}
}

Node* popHeap()
{
	if (maxId <= 0)
	{
		return 0;
	}

	Node* popNode = heap[1];

	heap[1] = heap[maxId];
	maxId--;

	int parent = 1;
	int left = 2 * parent;
	int right = 2 * parent + 1;

	while (1)
	{
		if (left > maxId)
		{
			break;
		}
		else if (right > maxId)
		{
			if (heap[left]->freq < heap[parent]->freq)
			{
				Node* t = heap[left];
				heap[left] = heap[parent];
				heap[parent] = t;

				parent = left;
				left = 2 * parent;
				right = 2 * parent + 1;
			}
			else
			{
				break;
			}
		}
		else
		{
			int small;
			if (heap[left]->freq <= heap[right]->freq)
			{
				small = left;
			}
			else
			{
				small = right;
			}
			if (heap[small]->freq < heap[parent]->freq)
			{
				Node* t = heap[small];
				heap[small] = heap[parent];
				heap[parent] = t;

				parent = small;
				left = 2 * parent;
				right = 2 * parent + 1;
			}
			else
			{
				break;
			}
		}
	}

	return popNode;
}


void search(Node* cur, char x)
{
	strId++;
	str[strId] = x;
	str[strId + 1] = 0;

	if (cur->left == 0 && cur->right == 0)
	{
		printf("%s\n", str);
	}
	else
	{
		search(cur->left, '0');
		search(cur->right, '1');
	}
	str[strId] = 0;
	strId--;
	return;
}
int main()
{
	int cnt;
	scanf("%d", &cnt);

	heap = (Node**)malloc((cnt + 1) * sizeof(Node*));
	memset(heap, 0, (cnt + 1) * sizeof(Node*));

	for (int i = 0; i < cnt; i++)
	{
		int input_freq;
		scanf("%d", &input_freq);
		Node* newNode = (Node*)malloc(sizeof(Node));
		newNode->freq = input_freq;
		newNode->left = newNode->right = 0;
		insertHeap(newNode);
	}

	Node* x_node = 0;
	Node* y_node = 0;

	while (1)
	{
		x_node = popHeap();
		y_node = popHeap();

		if (y_node == 0)
			break;

		Node* newNode = (Node*)malloc(sizeof(Node));
		newNode->freq = x_node->freq + y_node->freq;
		newNode->left = x_node;
		newNode->right = y_node;

		insertHeap(newNode);
	}

	//¼øÈ¸

	search(x_node->left, '0');
	search(x_node->right, '1');

	
}