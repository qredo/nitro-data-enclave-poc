FROM amazonlinux

# Install python for running the server and net-tools for modifying network config
RUN yum install python3 python-pip net-tools -y

WORKDIR /app

COPY requirements.txt ./
RUN pip3 install -r /app/requirements.txt

COPY server.py ./
COPY traffic-forwarder.py ./
COPY run.sh ./
COPY NsmUtil.py ./
COPY libnsm.so ./

RUN chmod +x run.sh

CMD ["/app/run.sh"]