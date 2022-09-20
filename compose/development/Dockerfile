FROM python:3.9-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /backend
WORKDIR /backend

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
    openssl \
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

COPY ./backend/requirements/ /backend/requirements
RUN pip install -r /backend/requirements/development.txt
