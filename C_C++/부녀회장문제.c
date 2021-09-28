#include <stdio.h>

int main() {

    int x;
    scanf("%d\n", &x);
    int str[x];
    for (int i = 0; i < x; i++) {
        scanf("%d\n", &str[i]);
    }

    printf("%c", str);


    return 0;
}