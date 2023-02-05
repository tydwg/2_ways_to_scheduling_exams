import itertools
import math
import time
with open(r"C:\Users\DELL\data.txt") as f:
        n = int(f.readline())
        students = [int(x) for x in f.readline().split()]
        m = int(f.readline())
        room_capacity = [int(x) for x in f.readline().split()]
        k = int(f.readline())
        conf = []
        for i in range(k):
            conf.append([int(x) for x in f.readline().split()])
        print("read file done")
        f.close()
# create list of subjects

N = [i for i in range(1,n+1)]

#No conflict pairs

def consistent(x):
    for (i,j) in conf:                        
        if i not in x or j not in x:
            continue
        if i in x and j in x:
            return False
    return True

#check to see if the subject has any students who have not yet taken the exam.

def students_check(x):
    for sub in x:
        if students[sub-1] != 0:
            continue
        if students[sub-1] == 0:
            return False
    return True

#create feasible ways to arrange for a period using itertools (Bruteforce)

res = []
total = []
for i in range(1, m + 1):
    total += itertools.permutations(N, i)
total.reverse()

#take the most subjects ways that is available and put into result list (Greedy)

time_start = time.time()
for i in total:
    room_taken = [0] * m
    if consistent(i) and students_check(i):
        for j in i:
            if room_capacity[i.index(j)] >= students[j-1] and room_taken[i.index(j)] == 0:
                students[j-1] = 0
                room_taken[i.index(j)] = 1
                print(students)

            elif room_capacity[i.index(j)] < students[j-1] and room_taken[i.index(j)] == 0:
                students[j-1] -= room_capacity[i.index(j)]
                room_taken[i.index(j)] = 1
                print(students)
                
        res.append(i)

#if there are too few seats and there are students still haven't taken the exam after the exam

def final_results(x):
    if sum(x) != 0:
        return ("Need more rooms or too few seats/room")
    else:
        minimum_days = math.ceil(len(res) / 4)
        return ("The exam schedule will be held " + str(minimum_days) + " day(s)")

time.sleep(1) 
time_end = time.time() 
time_taken = time_end - time_start

print("Time:" + str(time_taken))
print(res)
print(final_results(students))
            



