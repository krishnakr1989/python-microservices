FROM python:3.8.15-alpine3.15

WORKDIR /apps
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src src
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
                CMD curl -f http://localhost:5000/health || exit 1
ENTRYPOINT ["python","./src/flask-app.py"]
