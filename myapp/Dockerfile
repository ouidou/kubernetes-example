FROM python:3.7-alpine3.8

#REPOSITORIES=docker.ouidou.fr/meetkube/myapp
#TAGS=0.5

ENV APP_PORT 8090

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "myapp.py"]
