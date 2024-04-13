FROM python:3.10-slim

WORKDIR /server

COPY . /server

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start_server.sh

EXPOSE 8080

CMD ["./start_server.sh"]
