FROM python:3

WORKDIR /usr/src/prom_client

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./prom_client.py" ]
