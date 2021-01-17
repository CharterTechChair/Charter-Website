FROM python:2.7.18

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install -y \
	python-dev \
	libldap2-dev \
	libsasl2-dev \
	libssl-dev \
	libpq-dev \
	gcc

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD scripts/run.sh
