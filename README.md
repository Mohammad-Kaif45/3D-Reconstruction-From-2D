# 3D RECONSTRUTION FROM 2D

*3D RECONSTRUTION FROM 2D* is a Django-based web application that converts 2D images into 3D models using advanced machine learning and deep learning techniques. The application is designed to be user-friendly, allowing users to easily upload images, confirm conversion, and interact with the generated 3D models.

## Table of Contents

1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Project Structure](#project-structure)
4. [Installation](#installation)
5. [Usage](#usage)

## Features

- *Image Upload:* Users can upload 2D images for processing.
- *3D Conversion:* Converts the uploaded images into 3D models.
- *Model Preview:* Users can preview and interact with the generated 3D models.
- *User-Friendly Interface:* Clean and simple design for easy navigation.

## Tech Stack

- *Backend Framework:* Django
- *Frontend:* HTML, CSS, JavaScript
- *Database:* SQLite 
- *Image Processing:* Pillow
- *3D Conversion:* Stable Fsat API(credit based)
- *Version Control:* Git

## Project Structure

plaintext
3D RECONSTRUTION FROM 2D/
├── manage.py
├── db.sqlite3
├── 3Dreconstructionfrom2D/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── __inti__.py
├── upload/
│   ├── migrations/
│   ├── templates/
│   │   └── upload/
│   │       ├── upload.html
│   │       ├── confirm.html
│   │       ├── 3d.html
│   │       ├── upload_success.html
│   │       └── result.html
│   ├── servicess/
│   │   ├── __init__.py
│   │   ├── converter.py
│   │   └── model.py
│   ├── static/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── apps.py
│   ├── admin.py
│   ├── tests.py
│   ├── forms.py
│   └── ...
└── media/
    ├── models/
    └── uploads/
venv/
├── Include
├── Lib
├── Scripts


## Installation

### Prerequisites

Python 3.x
Django
Pillow

### Steps

1. *Clone the repository:*

   bash
(https://github.com/sampath26082004/3D-Reconstruction-from-2D.git)
cd 3D RECONSTRUTION FROM 2D
   

2. *Create and activate a virtual environment:*

   bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `venv\Scripts\activate`
   

3. *Install the dependencies:*

   bash
   pip install -r requirements.txt
   

4. *Apply migrations:*

   bash
   python manage.py makemigrations
   python manage.py migrate
   

5. *Run the server:*

   bash
   python manage.py runserver
   

6. *Access the application:*
   - Open your browser and go to http://127.0.0.1:8000/.

## Usage

1. *Upload an Image:*
   - Go to the upload page and choose a 2D image to upload.
  
2. *Confirm Conversion:*
   - Review the uploaded image and click the "Convert to 3D" button.

3. *View 3D Model:*
   - Once the conversion is complete, view and interact with the 3D model.


### Test Cases

1. *Image Upload:*
   - *Input:* Valid image file (e.g., .jpg, .png).
   - *Expected Output:* Image is uploaded and stored successfully.

2. *Conversion Confirmation:*
   - *Input:* Confirmation of the uploaded image.
   - *Expected Output:* Image is converted to a 3D model.

3. *3D Model Rendering:*
   - *Input:* View the generated 3D model.
   - *Expected Output:* The model is displayed correctly and is interactive.
3. Commit your changes (git commit -m 'Add some feature').
4. Push to the branch (git push origin feature-branch).
5. Open a pull request.
