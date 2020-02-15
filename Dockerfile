FROM python:3.7-alpine

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN apk add --no-cache --virtual .build-deps \ 
        g++ \
        gcc \
        linux-headers \
        musl-dev \
    && apk add --no-cache dumb-init \
    && pip install -r requirements.txt \
    && apk del .build-deps
COPY . /opt/app

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["python","temp.py"]