#include <stdio.h>

int main(void) {

	// �־��� ������ row�� coulmn �ε����� ���ϸ� ��
	// ���������� �� n(n+1)/2 ���� �� ���� ������
	// ex 4�� =>(1,4) (2,3) (3,2) (4,1)
	// ¦�� �� -> 1���ʿ��� ����, Ȧ�� �� -> 1���ʿ��� ����

	int x;
	scanf("%d", &x);
	int f = 1, i = 1;
	while (1)
	{
		if (x == 1) break;
		else if (i + 1 <= x && x <= f * (f + 1) / 2) break;
		else
		{
			i = f * (f + 1) / 2;
			f += 1;
		}
	}
	//�ش� ������ ���°���� ���ϱ�
	if (f % 2 == 0) {
		int start = f * (f - 1) / 2 + 1;
		int cnt = 1;
		while (1)
		{
			if (start == x) break;
			else {
				cnt++;
				start++;
			}
		}
		int u = 1, d = f; // ¦���� 1�࿡�� �����ϹǷ� ���ڰ� 1, �и� ����
		for (int a = 1; a < cnt; a++)
		{
			u++;
			d--;
		}
		printf("%d/%d", u, d);
	}
	else if (f % 2 != 0)
	{
		int start = f * (f - 1) / 2 + 1;
		int cnt = 1;
		while (1)
		{
			if (start == x) break;
			else {
				cnt++;
				start++;
			}
		}
		int u = f, d = 1; // Ȧ���� 1������ �����ϹǷ� ���ڰ� ����, �и� 1
		for (int a = 1; a < cnt; a++)
		{
			u--;
			d++;
		}
		printf("%d/%d", u, d);
	}
	return 0;

}