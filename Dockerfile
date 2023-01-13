FROM python:3.11.1-alpine3.16

RUN apk add nodejs-current
RUN apk add npm

WORKDIR /app

COPY . .

WORKDIR /app/frontend/vite-project

RUN npm i
RUN npm run build

WORKDIR /app

ENTRYPOINT ["flask", "--app", "app", "run"]
