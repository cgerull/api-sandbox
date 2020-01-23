FROM alpine:3.11
# Use alpine linux as base image

RUN apk add --no-cache --virtual ca-certificates && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools && \
    adduser --disabled-password web && mkdir -p /home/web/log/ && chown -R web.web /home/web/

USER web
WORKDIR /home/web

COPY --chown=1000 requirements.txt /home/web


ENV PATH=$PATH:/home/web/.local/bin \
    PORT=8080 \
    ERRLOG=- \
    ACCESSLOG=- \
    LOGFORMAT="%(h)s %(l)s %(t)s %({Server-IP}o)s %(l)s %(r)s %(s)s %(b)s %(a)s" \
    LOGLVL=INFO

# Install application
RUN pip3 install --user -r requirements.txt

EXPOSE 8080

# ARG TOKEN
# RUN wget -O /microscanner https://get.aquasec.com/microscanner && \
#     chmod +x /microscanner && \
#     /microscanner $TOKEN && \
#     rm -rf /microscanner
