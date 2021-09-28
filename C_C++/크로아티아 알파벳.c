#include <stdio.h>
#include <string.h>

int main(void)
{
	char str[101];
	scanf("%s", str);

	int len = strlen(str);
	int cnt = 0;

	for (int i = 0; i < len; i++)
	{
		if (str[i] == 'c' && str[i + 1] == '=')
		{
			cnt += 1;
			i += 1; //c= 까지 포함해서 한 단어
		}
		else if (str[i] == 'c' && str[i + 1] == '-')
		{
			cnt += 1;
			i += 1;
		}
		else if (str[i] == 'd' && str[i + 1] == 'z'&& str[i + 2] == '=')
		{
			cnt += 1;
			i += 2;
		}
		else if (str[i] == 'd' && str[i + 1] == '-')
		{
			cnt += 1;
			i += 1;
		}
		else if (str[i] == 'l' && str[i + 1] == 'j')
		{
			cnt += 1;
			i += 1;
		}
		else if (str[i] == 'n' && str[i + 1] == 'j')
		{
			cnt += 1;
			i += 1;
		}
		else if (str[i] == 's' && str[i + 1] == '=')
		{
			cnt += 1;
			i += 1;
		}
		else if (str[i] == 'z' && str[i + 1] == '=')
		{
			cnt += 1;
			i += 1;
		}
		else
		{
			cnt += 1;
		}
	}
	printf("%d", cnt);
	return 0;
}