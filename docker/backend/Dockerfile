FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
COPY requirements_no_deps.txt /app/
COPY requirements_pytorch_no_deps.txt /app/

RUN pip install --no-cache-dir -r requirements_pytorch_no_deps.txt --no-deps
RUN pip install --no-cache-dir -r requirements_no_deps.txt --no-deps
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]