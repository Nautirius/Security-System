# Security System
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,docker,python,django,pytorch,tailwind" />
  </a>
</p>

___


### Project description

The project is a comprehensive security and access management system designed to help enterprises
efficiently control and monitor their facilities, users, and security assets. It integrates user 
authentication, role-based access control (RBAC), surveillance camera management, and facial recognition
to ensure high-security standards and streamlined administration.
This system is particularly useful for companies managing multiple buildings, restricted zones,
and large user bases, where security automation, controlled access, and real-time monitoring are critical.
By leveraging modern authentication mechanisms, including OAuth2 with third-party integrations
(Google, GitHub), and advanced AI-driven facial recognition, the platform ensures both security and
convenience.

Our project focuses on developing an efficient AI-based security system designed specifically for office
spaces. By leveraging facial and silhouette recognition, the system verifies employee identities at various
access points throughout a facility, creating a secure and streamlined process for managing entry
and monitoring activities. The primary aim is to establish a robust, real-time, automated verification
system that safeguards access to restricted areas.


The link below provides a brief demo in the form of a guided walkthrough of the user interface:

> Youtube video [link](https://www.youtube.com/watch?v=4WMYv0wn8rE)

### Authors

| Name               | GitHub Profile                                |
|--------------------|-----------------------------------------------|
| Andrzej Świętek    | [GitHub Profile](https://github.com/Andrzej-Swietek)   |
| Marcin Knapczyk    | [GitHub Profile](https://github.com/Nautirius)|
| Bartosz Biesaga    | [GitHub Profile](https://github.com/Bartosz-Biesaga)   |
| Mateusz Wawrzyczek | [GitHub Profile](https://github.com/MateuszWawrzyczek)   |


### Docker Ports

| Service            | GitHub Profile                                         |
|--------------------|--------------------------------------------------------|
| Django             | :8000                                                  |
| Postgres           | :5432                                                  |


### Starting app
#### Feature extraction:
Feature extraction tested only locally so far.
Feature extraction tested using python 3.10.11 available at
https://www.python.org/downloads/release/python-31011/.
Build python 3.10.11 after installing following libraries:
```shell
sudo apt-get install libbz2-dev
sudo apt-get install lzma
sudo apt-get install liblzma-dev
```
otherwise errors may occur.
```shell
python3.10 -m venv venv
source venv/bin/activate
pip3.10 install -r requirements_pytorch_no_deps.txt --no-deps
pip3.10 install -r requirements_no_deps.txt --no-deps
pip3.10 install -r requirements.txt
```
#### Locally:
```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

#### Docker
```shell
docker compose up --build -d
```


#### Run migrations in docker container

```shell
docker exec -it web python manage.py migrate
docker exec -it web python manage.py createsuperuser
docker exec -it web python manage.py runserver 0.0.0.0:8000
```

### Creating new Migrations
```shell
python manage.py makemigrations [app_name] --name [migration_name] --empty
```
Example:
```shell
python manage.py makemigrations authentication --name add_pgvector --empty
```

### Execute Migrations
```shell
python manage.py migrate
```

### Reset DB
```shell
python manage.py flush
```

### Create new application module
```shell
python manage.py startapp [app_name]
mv [app_name] apps/
```
then change `apps.py` file inside newly created app

Example
```python
class RecognitionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "recognition"
```
to
```python
class RecognitionConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.recognition"
```

### Folder structure

```

.
├── apps
│   ├── authentication
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── guards
│   │   │   ├── __init__.py
│   │   │   ├── user_company_required.py
│   │   │   ├── user_membership_role.py
│   │   │   └── user_permition_required.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_add_pgvector.py
│   │   │   ├── 0002_initial.py
│   │   │   ├── 0003_userprofile_city_userprofile_street_and_more.py
│   │   │   ├── 0004_userprofile_user.py
│   │   │   ├── 0005_alter_userprofile_email.py
│   │   │   ├── 0006_alter_userimage_user.py
│   │   │   ├── 0007_membership_userprofile_companies.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── signals.py
│   │   ├── storage.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── buildings
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_rename_company_id_building_company_and_more.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── cameras
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_camerafeed_camerafeed_unique_feed_per_camera.py
│   │   │   ├── 0003_camerafeed_authorized.py
│   │   │   ├── 0004_camerafeed_detected_user.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── companies
│   │   ├── migrations
│   │   │   └── __pycache__
│   │   │       ├── __init__.cpython-310.pyc
│   │   │       ├── __init__.cpython-313.pyc
│   │   │       └── __init__.cpython-39.pyc
│   │   └── __pycache__
│   ├── permissions
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── 0002_alter_permission_options_and_more.py
│   │   │   ├── 0003_alter_permission_users_alter_permission_zones.py
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── recognition
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── feature_extraction
│   │   │   ├── crowdpose.py
│   │   │   ├── default_runtime.py
│   │   │   ├── face_feature_extarction_model.py
│   │   │   ├── feature_extraction_model.py
│   │   │   ├── __init__.py
│   │   │   ├── pose_feature_extraction_model.py
│   │   │   └── rtmo-l_16xb16-700e_body7-crowdpose-640x640.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   └── user_management
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── __init__.py
│       ├── migrations
│       │   └── __init__.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── core
│   ├── asgi.py
│   └── __init__.py
│   ├── settings.py
│   ├── templatetags
│   │   ├── custom_tags.py
│   │   └── __init__.py
│   ├── urls.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── singleton.py
│   ├── views.py
│   └── wsgi.py
├── db.sqlite3
├── docker
│   └── backend
│       └── Dockerfile
├── docker-compose.yml
├── logging.conf
├── logs
│   └── django.log
├── manage.py
├── media
│   └── camera_feeds
│       ├── face
│       │   ├── Administration_Camera_face.jpg
│       │   ├── Entry_Camera_face.jpg
│       │   ├── Google_Lobby_Camera_face.jpg
│       │   ├── Google_Server_Room_face.jpg
│       │   ├── Offices_Camera_face.jpg
│       │   └── test_Camera_face.jpg
│       └── silhouette
│           ├── Administration_Camera_silhouette.jpg
│           ├── Entry_Camera_silhouette.jpg
│           ├── Google_Lobby_Camera_silhouette.jpg
│           ├── Google_Server_Room_silhouette.jpg
│           ├── Offices_Camera_silhouette.jpg
│           └── test_Camera_silhouette.jpg
├── README.md
├── Recognition_Using_Face_And_Body.pdf
├── requirements_no_deps.txt
├── requirements_pytorch_no_deps.txt
├── requirements.txt
├── scripts
│   ├── feature_extraction
│   │   ├── crowdpose.py
│   │   ├── default_runtime.py
│   │   ├── feature_extraction.py
│   │   ├── __init__.py
│   │   └── rtmo-l_16xb16-700e_body7-crowdpose-640x640.py
│   └── init.sql
├── static
│   ├── css
│   │   └── main.css
│   └── favicon.svg
├── storage
│   └── user_6
│       ├── face
│       │   ├── face-1.jpg
│       │   ├── face-2.jpg
│       │   ├── face-3.jpg
│       |   └── face-4.jpg
│       └── silhouette
│           ├── body-1.jpg
│           ├── body-2.jpg
│           ├── body-3.webp
│           └── body-4.jpg
└── templates
    ├── 403_csrf.html
    ├── 403.html
    ├── account
    │   ├── login.html
    │   ├── password_reset.html
    │   └── signup.html
    ├── base.html
    ├── buildings
    │   ├── building
    │   │   ├── building_create.html
    │   │   ├── building_list.html
    │   │   ├── building_update.html
    │   │   └── home.html
    │   ├── company
    │   │   ├── assign_user_to_company.html
    │   │   ├── company_by_id.html
    │   │   ├── company_create.html
    │   │   ├── company_list.html
    │   │   ├── company_update.html
    │   │   └── home.html
    │   ├── home.html
    │   └── zone
    │       ├── home.html
    │       ├── zone_create.html
    │       ├── zone_list.html
    │       └── zone_update.html
    ├── cameras
    │   ├── camera_create.html
    │   ├── camera_feed_grid.html
    │   ├── camera_feed_upload_error.html
    │   ├── camera_feed_upload.html
    │   ├── camera_list.html
    │   ├── camera_update.html
    │   └── home.html
    ├── dashboard.html
    ├── index.html
    ├── layouts
    │   └── dashboard_layout.html
    ├── partials
    │   ├── clickable_card_2.html
    │   ├── clickable_card.html
    │   ├── dashboard-header.html
    │   ├── navbar.html
    │   └── sidebar.html
    ├── permissions
    │   ├── permission_form.html
    │   ├── permission_home.html
    │   ├── permission_list.html
    │   ├── permission_list_users.html
    │   └── permission_list_zones.html
    ├── search.html
    ├── user
    │   ├── upload_profile_photos_failure.html
    │   ├── upload_profile_photos.html
    │   ├── upload_profile_photos_success.html
    │   └── user_uploaded_photos.html
    └── user_management
        ├── create_user.html
        ├── home.html
        ├── list_users.html
        ├── update_user.html
        └── user_details.html
```

- `apps/` - Custom Django applications specific to this project.

  - `authentication/` - Handles user authentication, including forms, models, and views.

  - `buildings/` - Manages building-related data and operations.

  - `cameras/` - Manages camera feeds and related functionalities.

  - `companies/` - Stores and handles company-related data.

  - `permissions/` - Manages user permissions and roles.

  - `recognition/` - Contains feature extraction models for face and body recognition.

  - `user_management/` - Handles user profiles, forms, and management views.

- `core/` - Core configuration and utility functions for the project.

  - `templatetags/` - Custom Django template tags.

  - `utils/` - Utility functions, such as singleton pattern implementation.

- `static/` - Folder containing static files such as CSS, JavaScript, and images.

- `templates/` - Template directory for storing HTML templates.

- `media/` - Directory for storing user-uploaded media files, including camera feeds.

- `migrations/` - Auto-generated database migration files for each app.

- `logs/` - Stores log files, such as Django application logs.

- `docker/` - Contains Docker-related configurations.

- `scripts/` - Stores scripts for feature extraction and database initialization.

- `storage/` - Directory for user-related stored images and data.

- `tests/` - Unit and integration tests for the project.
