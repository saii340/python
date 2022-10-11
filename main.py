my_list = [1, 2, 2, 4, 4, 5, 6, 8, 10, 13, 22, 35, 52, 83]
list=[]
for i in my_list:
    if i>=10:
       list.append(i)
print(list)
n=int(input())
list=[]
for i in my_list:
    if i>n:
        list.append(i)
print(list)
####output###
[10, 13, 22, 35, 52, 83]
4
[5, 6, 8, 10, 13, 22, 35, 52, 83]


employee = {
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}
employee['job']='software engineer'
del employee['age']
for i in employee:
 print(i, ':' ,employee[i])
###output####
name : Tim
birthday : 1990-03-10
job : software engineer

















