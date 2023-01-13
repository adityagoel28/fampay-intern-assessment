FROM python:3.8-slim-buster

ARG name
ENV SECRET_KEY $SECRET_KEY
ENV YOUTUBE_API $YOUTUBE_API
ENV YOUTUBE_API2 $YOUTUBE_API2
ENV YOUTUBE_API3 $YOUTUBE_API3
ENV YOUTUBE_API4 $YOUTUBE_API4

# Move to working directory /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]