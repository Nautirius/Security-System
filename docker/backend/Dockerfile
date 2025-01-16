FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/
COPY requirements_no_deps.txt /app/
COPY requirements_pytorch_no_deps.txt /app/

RUN apt-get update
RUN apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libbz2-dev \
    lzma \
    liblzma-dev \
    && apt-get clean


RUN pip install --no-cache-dir -r requirements_pytorch_no_deps.txt --no-deps
RUN pip install --no-cache-dir -r requirements_no_deps.txt --no-deps
RUN pip install --no-cache-dir -r requirements.txt


COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]