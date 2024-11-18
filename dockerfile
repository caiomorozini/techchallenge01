FROM python:3

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

# RUN chmod +x /app/entrypoint_app.sh

# ENTRYPOINT ["/app/entrypoint_app.sh"]

CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]