FROM python:3.9

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install

RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["bash", "run.sh"]