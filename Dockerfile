FROM python:3.8-slim

RUN apt-get update && \
    apt-get install -y gcc

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.port", "8501"]