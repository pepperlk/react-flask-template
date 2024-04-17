FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:18-bullseye as build
# RUN apk add --no-cache python3 py3-pip py3-dev
# # install latest nodejs
# RUN apk add --no-cache nodejs npm



WORKDIR /build
COPY . .

WORKDIR /build/client
RUN npm install
RUN npm run build






# CMD ["/bin/bash"]
FROM alpine:latest as runner
RUN apk add --no-cache python3 py3-pip

WORKDIR /app
COPY . /app
COPY --from=build /build/client/build /app/client/build


# install dependencies
RUN pip install -r requirements.txt --break-system-packages

EXPOSE 8005
# run flask on port 80 when the container launches
CMD ["python3", "-m", "flask", "run", "--port=8005", "--host=0.0.0.0"]



