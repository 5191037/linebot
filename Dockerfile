FROM python:3.8.3-buster

RUN pip install flask && \
    pip install beautifulsoup4 && \
    pip install pymongo && \
    pip install requests && \
    pip install argparse && \
    pip install flask && \
    pip install flask-restful && \
    pip install line_bot_sdk && \
    pip install tqdm && \
    pip install selenium

RUN sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' && \
    wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    apt update && \
    apt install google-chrome-stable && \
    curl -O https://chromedriver.storage.googleapis.com/84.0.4147.30/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin

RUN mkdir /var/flask

COPY ./app.py /var/flask
COPY ./bot.py /var/flask

EXPOSE 8080

ENTRYPOINT ["/usr/local/bin/python", "/var/flask/app.py"]
