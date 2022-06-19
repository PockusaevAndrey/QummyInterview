FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY ./entity ./entity
COPY ./handler ./handler
COPY ./repo ./repo
COPY ./server ./server
COPY ./config.py ./
COPY ./main.py ./
COPY ./db ./db
COPY ./sqlite.db ./

CMD [ "python", "./main.py" ]
