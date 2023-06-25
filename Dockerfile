FROM python:3.8.10

WORKDIR home/ubuntu/maceio-server/urbanZone

RUN python -m venv venv

ENV PATH="/home/ubuntu/maceio-server/urbanZone/venv/bin:$PATH"

COPY requirements.txt  .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir gunicorn

RUN pip install --no-cache-dir --user -r requirements.txt
COPY . .