#include <stdio.h>
int result(int k, int n, int r);
int main() {
    int t, k, n, r;
    t = 1; r = 0;
    scanf("%d", &t);
    while (t != 0) {
        scanf("%d\n%d", &k, &n);
        printf("%d\n", result(k, n, r));

        t--;
    }


    return 0;
}
int result(int k, int n, int r) {
    if (k == 1) {
        for (int i = 1; i < n + 1; i++) {
            r += i;
        }
        return r;
    }
    else {
        for (int i = 1; i < n + 1; i++) {
            r += result(k - 1, i, 0);
        }
        return r;
    }
}