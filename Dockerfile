FROM python:3.14
WORKDIR /usr/local/app

COPY requirements.txt ./
COPY .venv/ ./

RUN . .venv/bin/activate
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd app
USER app

