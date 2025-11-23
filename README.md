3D Reconstruction from 2D Image – Web Application

This project is a full-stack web application that allows users to upload a 2D image and visualize its reconstructed 3D model.
The system uses AI-based reconstruction algorithms via Stable Fast API to convert 2D images into 3D, and provides a smooth user experience with features like history tracking, gallery view, and user authentication.

🚀 Features
🔹 1. 2D → 3D Image Reconstruction

Users can upload any 2D image.

The backend sends the image to an AI-powered Stable Fast API.

The system returns and displays the 3D reconstructed output.

🔹 2. User Authentication

Login & Signup pages.

Secure user management using Django with SQL Database.

🔹 3. Conversion History

Each user can view their past 3D conversions.

Stored in the SQL database.

🔹 4. Gallery Section

Displays all previously uploaded and converted images.

Helps users quickly access their past work.

🔹 5. Responsive UI

Built using HTML, CSS, and Django templating engine.

Clean and easy-to-use interface.

🧠 Tech Stack
Frontend

HTML5

CSS3

JavaScript

Django Templates

Backend

Django (Python)

Stable Fast API (AI model for 3D reconstruction)

Python libraries:

Pillow (image processing)

Standard Django modules

Database

SQL (SQLite / MySQL) – used for:

User login / signup

Storing history

Gallery images and metadata

📂 Project Structure
├── 3dreconstruction/
│   ├── settings.py
│   ├── urls.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── signup.html
│   │   ├── history.html
│   │   ├── gallery.html
│   │   └── result.html
│   └── static/
│       ├── css/
│       └── js/
├── media/
│   ├── uploads/
│   └── results/
└── README.md

⚙️ How It Works

User uploads an image through the web interface.

Django backend receives the image and processes it using Pillow.

The image is forwarded to Stable Fast API for 3D reconstruction.

API returns the 3D model or processed image.

Result is stored in the database and displayed to the user.

Users can revisit all results via History or Gallery.

🛠️ Setup Instructions
1. Clone the Repository
git clone https://github.com/yourusername/3d-reconstruction.git
cd 3d-reconstruction

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate        # for Linux/Mac
venv\Scripts\activate          # for Windows

3. Install Dependencies
pip install -r requirements.txt

4. Apply Migrations
python manage.py migrate

5. Run Server
python manage.py runserver

🔐 Environment Variables

Create a .env file to store environment variables such as:

SECRET_KEY=
STABLE_API_KEY=
DATABASE_URL=

🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit pull requests.

📜 License

This project is licensed under the MIT License.

📸 Project Screenshots
![WhyChooseUs](https://github.com/user-attachments/assets/e486c984-567e-46de-9792-208602c98dfd)

