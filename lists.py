#!/usr/bin/python3
if __name__ == '__main__':
    N = int(input())
    l_list = []
    for _ in range(N):
        command = input().split()
        if command[0] == 'print':
            print(l_list)
        elif command[0] == 'insert':
            command[1] = int(command[1])
            command[2] = int(command[2])
            l_list.insert(command[1], command[2])
        elif command[0] == 'remove':
            command[1] = int(command[1])
            l_list.remove(command[1])
        elif command[0] == 'append':
            command[1] = int(command[1])
            l_list.append(command[1])
        elif command[0] == 'sort':
            l_list.sort()
        elif command[0] == 'pop':
            l_list.pop()
        elif command[0] == 'reverse':
            l_list.reverse()
    
    print(hash(l_list))
    
                     
