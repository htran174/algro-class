#Classwork2 march 8
#Hien Tran

#Greedy algo for sheduling task by earliest deadlines

#num of task

num_tasks =  int(input("Enter the number of tasks: "))

tasks = [] #storing task

#taking user input for task name and deadline
for i in range(num_tasks):
    task_name = input(f"Enter the name of task {i+1}: ")
    deadline = int(input(f"Enter the due date (in days) for task {task_name}: "))
    tasks.append((task_name, deadline))

tasks.sort(key=lambda x: x[1])

#Display the order schedule
print("\nTasks should be performed in the following order(earlist deadline first): ")
for task, deadline in tasks:
    print(f"Tasks: {task}, Deadline: {deadline} days")
