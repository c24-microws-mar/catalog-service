FROM mhart/alpine-node:4.2
MAINTAINER c24-microws-mar

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install

COPY . /usr/src/app

ENV PORT=3000
ENV SHUTDOWN_TIMEOUT=10000
ENV SERVICE_NAME=catalog-service
ENV SERVICE_TAGS=v2
ENV SERVICE_CHECK_HTTP=/healthcheck
ENV SERVICE_CHECK_INTERVAL=10s
ENV SERVICE_CHECK_TIMEOUT=2s
ENV SERVICE_ENDPOINTS=/endpoints
ENV DISCOVERY_SERVERS=http://46.101.245.190:8500,http://46.101.132.55:8500,http://46.101.193.82:8500

EXPOSE 3000

CMD ["node", "index.js"]
