FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /var/www/the_rhythm_box
RUN python -m venv venv
COPY requirements.txt requirements.txt
RUN venv/bin/pip install -r requirements.txt
COPY . /var/www/the_rhythm_box

EXPOSE 5002

CMD ["venv/bin/python3", "manage.py", "runserver", "0.0.0.0:5002"]

# base image  
FROM python
# setup environment variable  
ENV DockerHOME=/var/www/the_rhythm_box

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 5002  
# start server  
CMD python manage.py runserver 0.0.0.0:5002
