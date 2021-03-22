FROM python:3.7.2-stretch

WORKDIR /app

ADD . /app

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "levent.py"]
