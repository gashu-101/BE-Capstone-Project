# 📱 Social Media API with Django

Welcome to the **Social Media API** project built using **Django** and **Django REST Framework**. This API allows users to create posts, follow/unfollow other users, and view a personalized feed! 🚀

## 🎯 Features

- 📝 **Create Posts**: Users can create posts with text content and optional media links.
- 👥 **Follow/Unfollow Users**: Users can follow or unfollow other users.
- 📰 **Feed**: Users can view a feed of posts from the people they follow.
- ⚙️ **Django Admin**: Manage users, posts, and follows through the Django admin panel.

## 🛠️ Installation and Setup

Follow these steps to get the project up and running on your local machine:

### 1. Clone the Repository

```bash
git clone <repository-url>
cd socialmedia_api
```

### 2. Install Dependencies

Make sure you have **Python** and **pip** installed. Then, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Configure the Database

By default, the project uses **SQLite**. If you want to use a different database, update the `DATABASES` setting in `socialmedia_api/settings.py`.

### 4. Apply Migrations

Run the following commands to create the necessary database tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create a Superuser

To manage the app via Django admin, create a superuser account:

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

Finally, start the Django development server:

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`.

## 🚪 Endpoints

Here are the available API endpoints:

| Endpoint                      | Method | Description                      |
| ----------------------------- | ------ | -------------------------------- |
| `/social/posts/`              | GET    | List all posts                   |
| `/social/posts/`              | POST   | Create a new post                |
| `/social/follow/<user_id>/`   | POST   | Follow a user                    |
| `/social/unfollow/<user_id>/` | POST   | Unfollow a user                  |
| `/social/feed/`               | GET    | View posts from users you follow |

## 🛠️ Project Structure

```
socialmedia_api/
    ├── socialmedia_api/
    │   ├── settings.py      # Project settings
    │   ├── urls.py          # Project URL configurations
    ├── social/
    │   ├── models.py        # Post and Follow models
    │   ├── serializers.py   # DRF serializers for Post and Follow
    │   ├── views.py         # API views for post, follow, unfollow, and feed
    │   ├── urls.py          # App URL configurations
    ├── manage.py            # Django management script
```

## 🛠️ Dependencies

- **Django**: 4.0+
- **Django REST Framework**: 3.12+

You can install these using `pip install -r requirements.txt`.

## 🚀 Future Enhancements

Some ideas to improve the API further:

- 🔑 **Add Authentication**: Implement token-based or session authentication.
- 💬 **Comment System**: Allow users to comment on posts.
- ❤️ **Likes**: Enable users to like posts.
- 🔔 **Notifications**: Notify users when they get followed or receive a new post in their feed.

## 📝 License

This project is licensed under the MIT License.

Thanks for checking out this project! ✨ Feel free to contribute or reach out if you have any questions. 😊

```

```
