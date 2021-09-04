FROM python:3.8

ADD calendario.py .

CMD ["calendario.py"]

ENTRYPOINT [ "python3" ]