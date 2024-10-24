FROM python:3.10
WORKDIR /app
COPY . ./
RUN pip install pyyaml click requests
ENTRYPOINT ["python", "./main.py"]