# the second maximum is runner up
if __name__ == '__main__':
    n = int(input())
    # for enter input as 1 2 3 10 ...
    arr = map(int, input().split())
    # print(arr,type(arr)) # arr is map object
    arr_list=list(arr)
    arr_list.sort()
    # print(arr_list)
    runner_up_number=len(arr_list)-2
    count=len(arr_list)-1
    while arr_list[runner_up_number] == arr_list[count]:
        runner_up_number-=1
        count-=1
    print(arr_list[runner_up_number])    