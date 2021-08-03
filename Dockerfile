FROM python:3.7-slim

RUN apt-get update -qq \
    && apt-get install -y --no-install-recommends build-essential git-core \
    && apt-get clean \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /textbookanalysis
COPY . /textbookanalysis
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "5000"]