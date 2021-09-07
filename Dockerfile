FROM python:3.8-slim-buster

ADD calendario.py .

CMD ["calendario.py"]

ENTRYPOINT [ "python3" ]