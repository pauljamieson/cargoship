FROM nginx:alpine

RUN apk add openssl gettext
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.template
COPY setup_server.sh /docker-entrypoint.d/