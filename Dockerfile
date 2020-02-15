FROM python:3.7-alpine

COPY requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app
RUN apk add --no-cache --virtual .build-deps gcc musl-dev
RUN pip install -r requirements.txt
RUN apk del .build-deps gcc musl-dev
COPY . /opt/app

CMD ["python","temp.py"]