FROM python:3.7.2-stretch

ENV webhook_url="https://webhook.site/17b407f8-5266-4e83-8305-57d60136995e"

WORKDIR /app

ADD . /app

RUN python3 -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "levent.py"]
