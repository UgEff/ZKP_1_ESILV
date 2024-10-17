#Use an official Python runtime as a parent image
FROM python:3.7-slim

#TODO
# Set the working directory to /app
WORKDIR /app

#COPY THE REQUIRED FILES
COPY requirement.txt requirement.txt
COPY schnorr_server.py schnorr_server.py

#INSTALL THE REQUIRED PACKAGES
RUN pip install --no-cache-dir -r requirement.txt

#Expose the port
EXPOSE 5000

#Run the application
CMD ["python", "schnorr_server.py"]
