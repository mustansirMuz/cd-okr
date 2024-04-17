FROM python:3.11

WORKDIR /usr/src/app

COPY ./requirements.txt requirements.txt
# COPY ./requirements.txt ./requirements.txt
RUN sh -c "pip install --no-cache-dir -r requirements.txt" 

COPY . .


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]