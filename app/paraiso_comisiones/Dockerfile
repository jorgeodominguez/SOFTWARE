FROM debian:bullseye-slim
# FROM python:3.11.0-slim-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y \
    apache2 \
    python3 \
    python3-pip \
    python3-dev \
    libmariadb-dev \
    libapache2-mod-wsgi-py3 \
    pkg-config \
    gcc 

# Configure timezone
ENV TZ=America/Mexico_City
RUN ln -snf  /etc/l/usr/share/zoneinfo/$TZocaltime && echo $TZ > /etc/timezone

COPY ./ss.conf /etc/apache2/sites-available/
COPY ./frameworks2024/app/servicio_social/ /app
COPY ./settings.py /app/servicio_social/
COPY ./frameworks2024/requirements.txt /app/

WORKDIR /app

RUN a2ensite ss.conf

#RUN mkdir /app/media && chown :www-data /app/media -R && chmod 775 /app/media -R
RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
RUN python3 manage.py collectstatic --no-input

# forward request and error logs to docker log collector
RUN ln -sf /dev/stdout /app/err_log \
    && ln -sf /dev/stderr /app/log

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]