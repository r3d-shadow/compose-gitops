FROM docker:24.0.7-dind-alpine3.18
RUN apk update && \
    apk add bash git jq python3
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY requirements.txt utils/misc/* utils/cronjob.sh utils/starter.py /utils/
RUN pip install -r /utils/requirements.txt
RUN echo "*/5    *       *       *       *       /utils/cronjob.sh" >> /etc/crontabs/root
CMD [ "python3", "utils/starter.py" ]