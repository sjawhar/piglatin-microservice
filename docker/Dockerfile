FROM alpine:3.4

RUN apk add --update musl py-pip bash
RUN pip install falcon gunicorn

WORKDIR /app

EXPOSE 80
CMD ["gunicorn", "-b", "0.0.0.0:80", "--reload", "api:app"]
