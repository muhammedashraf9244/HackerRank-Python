if __name__ == '__main__':
    student_list=[]
    # enter data from user
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student_list.append([name,score])
    # sort student_list  use lambda x[1] for score but x[0] for name
    student_list.sort(key=lambda x: (x[1],x[0]))
    # print(student_list)
    # get name of students and score of students 
    names_students=[x[0] for x in student_list ]
    score_students=[x[1] for x in student_list]
    lowest_names=[]
    count=1
    while (score_students[0] == score_students[count]):
        count+=1
    lowest_inedx=count
    lowest_names.append(names_students[count])
    length=len(score_students)
    while( count < length and (count+1 != length) ):
        # if count == 1: continue
        if score_students[lowest_inedx]==score_students[count+1]:
            lowest_names.append(names_students[count+1])
        count+=1    
    # sort names
    lowest_names.sort()
    for name in lowest_names:
        print(name)