# ./Dockerfile 
FROM python:3.8.10
WORKDIR /usr/src/app

## Install packages
COPY requirements.txt ./
RUN pip install -r requirements.txt

## Copy all src files
COPY . .

## Run the application on the port 8080
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]