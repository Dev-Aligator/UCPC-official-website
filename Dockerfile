FROM python:3.8-slim-buster

ENV PATH="/scripts:${PATH}"
ENV DEBUG=0
ENV ALLOWED_HOSTS=127.0.0.1,localhost

RUN apt-get update
RUN apt-get install -y .tmp gcc libc-dev python3-dev

COPY ./requirements.txt /requirements.txt
RUN python3 -m pip install --no-cache-dir -r /requirements.txt

RUN mkdir -p /app
COPY ./ /app

WORKDIR /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*

# RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN useradd -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user

EXPOSE 8000

CMD ["entrypoint.sh"]