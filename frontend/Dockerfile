FROM node:16

WORKDIR /frontend

COPY . /frontend

RUN npm install

EXPOSE 3000

RUN npm run build

CMD ["npm", "start"]
