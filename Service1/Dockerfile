FROM python:3.6.10
WORKDIR /Service1
COPY . /Service1
RUN pip3 install --no-cache-dir -r requirements.txt
RUN chmod a+x run.sh
CMD ["./run.sh"]