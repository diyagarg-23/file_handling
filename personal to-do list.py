#!/usr/bin/env python
# coding: utf-8

# # PERSONAL TO-DO LIST

# In[2]:


#define the file to store tasks

#load tasks from the file
def load_tasks():
    try:
        with open('tasks.txt','r') as file:
            return file.read().splitlines()#read the entire content of file and splits it into list of lines.
    except FileNotFoundError:
        return[]

#save tasks to the file
def save_tasks(tasks):
    with open('tasks.txt','w') as file:
        for task in tasks:
            file.write(task + '\n')
                
#main program loop
def main():
    tasks = load_tasks()
    
    while True: #starts an infinite loop to continuously prompt the user for input
        print('\n1. Add task')
        print('\n2. Remove task')
        print('\n3. View task')
        print('\n4. Exit')
        
        choice = input('select an option (1-4): ')
        
        if choice == '1':
            task = input("enter the task: ")
            tasks.append(task)

            print(f'Task "{task}" added.')
        elif choice == '2':
            task = input('enter the task to remove: ')
            if task in tasks:
                tasks.remove(task)
                print(f'Task "{task}" removed.')
            else:
                print(f'Task "{task}" not found.')
        elif choice == '3':
            print("your tasks: ")
            '''this function adda a counter to the tasks list, returning pairs of the index and corresponding task'''
            for i, task in enumerate(tasks): #this sets up a loop where i is the index(starting from 0) and task is used to display task
                print(f'{i+1}. {task}') #this prints each task with its index starting from 1 instead of 0
                
        elif choice == '4':
            save_tasks(tasks)
            print('Tasks saved. Goodbye!')
            break
        else:
             print("Invalid option. Please try again.")
                
main()


# In[3]:


#nested for
rows = 5
for i in range(1,rows+1):#for rows
    for j in range(0,i):#for columns
        print("*",end=" ")
    print()


# In[4]:


#nested while
t = int(input()) #count numbers for which multiplication table is required
i = 1 #initialization for outer loop
while i<=t: #outer loop to iterate over the count of numbers 
    n = int(input()) #this is for entering number for which multiplication table will be displayed
    j=1 #initialization for inner loop
    while j<=10: #condition of inner loop
        print(n*j)
        j=j+1 #updation for inner loop
    i=i+1 #updation for outer loop


# In[ ]:




