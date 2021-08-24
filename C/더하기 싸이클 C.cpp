#include<stdio.h>

int main()
{
    int x=26;
    
    scanf("%d", &x);
    int temp = x;
    int cnt = 0;
    
    do
    {
        if (temp < 10){
            temp *= 11;
            cnt ++;
        }
        else{
            int temp_f = temp /10;
            int temp_b = temp %10;
            int new_num = temp_f + temp_b;
            
            if(new_num < 10){
                temp = new_num + temp_b*10;
            }
            else{
                temp = new_num%10 + temp_b*10;
            }
            cnt++;
        }
    } while ( temp != x);
    
    printf("%d",cnt);

    return 0;
}

