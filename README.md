# flask-project
## Project Description

In this mini-project, we explore how to effectively work and communicate between different components of a website. The core of our BLOG application is a Python file called APP, which encompasses a wide range of essential functionalities for a website.

With our application, users can easily register, sign in, and publish their own text content. Visitors to the site can access and engage with the posted content. On the main page, we have implemented a feature to display the number of registered users, leveraging the fetch method. Additionally, we have integrated API handling and developed a robust database to securely store user information and content. If a user forgets their password, we will send a password reset email to their registered email address. 🔐

(Although sending passwords via email carries security risks, it is a common practice during development.)

Within a single file, we have successfully implemented both the registration form and login functionality. While we have not prioritized the visual design aspect of the main page, the registration and login page features an appealing and eye-catching layout.

We sincerely hope that our Flask code provides you with valuable insights and enhances your learning experience! 💻

## Installation

To run this project locally, please follow these steps:

1. Clone this repository.
2. Navigate to the project directory.
3. Install the necessary dependencies by running the following command:
<pre>
<code>
```
pip install Flask              # 🌐 Web framework
pip install sqlite3            # 🗃️ SQLite database support
pip install secrets            # 🔒 Generate secure random numbers
pip install smtplib            # 📧 SMTP client library for sending emails
pip install ssl                # 🔐 SSL/TLS support
```
</code>
</pre>

4. Configure the database connection settings in the `config.py` file.
5. Launch the application by running the following command:

   ```
   python app.py
   ```

6. Access the application by visiting `http://localhost:5000` in your web browser.
*You can view the database with TablePlus*

## Usage

1. Register an account on the site by providing the required information.
2. Log in to your account using the registered credentials.
3. Explore the site's features, such as publishing your own text content and interacting with other users' posts.
4. If you forget your password, use the password reset functionality to receive an email with further instructions. 📧

## Contributing

We welcome contributions to enhance the functionality and usability of our project. To contribute, please follow these steps:

1. Fork this repository.
2. Create a new branch.
3. Make your desired changes and improvements.
4. Test the changes thoroughly.
5. Submit a pull request, explaining the purpose and benefits of your changes.

We appreciate your valuable input and are excited to collaborate with you! ✨

