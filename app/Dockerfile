# FastAPI container.
FROM python:alpine
LABEL Maintainer="sean bourg <sean.bourg@gmail.com>"

WORKDIR /app
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

EXPOSE 80
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "80"]