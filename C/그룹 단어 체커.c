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
		scanf("%s", arr, sizeof(arr)); //단어입력
		//현 문자와 다음 문자가 다를 경우  
		//문자에 해당하는 alpha에 1저장. 
		//j+1에 해당되는 문자를 alpha에서 찾아 1이면 이전에 나온적이 있는 문자임.
		//0이면 나온적이 없음.
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