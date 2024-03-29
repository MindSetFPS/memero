FROM node:18.9.1-alpine3.15 as node

WORKDIR /app/frontend
COPY ./frontend .

WORKDIR /app/frontend

RUN npm install
RUN npm run build

FROM python:3.11.1-alpine3.16

WORKDIR /app
COPY --from=0 /app/public ./public

COPY ./app.py /app
COPY ./db.py /app
COPY ./requirements.txt /app

RUN pip install -r requirements.txt
# RUN python db.py
EXPOSE 5000
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
# ENTRYPOINT ["sh"]