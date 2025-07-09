# Kanban Board Backend with Django

This repository contains the backend for a Kanban board project built using Django. It provides RESTful APIs to manage tasks, columns, and boards, enabling seamless task management and organization.

---

## Features

-   Create, read, update, and delete (CRUD) operations for boards, columns, and tasks.
-   RESTful API endpoints for managing Kanban boards.
-   Authentication and authorization for secure access.
-   Scalable and modular codebase.

---

## Prerequisites

Before you begin, ensure you have the following installed:

-   Python 3.8 or higher
-   pip (Python package manager)
-   Git (optional, for version control)

---

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:

    git clone https://github.com/lehmand/Join-Backend.git  
    cd Join-Backend

2. Create a virtual environment:

    python -m venv env    
    source env/bin/activate  # On Windows, use "env/Scripts/activate"

3. Install dependencies:

    pip install -r requirements.txt

4. Run migrations:

    python manage.py makemigrations  
    python manage.py migrate

5. Run server: 

    python manage.py runserver
