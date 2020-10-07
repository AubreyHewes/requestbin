FROM python:3.8-alpine

RUN apk update && apk upgrade && \
    apk add \
        build-base \
        py3-gevent \
        py3-greenlet \
        libffi-dev \
        # file
        file \
    && rm -rf /var/cache/apk/* 
# want all dependencies first so that if it's just a code change, don't have to
# rebuild as much of the container
ADD requirements.txt /opt/requestbin/
RUN pip install -r /opt/requestbin/requirements.txt \
    && rm -rf ~/.pip/cache

# the code
ADD requestbin  /opt/requestbin/requestbin/

EXPOSE 8000

WORKDIR /opt/requestbin
ENV PYTHONPATH=/usr/lib/python3.8/site-packages
CMD gunicorn -b 0.0.0.0:8000 --worker-class gevent --workers 2 --max-requests 1000 requestbin:app


