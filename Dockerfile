FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
RUN  pip install --upgrade pip
RUN  pip install --upgrade google-api-python-client
RUN pip install -r requirement.txt
EXPOSE 5000
RUN -p 5000:5000 sonalk527/python-flask:latest
CMD python ./main.py

