FROM python:3.10-slim-buster
WORKDIR /usr/src/app
ADD app.py .
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
VOLUME [ "/app/data" ]
COPY . .
EXPOSE 5000 
CMD ["python", "./app.py"]

