FROM python:3.9.18-slim
RUN apt update -y && \
    apt install git curl -y
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt src /src/
RUN pip install -r /src/requirements.txt

RUN curl -SL https://github.com/docker/compose/releases/download/v2.23.3/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose && \
    chmod +x /usr/local/bin/docker-compose

CMD [ "python3", "/src/index.py" ]