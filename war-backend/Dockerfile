FROM python:3

RUN apt-get update && apt-get install sqlite3 libsqlite3-dev -y && apt-get install nano

ENTRYPOINT ["tail", "-f", "/dev/null"]
