FROM python:3.8-slim-buster

ADD calendario.py .

RUN python3 -m pip install requests

CMD ["python3" , "calendario.py"]

