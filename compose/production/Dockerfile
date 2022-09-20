FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add --update \
    python3 \
    python3-dev \
    gcc \
    py-pip \
    build-base \
    git \
    wget \
    libxslt-dev \
    xmlsec-dev \
    mariadb-dev \
    libressl-dev \
    libffi \
    cairo-dev \
    pango-dev \
    gdk-pixbuf \
    jpeg-dev \
    zlib-dev \
    freetype-dev \
    lcms2-dev \
    openjpeg-dev \
    tiff-dev \
    tk-dev \
    tcl-dev \
    fontconfig \
    ttf-dejavu

RUN mkdir /backend
WORKDIR /backend

ADD ./backend /backend
RUN pip install -r /backend/requirements/production.txt

EXPOSE 8000
CMD gunicorn -b 0:8000 config.wsgi
