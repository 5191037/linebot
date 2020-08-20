FROM python:3.8.3-buster

RUN apt update && \
    pip install -U pip

RUN pip install flask && \
    pip install beautifulsoup4 && \
    pip install pymongo && \
    pip install requests && \
    pip install argparse && \
    pip install flask && \
    pip install flask_restful && \
    pip install pymongo && \
    pip install linebot && \
    pip install linebot.exceptions && \
    pip install linebot.models && \
    pip install tqdm && \
    pip install selenium && \
    pip install selenium.webdriver.chrome.options

RUN mkdir /var/flask

COPY ./app.py /var/flask
COPY ./bot.py /var/flask

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python", "/var/flask/app.py"]
