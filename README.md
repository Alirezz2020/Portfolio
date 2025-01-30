# Portfolio Website

This is a personal portfolio website built using **Django**. It showcases projects, about me information, contact form, and a blog where users can view posts and leave messages. The site includes a full CRUD system for posts and a messaging feature. Additionally, it has search functionality, pagination, and integrates **Bootstrap** for styling and responsive design.

### Features
- **Home Page**: Displays a welcome message, list of posts, and pagination.
- **About Page**: A section where you can add information about yourself, including a resume and image.
- **Projects Page**: Showcases your work and projects with details.
- **Contact Page**: Allows users to contact you directly by filling out a form. Includes social media links (**Instagram**, **Telegram**, and **Twitter**) and an option to send messages via email.
- **Search Functionality**: Users can search for posts by title and content.
- **Post Details**: Each post has its own detail page with all the content, including images, videos, and more.
- **Admin Panel**: Fully functional Django Admin Panel to manage posts and contact messages.

### Technologies Used
- **Backend**: Django (**Python** framework)
- **Frontend**: HTML, CSS, JavaScript, **Bootstrap 5**
- **Database**: SQLite (or your choice of database for deployment)
- **Authentication**: Django's built-in authentication system (optional)

### Features in Detail

#### Home Page
- A dynamic home page that welcomes the user and displays a list of blog posts.
- Users can search posts by content or title.
- **Pagination** for blog posts to make navigation easier.

#### About Page
- Contains a section about the developer (you!) and your resume.
- Option to display an image and any personal information you'd like to share.

#### Projects Page
- Display various projects with descriptions, links, or images.
- Organize them by category or date.

#### Contact Page
- Allows visitors to send a message to you directly through a contact form.
- Social media links like **Instagram**, **Telegram**, and **Twitter** (**X**) are included.
- A message is saved in the database so you can review and respond later.

### Setup Instructions

#### Requirements
- **Python 3.x**
- **Django** (Install via `pip install django`)

#### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Alirezz2020/Portfolio.git
    cd Portfolio
    ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run migrations to set up the database:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser to access the Django admin:
    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```bash
    python manage.py runserver
    ```

7. Visit `http://127.0.0.1:8000/` in your browser to see the site.

#### Admin Panel
- To access the admin panel, navigate to `http://127.0.0.1:8000/admin/` and log in using the superuser credentials you created.
- You can manage posts, view contact messages, and more.

### Future Improvements
- Integrate a richer media system for posts (e.g., videos, podcasts).
- Add more dynamic features using **JavaScript** or Django REST Framework for an API.
- Improve form validation and error handling.
- Enhance UI/UX with animations or additional **Bootstrap** components.

### Contributing
Feel free to fork this repository and create a pull request for any improvements or features you'd like to add I am not a frontend guy , if you are, toy are welcomed to show your art.

### License
This project is open-source and available under the **MIT License**.
