if __name__=='__main__':
    n =int(input())
    student_dic={}
    for _ in range(n):
        name , *line = input().split()
        scores = list(map(float,line))
        student_dic[name]=scores
    # print(student_dic) 
    name_student=input()
    print("{:.2f}".format(sum(student_dic.get(name_student))/3))   