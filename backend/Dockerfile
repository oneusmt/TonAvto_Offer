FROM python:3.11.9-slim

COPY requierements.txt requierements.txt
RUN pip install -r requierements.txt

COPY . .

CMD ["python", "main.py"]