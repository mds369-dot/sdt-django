# import os
# import django
# from faker import Faker
# import random
# from tasks.models import Employee, Project, Task, TaskDetail

# # Set up Django environment
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
# django.setup()

# # Function to populate the database


# def populate_db():
#     # Initialize Faker
#     fake = Faker()

#     # Create Projects
#     projects = [Project.objects.create(
#         name=fake.bs().capitalize(),
#         description=fake.paragraph(),
#         start_date=fake.date_this_year()
#     ) for _ in range(5)]
#     print(f"Created {len(projects)} projects.")

#     # Create Employees
#     employees = [Employee.objects.create(
#         name=fake.name(),
#         email=fake.email()
#     ) for _ in range(10)]
#     print(f"Created {len(employees)} employees.")

#     # Create Tasks
#     tasks = []
#     for _ in range(20):
#         task = Task.objects.create(
#             project=random.choice(projects),
#             title=fake.sentence(),
#             description=fake.paragraph(),
#             due_date=fake.date_this_year(),
#             status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
#             is_completed=random.choice([True, False])
#         )
#         task.assigned_to.set(random.sample(employees, random.randint(1, 3)))
#         tasks.append(task)
#     print(f"Created {len(tasks)} tasks.")

#     # Create Task Details
#     for task in tasks:
#         TaskDetail.objects.create(
#             task=task,
#             assigned_to=", ".join(
#                 [emp.name for emp in task.assigned_to.all()]),
#             priority=random.choice(['H', 'M', 'L']),
#             notes=fake.paragraph()
#         )
     

    
#     print("Populated TaskDetails for all tasks.")
#     print("Database populated successfully!")

import os
import django
from faker import Faker
import random
from django.contrib.auth.models import User
from tasks.models import Employee, Project, Task, TaskDetail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_management.settings')
django.setup()

fake = Faker()

def create_users(count=10):
    users = []
    for _ in range(count):
        user = User.objects.create_user(
            username=fake.user_name(),
            email=fake.email(),
            password='password123'
        )
        users.append(user)
    return users

def create_employees(count=10):
    employees = []
    for _ in range(count):
        employee = Employee.objects.create(
            name=fake.name(),
            email=fake.email()
        )
        employees.append(employee)
    return employees

def create_projects(count=5):
    projects = []
    for _ in range(count):
        project = Project.objects.create(
            name=fake.bs().capitalize(),
            description=fake.paragraph(),
            start_date=fake.date_this_year()
        )
        projects.append(project)
    return projects

def create_tasks(projects, employees, count=20):
    tasks = []
    for _ in range(count):
        project = random.choice(projects)
        task = Task.objects.create(
            project=project,
            title=fake.sentence(),
            description=fake.paragraph(),
            due_date=fake.date_this_year(),
            status=random.choice(['PENDING', 'IN_PROGRESS', 'COMPLETED']),
            is_completed=random.choice([True, False]),
        )
        # Assign 1-3 random employees to the Task
        selected_employees = random.sample(employees, random.randint(1, 3))
        task.assigned_to.add(*selected_employees)
        tasks.append(task)
    return tasks

def create_task_details(tasks, users):
    for task in tasks:
        # Assign a random User to the TaskDetail's assigned_to field
        user = random.choice(users)
        TaskDetail.objects.create(
            task=task,
            assigned_to=user,  # Using User instance
            priority=random.choice(['H', 'M', 'L']),
            notes=fake.paragraph()
        )

def populate_database():
    print("Generating data...")
    users = create_users(10)
    employees = create_employees(10)
    projects = create_projects(5)
    tasks = create_tasks(projects, employees, 20)
    create_task_details(tasks, users)
    print("Database populated successfully!")

if __name__ == "__main__":
    populate_database()