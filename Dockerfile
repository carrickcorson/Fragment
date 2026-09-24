FROM python:3.14
RUN adduser app-user
USER app-user

WORKDIR /home/app-user/fragment/

COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /home/app-user/fragment/src/
ENTRYPOINT ["uv", "run", "fastapi", "dev", "app.py"]