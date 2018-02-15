# mkdir -p /var/docker/book_catalog/data
# docker run -ti --rm --name catalog -p 8000:80 -v /var/docker/book_catalog/data/:/data/ bm0/bcatalog-alpine

FROM python:alpine3.6
MAINTAINER bm0 <paul0radkov@gmail.com>

WORKDIR /opt/book_catalog
COPY . ./

EXPOSE 80
VOLUME /data/

RUN apk --no-cache add nginx libzmq libjpeg-turbo-dev zlib-dev \
    && apk --no-cache add --virtual build-dependencies gcc g++ linux-headers musl-dev \
    && pip install --no-cache-dir pipenv && pipenv install --system --deploy \
    && ln -sf /opt/book_catalog/conf/nginx.conf /etc/nginx/conf.d/default.conf; mkdir -p /run/nginx \
    && apk del build-dependencies

CMD ./manage.py migrate; ./manage.py loaddata authors books tags; ./manage.py collectstatic --noinput \
    && nginx; circusd ./conf/circus.conf
