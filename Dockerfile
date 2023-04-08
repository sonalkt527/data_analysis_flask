FROM python:3-alpine3.15
WORKDIR /app
COPY . /app
EXPOSE  80:80
EXPOSE 0:0
RUN  pip install --upgrade pip
RUN  pip install --upgrade google-api-python-client
RUN pip install -r requirement.txt

CMD python ./main.py

