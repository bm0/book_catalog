# docker build -t bm0/bcatalog .

# mkdir -p /var/docker/bcatalog/{data,conf}
# docker run -ti --rm --name bcatalog -p 8000:80 -v /var/docker/bcatalog/data/:/data/ -v /var/docker/bcatalog/conf/:/conf/ bm0/bcatalog

FROM python:alpine3.6
MAINTAINER bm0 <paul0radkov@gmail.com>

EXPOSE 80
VOLUME /data
VOLUME /conf

WORKDIR /opt/book_catalog
COPY . ./

RUN apk --no-cache add nginx libzmq libjpeg-turbo-dev zlib-dev \
    && apk --no-cache add --virtual build-dependencies gcc g++ linux-headers musl-dev \
    && pip install --no-cache-dir pipenv && pipenv install --system --deploy \
    && mkdir -p /run/nginx \
    && apk del build-dependencies

ENTRYPOINT  ["sh", "./bootstrap.sh"]
