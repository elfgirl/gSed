FROM python:2.7
MAINTAINER Adrian

ADD https://bootstrap.pypa.io/get-pip.py ./
RUN python ./get-pip.py

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
#RUN pip install -r requirements.txt --proxy http://199.168.151.9:9480

RUN mkdir -p /build
WORKDIR /build

# Copy files
COPY ./builder.sh /
RUN chmod a+x /builder.sh

# Start building process
ENTRYPOINT ["/builder.sh"]
