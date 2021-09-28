#include <stdio.h>
#include <stdlib.h> 
int find_max_sub_middle(int arr[], int low, int middle, int high) {
	int left_sum = -99999;
	int sum = 0;
	int max_left =0;
	
	for (int i = middle; i >= low; i--) {
		sum = sum + arr[i];
		if (sum > left_sum)
			left_sum = sum;
			max_left = i;
			
	}

	int right_sum = -99999;
	sum = 0;
	int max_right=0;

	for (int j = middle + 1; j <= high; j++) {
		sum = sum + arr[j];
		if (sum > right_sum)
			right_sum = sum;
			max_right = j;
	}

	return (left_sum + right_sum);
}
int find_max_sub(int arr[], int low, int high) {
	if (high == low)
		return arr[low];
	else {
		int middle = (high + low) / 2;

		int max_sum_left = find_max_sub(arr, low, middle);
		int max_sum_right = find_max_sub(arr, middle + 1, high);
		int max_sum_cross = find_max_sub_middle(arr, low, middle, high);

		if (max_sum_left >= max_sum_right && max_sum_left >= max_sum_cross)
			return max_sum_left;
		else if (max_sum_right >= max_sum_left && max_sum_right >= max_sum_cross)
			return max_sum_right;
		else return max_sum_cross;
	}
}


int main() {
	int size;
	scanf("%d", &size);
	int* arr = (int*)malloc(sizeof(int) * size);

	for (int i = 0; i < size; i++) {
		scanf("%d", &arr[i]);
	}
	int ans = find_max_sub(arr,0,size-1);
	
	printf("%d",ans);

	free(arr);

	return 0;
}
