

if __name__ == '__main__':
    n = int(input())
    country_list=[]
    while n > 0 :
        country_name=input()
        country_list.append(country_name) 
        n-=1
    country_set=set(country_list)
    print(len(country_set))