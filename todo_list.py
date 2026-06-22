# ----------------------------------------
# CODSOFT Python Programming Internship
# Task 1: To-Do List Application
#
# Description:
# This application allows users to manage their daily tasks.
# Users can add tasks, view tasks, and remove completed tasks.
# The project demonstrates the use of lists, loops,
# conditional statements, and user input in Python.
#
# Developed by: Devyani Verma
# ----------------------------------------
1tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")

    elif choice == "4":
        print("Thank you for using To-Do List.")
        break

    else:
        print("Invalid choice!")