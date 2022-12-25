FROM python:3.10-bullseye
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN bash install_caddy.sh
EXPOSE 8880
CMD ["sh", "entry.sh"]
