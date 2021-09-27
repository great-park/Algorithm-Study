a =int(input())
num_list = []

for i in range(a):
    s = int(input())
    num_list.append(s)


def find_max_sub(arr,low,high):
    if high == low:
        return (low,high,arr[low])
    else:
        middle = int((low+high)/2)
        (left_low,left_high,left_sum) = find_max_sub(arr,low,middle)
        (right_low, right_high, right_sum) = find_max_sub(arr, middle+1,high)
        (cross_low,cross_high,cross_sum)= find_max_cross_sub(arr, low, middle, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            return (left_low,left_high,left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return (right_low, right_high, right_sum)
        else: return (cross_low,cross_high,cross_sum)
def find_max_cross_sub(arr, low, middle, high):
    left_sum = -999999
    sum =0
    for i in range(middle,low-1,-1):
        sum = sum + arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i
    right_sum = -999999
    sum =0
    for j in range(middle+1, high+1):
        sum = sum + arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return (max_left,max_right,left_sum+right_sum)

x = find_max_sub(num_list,0,a-1)
for i in range(3):
    print(x[i])
