FROM python:3.7-alpine

RUN mkdir -pv app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
ENTRYPOINT [ "python" ]

CMD [ "app.py" ]