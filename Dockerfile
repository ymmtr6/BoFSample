FROM ubuntu:latest

# setup python3.6
RUN set -x \
&& apt-get update \
&& apt-get install -y python3-pip python3-dev \
&& apt-get install -y make wget unzip \
&& cd /usr/local/bin \
&& ln -s /usr/bin/python3 python \
&& pip3 install --upgrade pip

# setup libsvm
RUN set -x \
&& cd /usr/local/ \
&& wget "http://www.csie.ntu.edu.tw/~cjlin/cgi-bin/libsvm.cgi?+http://www.csie.ntu.edu.tw/~cjlin/libsvm+zip" -O libsvm-3.23.zip \
&& unzip libsvm-3.23.zip \
&& cd libsvm-3.23 \
&& make

ENV PATH $PATH:/usr/local/libsvm-3.23/
WORKDIR /workspace
ENV HOME /workspace