## Features

- **View Students:** An elegant, responsive data table displaying student details (Name, Email, Course, Marks). marks accurately report passing or failing logic with color-coded numbers.
- **Add New Students:** A clean, validated form to register new students.
- **Edit Students:** Easily update a student's information.
- **Delete Students:** Seamless one-click deletion with a safety prompt.
- **Dynamic Messaging:** Receive clear, responsive success/error notifications after taking actions.

## Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package installer)

## Installation & Setup

Follow these steps to get the project running locally on your machine.

**1. Clone or download the repository**

Navigate to the project folder (`student_portal`) where the `manage.py` file is located.

**2. Create a Virtual Environment (Optional but Recommended)**
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

**3. Install Dependencies**
Install Django if you haven't already:
```bash
pip install django
```

**4. Set up the Database**
Apply the migrations to configure your local SQLite database:
```bash
python manage.py makemigrations
python manage.py migrate
```

## Running the Application

Once your database is fully set up, you can start the local development server:

```bash
python manage.py runserver
```

Open your web browser and navigate to the application:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

## Usage Guide

1. **Dashboard:** You will land on the main data table showing the roster of students.
2. **Add a Student:** Click the primary blue bounded **"Add Student"** button at the top right of the application to fill in info for a new user. 
3. **Updating Records:** To change an existing student's data, hit the **"Edit"** button alongside their name in the designated row.
4. **Deleting Records:** Hit the red **"Delete"** button to remove a student and observe the changes reflect immediately on the dashboard. 

## Technology Stack

- **Backend:** Python / Django
- **Database:** SQLite3 (Django's default)
- **Frontend UI:** HTML5, CSS3, Ant Design (via CDN)
