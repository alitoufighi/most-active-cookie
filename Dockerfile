FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN python -m unittest tests/*.py -v
ENTRYPOINT ["python", "main.py"]
