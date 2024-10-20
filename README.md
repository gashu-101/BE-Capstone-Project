# 🌐 Social Media API

## 📜 Project Overview

This project is a Social Media API built using Django and Django REST Framework (DRF). It allows users to create, update, delete posts, follow other users, and view a feed of posts from the users they follow. The project simulates a real-world social media environment focusing on CRUD operations, user relationships, and efficient data handling.

## 🚀 Features

### 1. 📝 Post Management (CRUD)

- Users can create, read, update, and delete posts.
- Each post contains:
  - **Content** (required text)
  - **User** (author of the post)
  - **Timestamp** (auto-generated)
  - **Optional Media** (e.g., image URLs 🖼️)
- Posts can only be updated or deleted by the user who created them.
- Validation is in place for required fields like `Content` and `User`.

### 2. 👤 User Management (CRUD)

- Users can register, log in, and manage their accounts.
- Each user has:
  - **Username** (unique ✨)
  - **Email** (unique 📧)
  - **Password** (secure 🔒)
  - Optional **Profile Fields** such as Bio 📝 and Profile Picture 📷.
- Only authenticated users can create, update, or delete posts.

### 3. 🔄 Follow System

- Users can follow and unfollow others 🔔.
- A user cannot follow themselves 🚫.
- Follow relationships are stored and managed efficiently.

### 4. 📰 Feed of Posts

- Users can view a feed of posts from the users they follow.
- Posts in the feed are displayed in reverse chronological order (newest first ⏳).
- Optionally, users can filter the feed by date 📅 or search posts by keywords 🔍.

## ⚙️ Technical Requirements

### 🗄️ Database

- The API uses Django ORM to manage the database.
- **Models**:
  - `User`: Manages user information and profile fields.
  - `Post`: Stores post content, author, and timestamp.
  - `Follower`: Tracks relationships between users (followers/following).

### 🔑 Authentication

- User authentication is managed using Django’s built-in system 🔐.
- Optionally, token-based authentication (JWT) is supported for secure access.

### 🛠️ API Design

- The API follows RESTful principles, with appropriate HTTP methods for each operation:
  - `GET`, `POST`, `PUT`, `DELETE`
- Error handling is implemented with relevant HTTP status codes 🛑.

### 🌍 Deployment

- The API is deployed on a platform like Heroku 🚀 or PythonAnywhere 🖥️.
- Ensure the API is secure 🔒 and performs well 🚀.

### 🔄 Pagination and Sorting

- Pagination 📄 is added to the post feed for users with large numbers of followed users or posts.
- Sorting options like sorting by Date 📅 or Popularity ⭐ are available.

## 🌟 Stretch Goals (Optional)

- **❤️ Likes and Comments**: Users can like ❤️ and comment 💬 on posts.
- **🔔 Notifications**: Users are notified when someone follows them, likes their post, or comments on it.
- **📩 Direct Messaging**: Allows private messaging between users.
- **🔄 Post Sharing**: Users can share or "repost" content.
- **🏷️ Hashtags and Tagging**: Users can tag others or use hashtags #️⃣.
- **🔥 Trending Posts**: Displays popular posts based on likes or reposts.
- **🛠️ Profile Customization**: Users can add fields like Location 📍 and Cover Photo 🖼️.
- **📷 Media Uploads**: Supports media file uploads (images, videos) to a cloud service like AWS S3 ☁️.

## 🛠️ How to Run the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/gashu-101/BE-Capstone-Project.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the server:

   ```bash
   python manage.py runserver
   ```

6. Access the API at `http://127.0.0.1:8000/`.

## 🚀 Deployment

To deploy on Heroku:

1. Set up your Heroku project.
2. Add necessary environment variables for your database and secret key.
3. Deploy your code to Heroku.

## 📄 License

This project is licensed under the MIT License.
