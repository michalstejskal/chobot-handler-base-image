FROM python:3-alpine
WORKDIR /service
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . ./
ARG EXPOSE_PORT
EXPOSE ${EXPOSE_PORT}
ENTRYPOINT ["python3", "handler.py"]