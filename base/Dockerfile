FROM debian:8.1
RUN apt-get update && apt-get install -y --no-install-recommends openjdk-7-jre \
    python \
    python-dev \
    python-pip \
    && rm -rf /var/lib/apt/lists/*

RUN pip install amazon_kclpy==1.1.0
COPY base.py /code/

ONBUILD COPY . /code/
ONBUILD RUN chmod -R 755 /code/

CMD ["/usr/bin/java", "-cp", \
     "/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/jackson-core-2.1.1.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/commons-logging-1.1.1.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/jackson-databind-2.1.1.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/amazon-kinesis-client-1.2.1.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/jackson-annotations-2.1.1.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/aws-java-sdk-1.7.13.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/httpclient-4.2.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/commons-codec-1.3.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/httpcore-4.2.jar:/usr/local/lib/python2.7/dist-packages/amazon_kclpy-1.1.0-py2.7.egg/amazon_kclpy/jars/joda-time-2.4.jar:/code", \
     "com.amazonaws.services.kinesis.multilang.MultiLangDaemon", \
     "main.properties"]
