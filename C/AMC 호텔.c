#include <stdio.h>

int main(void) {

	int x;
	int room=0;
	scanf("%d", &x);
	for (int i = 0; i < x; i++)
	{
		int h, w, n;
		scanf("%d%d%d", &h, &w, &n);

		if (n%h ==0) {
			int a = n / h; //È£
			int b = h; // Ãþ
			room = b *100 + a;
			printf("%d\n",room);
		}
		else
		{
			int a = n / h + 1; // È£
			int b = n % h; //Ãþ
			room = b * 100 + a;
			printf("%d\n", room);
		}
	}
	return 0;
}