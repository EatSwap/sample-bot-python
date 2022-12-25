FROM python:3.10-alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk add caddy
EXPOSE 8880
CMD ["sh", "entry.sh"]
