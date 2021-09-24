#include <stdio.h>
#include <string.h>

int main(void) {
	int t;
	scanf("%d", &t);

	int room[15];
	int i, j;
	int h = 0;

	while (h < t) {
		scanf("%d", &i);
		scanf("%d", &j);
		int floor = 0;
		for (int a = 0; a < 14; a++) {
			room[a] = a;
		}
		while (floor < i) {
			for (k = 2; k <= j; k++) {
				room[k] += room[k - 1];
			}
			floor++;
		}
		printf("%d\n", room[j]);
		h++;
	}


	return 0;
}