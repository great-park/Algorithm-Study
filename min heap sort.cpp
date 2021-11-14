#include <bits/stdc++.h>
using namespace std;
int queue_1[10000];
int front = 0, rear = -1;


typedef struct node 
{
	int freq;
	struct node* left;
	struct node* right;
}Node;
 
 //�ε��� 0���� 
void heapify(Node* arr[], int n, int i)
{
    int smallest = i; 
    int l = 2 * i +1; 
    int r = 2 * i +1+1; 
 
    if (l < n && arr[l]->freq < arr[smallest]->freq)
        smallest = l;
 
    if (r < n && arr[r]->freq < arr[smallest]->freq)
        smallest = r;
 
    if (smallest != i) {
        swap(arr[i], arr[smallest]);
 
        heapify(arr, n, smallest);
    }
}
 
void heapSort(Node* arr[], int n)
{
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
 
    for (int i = n - 1; i >= 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}
 

void insert(int num)
{
	rear++;
	queue_1[rear] = num;
}

int delete_element()
{
	int val;
	val = queue_1[front];
	front++;
	if (front > rear) // front�� �Ű��� �� front�� rear���� ũ�ٸ�, ������ �� ť�� �� ť�� �Ǵ� ��
		front = rear = -1;
	return val; // ���� �� �˷��ֱ�

}

int main()
{
    struct node* arr[1000];
    int x;
	scanf("%d", &x);
	for (int i = 0; i < x; i++) {
		int t;
		scanf("%d", &t);
		Node* newNode = (Node*)malloc(sizeof(Node));
		newNode->freq = t;
		newNode->left =NULL;
		newNode->right=NULL;
		arr[i]=newNode;
	}
    int n = x;
    heapSort(arr, n);
    
    for(int i =n-1; i>=0;i--){
    	insert(arr[i]->freq);
	}
	for (int i = front; i <= rear; i++){
		printf("%d ", queue_1[i]);
	}
	
}
