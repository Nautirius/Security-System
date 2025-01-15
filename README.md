# Security System
<p align="center">
  <a href="https://skillicons.dev">
    <img src="https://skillicons.dev/icons?i=git,docker,python,django,pytorch,tailwind" />
  </a>
</p>

___

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
pip3.10 install -r requirements_pytorch.txt
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