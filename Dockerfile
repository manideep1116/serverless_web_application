FROM ubuntu:latest
RUN echo Updating existing packages, installing and upgrading python and pip.
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install --upgrade pip
RUN echo Copying the Flask service into a service directory.
COPY ./service /serverlessService
WORKDIR /serverlessService
RUN echo Installing Python packages listed in requirements.txt
RUN pip install --requirement ./requirements.txt
RUN echo Starting python and starting the Flask service...
ENTRYPOINT ["python"]
CMD ["app.py"]
