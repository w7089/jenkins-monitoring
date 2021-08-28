FROM python:3.9

COPY requirements.txt /usr/src/app/requirements.txt
WORKDIR /usr/src/app
RUN pip3 install -r requirements.txt
COPY initialize-jenkins.py /usr/src/app/
CMD python3 initialize-jenkins.py