FROM python:3.9

EXPOSE 8000
WORKDIR . ./code
COPY . .

RUN pip install -r requirements.txt


