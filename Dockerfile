FROM python:3.7.2-stretch

WORKDIR /app

COPY . /app

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "levent.py"]
