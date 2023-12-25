FROM docker:24.0.7-dind-alpine3.18
RUN apk update && \
    apk add bash git jq python3
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt src /src/
RUN pip install -r /src/requirements.txt
CMD [ "python3", "src/starter.py" ]