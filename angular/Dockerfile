FROM node:19-bullseye

RUN mkdir /project
WORKDIR /project

RUN npm install -g @angular/cli@13

COPY package.json package-lock.json ./
RUN npm ci
ARG proxy_address

COPY . .
CMD ["ng", "serve", "--host", "0.0.0.0", "--disable-host-check", "--live-reload", "false"]
