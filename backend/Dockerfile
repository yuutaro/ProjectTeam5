FROM python:3.9-slim

WORKDIR /backend

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gosu \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5000

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]