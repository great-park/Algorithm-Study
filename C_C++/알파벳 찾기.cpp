#include <stdio.h>
#include <string.h>

int main() {
    
    int arr1[26];
    int a;
    
    for(int i=0;i<26;i++)
        arr1[i] = -1;
    
    char arr[100];
    scanf("%s", arr);
 
    for(int i=0;i<strlen(arr);i++)
    {
        a = arr[i] - 'a';
        
        if(arr1[a] != -1)
            continue;
        
        arr1[a] = i;
    }
    for(int i = 0;i<26;i++)
    {
        printf("%d ", arr1[i]);
    }
    return 0;
}
