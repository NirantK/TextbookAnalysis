FROM python:3.7-slim

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD requirements.txt /root/

RUN pip3 install -r /root/requirements.txt --no-cache-dir

RUN python -m spacy download en_core_web_sm

ADD . /root/textbookanalysis/

WORKDIR /root/textbookanalysis/

EXPOSE 3000

# CMD [ "uvicorn", "server.app:app", "--host=0.0.0.0" "--port=${PORT:-5000}" ]