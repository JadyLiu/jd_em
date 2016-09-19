############################################################
# Dockerfile to build Python app
############################################################

FROM python:2.7
MAINTAINER Jady Liu

RUN echo "Docker build is starting"
RUN pip install Flask==0.11.1
WORKDIR /app
COPY . /app
CMD [ "python", "app.py" ]
