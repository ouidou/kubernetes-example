## Notre Dockerfile du jour

```Dockerfile
FROM python:3.7-alpine3.8

ENV APP_PORT 8090

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-u", "myapp.py"]
```