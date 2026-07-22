#Using an official Python Image
FROM python:3.14-slim 

#Set the working directory inside the container
WORKDIR /app

#copy the requirements first
COPY requirements.txt .

#install dependencies
RUN pip install --no-cache-dir -r requirements.txt

#copy the rest of the project
COPY . .

#Expose the port FastAPI uses
EXPOSE 8000

#start the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]