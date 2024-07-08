FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# COPY agents.py prompts.py utils.py ./
COPY . /app

RUN mkdir /app/data

EXPOSE 8080

# command to run the script
CMD ["python", "agents.py"]