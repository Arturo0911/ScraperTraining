FROM python:3.8.5

run mkdir /app

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3", "app.py"]

