FROM  python:3.12-alpine

ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--reload", "--port", "8000"]