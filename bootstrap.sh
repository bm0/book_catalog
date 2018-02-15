#! /bin/bash

if [ ! -f /conf/local_settings.py ]
    then
        cp /opt/book_catalog/project/local_settings.sample.py /conf/local_settings.py
fi

if [ ! -f /conf/nginx.conf ]
    then
        cp /opt/book_catalog/conf/nginx.conf /conf/nginx.conf
fi

if [ ! -f /conf/circus.conf ]
    then
        cp /opt/book_catalog/conf/circus.conf /conf/circus.conf
fi

ln -sf /conf/local_settings.py /opt/book_catalog/project/local_settings.py
ln -sf /conf/nginx.conf /etc/nginx/conf.d/default.conf

nginx
./manage.py migrate
./manage.py loaddata authors books tags
./manage.py collectstatic --noinput
circusd /conf/circus.conf
