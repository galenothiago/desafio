FROM python:3.8

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

COPY hello.py .

# install dependencies
RUN pip install -r requirements.txt

# copy the content of the local src directory to the working directory

# command to run on container start
CMD [ "python", "./hello.py" ]