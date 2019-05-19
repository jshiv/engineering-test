FROM python:3.6
RUN apt-get update
COPY . /app
WORKDIR /app/app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "--bind=0.0.0.0","--workers=4", "service:app"]
