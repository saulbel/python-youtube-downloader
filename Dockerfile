FROM python:3.10.6-alpine3.16
WORKDIR /app
COPY  requirements.txt /app/requirements.txt
RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate
RUN pip install -r requirements.txt
COPY app.py /app
CMD ["python", "app.py"]

