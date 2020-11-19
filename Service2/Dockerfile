# FROM python:3.6.10
FROM python:3
WORKDIR /Service2
COPY . /Service2
RUN pip3 install --no-cache-dir -r requirements.txt && chmod a+x run.sh
CMD ["./run.sh"]
