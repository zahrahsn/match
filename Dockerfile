FROM python:3-buster

RUN apt update && apt install -y build-essential

WORKDIR /web

COPY . .
RUN pip install -r requirements.txt

CMD ["python","manage.py","runserver","0.0.0.0:8000","--noreload"]
