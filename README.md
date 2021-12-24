<div id="top"></div>

<!-- PROJECT Intro -->
<br />
<div align="center">
  <a href="">
    <img src="https://mediusware.com/wp-content/uploads/2021/02/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Coding Test - Mediusware Ltd.</h3>

</div>

### Note

I have used Ubuntu 20.04 LTS. This documentation is made for that. For windows or mac you may need to change some staffs if needed but the steps will be the same as follows.

### Prerequisites

Here, I have used React.js as frontend and Django as backend. So, you must have to install the following before running the project.

- node
- python
- pip
- virtualenv

### Usages

1. Clone the repository

   ```sh
   https://github.com/hrid0ybd/coding-test-mediusware.git

   ```

2. Open this project in your favourite IDE. In my case, I have used [Visual Studio Code](https://code.visualstudio.com/download)

3. Go to the terminal and activate virtual env.

4. Simply install all the backend requirements using this command from the project root folder.

   ```sh
   pip install -r requirements.txt
   ```

5. Go the the frontend folder and install NPM packages

   ```sh
   cd frontend

   npm install
   ```

6. Then build the project from frontend folder.

   ```sh
   npm run build
   ```

7. Go to the backend folder.

   ```sh
   cd ..
   cd backend
   ```

8. Migrate database.

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

9. Create superuser for the admin access.

   ```sh
   python manage.py createsuperuser
   ```

10. Run the server to see the frontend works. (It takes you to the given host http://127.0.0.1:8000/)

    ```sh
    python manage.py runserver
    ```

11. Go to the admin panel by providing your superadmin credentials.

    ```sh
    http://127.0.0.1:8000/admin/
    ```

Now you are good to see this project. Happy Coding 👨‍💻

<p align="right">(<a href="#top">Back to top</a>)</p>
