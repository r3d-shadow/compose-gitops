FROM docker:24.0.7-dind-alpine3.18
RUN apk update && \
    apk add bash git jq
COPY utils/misc/* utils/cronjob.sh utils/starter.sh /utils/
RUN echo "*/5    *       *       *       *       /deploy/cronjob.sh" >> /etc/crontabs/root
CMD [ "utils/starter.sh" ]