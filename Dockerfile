# base image  
FROM python:3.8-slim
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

RUN apt-get update && apt-get install -y curl --no-install-recommends && rm -rf /var/lib/apt/lists/*

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD curl -f http://localhost:5002/ || exit 1

# start server
CMD ["gunicorn", "rhythmbox.wsgi:application", "-b", "0.0.0.0:5002", "--access-logfile", "-", "--error-logfile", "-"]
