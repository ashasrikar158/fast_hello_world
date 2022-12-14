FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn","Main:app","--host","0.0.0.0","--reload"]