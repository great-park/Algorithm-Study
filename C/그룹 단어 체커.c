#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
	int N;
	int cnt = 0;
	char arr[101];
	int alpha[26] = { 0, };
	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		scanf("%s", arr, sizeof(arr)); //�ܾ��Է�
		//�� ���ڿ� ���� ���ڰ� �ٸ� ���  
		//���ڿ� �ش��ϴ� alpha�� 1����. 
		//j+1�� �ش�Ǵ� ���ڸ� alpha���� ã�� 1�̸� ������ �������� �ִ� ������.
		//0�̸� �������� ����.
		//j++;
		for (int j = 0; arr[j] != '\0'; j++) {
			if (arr[j + 1] != '\0' && arr[j] != arr[j + 1]) {
				alpha[arr[j] - 'a'] = 1;
				if (alpha[arr[j + 1] - 'a'] == 1) {
					cnt++;
					break;
				}
			}

		}
		memset(arr, 0, sizeof(arr));
		memset(alpha, 0, sizeof(alpha));
	}
	printf("%d\n", N - cnt);



	return 0;
}