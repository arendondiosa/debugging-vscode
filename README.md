# Introduction to debugging using VSCode

Some examples using different packages: Flask and Django.

## Requirements

- Python >= 3.6

## Installation

```bash
pip install -r requirements.txt
```

## Run

### Flask app

Execute the application using Flask

```bash
cd flask_app
python app.py
```

Expected output: The application is running on port 5000

```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

### Django app

Before execute the application, it's necessary to update the migrations

```bash
cd django_app
python manage.py migrate
```

Create an Admin user

```bash
python manage.py createsuperuser
```

Execute the application using Django


```bash
python manage.py runserver
```

Expected output: The application is running on port 8000

```bash
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 15, 2021 - 02:43:54
Django version 3.1.7, using settings 'django_app.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

### Scripts

```bash
cd scripts
python calculator.py
```
