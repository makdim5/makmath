# MakMath

This project consists of a Django backend and a React frontend with Vite.

## Running Backend (Django)

1. Create and activate a virtual environment:
   ```
   uv venv
   source .venv/bin/activate
   ```

2. Create .env file from .env.example. The project uses PostgreSQL.

3. Run database migrations:
   ```
   python manage.py migrate
   ```

4. Start the development server:
   ```
   python manage.py runserver
   ```

The backend will be available at http://localhost:8000.

## Running Frontend (React + Vite)

Navigate to the `makmath_frontend` folder and follow the instructions in [README.md](makmath_frontend/README.md).

## Project Structure

- `courses/` - Django app for courses
- `makmat/` - Django project settings
- `makmath_frontend/` - React frontend
- `userswork/` - app for users work