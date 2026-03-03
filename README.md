# Django Todo Application

A simple todo application built with Django that allows users to create, read, update, and delete tasks.

## Features

- **Create Tasks**: Add new tasks with a name and optional description
- **View Tasks**: Display all tasks on a dedicated page
- **Update Tasks**: Edit existing task names and descriptions
- **Delete Tasks**: Remove tasks from the database

## Project Structure

```
todo/
├── todo/                    # Django project configuration
│   ├── settings.py         # Project settings
│   ├── urls.py             # Main URL router
│   ├── wsgi.py             # WSGI configuration
│   └── asgi.py             # ASGI configuration
│
├── todo_app/               # Main Django application
│   ├── models.py           # Task model definition
│   ├── views.py            # View functions
│   ├── urls.py             # App-level URL routing
│   ├── admin.py            # Django admin configuration
│   ├── templates/          # HTML templates
│   │   ├── index.html      # Task creation form
│   │   ├── tasks.html      # Task list view
│   │   └── update_task.html # Task update form
│   └── migrations/         # Django database migrations
│
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
└── README.md              # This file
```

## Requirements

- Python 3.x
- Django 3.x or higher

## Installation & Setup

1. **Navigate to the project directory**:

   ```bash
   cd todo
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**:

   ```bash
   pip install django
   ```

4. **Apply migrations**:

   ```bash
   python manage.py migrate
   ```

5. **Run the development server**:

   ```bash
   python manage.py runserver
   ```

6. **Access the application**:
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

### Create a Task

1. Navigate to the home page (`/`)
2. Fill in the task name and description
3. Click submit to create the task
4. You'll be redirected to the tasks page

### View All Tasks

- Navigate to `/tasks/` to see all created tasks

### Update a Task

1. Click on a task from the tasks list
2. Modify the task name or description
3. Click submit to save changes

### Delete a Task

- Click the delete button next to a task to remove it permanently

## Database Models

### Task Model

```python
class Task(models.Model):
    task_name = models.CharField()          # Task title (required)
    description = models.CharField()        # Task description (optional)
```

## Development Notes

- This project uses SQLite as the default database, suitable for development
- The application follows Django best practices with separated concerns (models, views, templates)
- Template rendering is handled by Django's template engine

## License

This project is open source and available for educational purposes.
