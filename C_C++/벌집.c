
#include <stdio.h>

int main(void) {

	long long n, count = 2, different = 6, min = 1, max = 1;

	scanf("%lld", &n);

	if (n == 1) {

		printf("%lld", n);

		return 0;

	}

	while (1) {

		min = max + 1;

		different *= (count - 1);

		max = max + different;

		if (min <= n && max >= n) {

			printf("%lld", count);

			break;

		}

		count++;
		different = 6;
	}

	return 0;

}