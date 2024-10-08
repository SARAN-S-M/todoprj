# Django To-Do Application

This is a simple To-Do application built using Django, where users can create, view, and delete tasks. The application uses HTML templates for rendering views.

## Features

- Add new tasks
- Mark tasks as completed
- Delete tasks
- List all tasks

## Technologies Used

- **Django**: A high-level Python web framework that encourages rapid development and clean, pragmatic design.
- **HTML**: For creating the templates and rendering the user interface.
- **CSS**: For styling the application and making it visually appealing.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- Django 4.x (or the version you're using)
- Git

### Installation

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
1. Clone the repository:</div>

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
2. Create a virtual environment:</div>

```bash
python -m venv env
```

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
3. Activate the virtual environment:</div>

On Windows:
```bash
env\Scripts\activate
```

On macOS/Linux:
```bash
source env/bin/activate
```

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
4. Install the dependencies:</div>

```bash
pip install -r requirements.txt
```

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
5. Apply the migrations:</div>

```bash
python manage.py migrate
```

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
6. Run the development server:</div>

```bash
python manage.py runserver
```

<div style="border:1px solid black; display:inline-block; padding:5px; border-radius:3px;">
7. Open your browser and navigate to:</div>

```bash
http://127.0.0.1:8000/
```

## File Structure

- **todoapp/**: Contains the Django application.
  - **templates/**: Holds the HTML files used for rendering the views.
  - **models.py**: Defines the Task model.
  - **views.py**: Contains the logic for handling requests and returning responses.
  - **urls.py**: Maps URLs to views.
- **db.sqlite3**: SQLite database to store tasks.


# Usage
 - **Home Page**: Displays the list of tasks. You can add new tasks by entering them in the input box and clicking "Add".
 - **Delete Task**: Click on the delete icon to remove a task from the list.
 - **Mark as Completed**: Click the checkbox next to a task to mark it as completed.

# Future Enhancements

 - Enable task prioritization and categorization.
 - Implement task deadlines and reminders.

# Contributing
Feel free to fork this project and submit pull requests if you'd like to contribute.

# License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

You can find my contact details in my profile.

- **LinkedIn**: [Saran S M](https://www.linkedin.com/in/saran-s-m/)
- **GitHub**: [SARAN-S-M](https://github.com/SARAN-S-M)