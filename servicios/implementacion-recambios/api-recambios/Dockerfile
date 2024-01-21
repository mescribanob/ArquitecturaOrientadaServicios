FROM python:3.10-slim-bullseye

WORKDIR /usr/src/api/

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "-m" , "uvicorn", "main:app", "--host 0.0.0.0", "--reload"]
