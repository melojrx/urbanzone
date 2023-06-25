FROM python:3.8.10

WORKDIR home/ubuntu/maceio-server/urbanZone
COPY requirements.txt  .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir gunicorn

RUN pip install --no-cache-dir --user -r requirements.txt
COPY . .