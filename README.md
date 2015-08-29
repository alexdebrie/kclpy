# KCLPY -- Docker

### Amazon Kinesis Client Library for Python

This is a base image for running a Kinesis Client Library application
with Python. It's designed to require a minimal amount of code to process
Kinesis records.

## Using the KCLPY image

To use the KCLPY image, you'll need the following things in a directory:

1. `main.py` -- A Python module that implements the [RecordProcessor class methods](http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-record-processor-implementation-app-py.html)
from the Python KCL library. 
2. `main.properties` -- A properties file for the KCL. An example can be found [here](https://github.com/awslabs/amazon-kinesis-client-python/blob/master/samples/sample.properties).
3. A Dockerfile to build your image.

Additional details on each can be found below. You can find an example in the
`example` directory. 

## Python RecordProcessor implementation

Read the AWS documentation on the RecordProcessor class implementation. 

Amazon has given a sample implementation of the RecordProcessor class [here](https://github.com/awslabs/amazon-kinesis-client-python/blob/master/samples/sample_kclpy_app.py).
It includes all logic necessary *except* the processing of a single record.
I've included it in `/code/base.py` in the Docker image, so you can import it
and subclass if you like. Then you'll only need to implement the `process_record` 
method to use it.

Example `main.py`:

    #!/usr/bin/env python
    from amazon_kclpy import kcl
    from base import RecordProcessor

    class ExampleProcessor(RecordProcessor):

        def process_record(self, data, partition_key, sequence_number):
            print data

    if __name__ == "__main__":
        kclprocess = kcl.KCLProcess(ExampleProcessor())
        kclprocess.run()

## Dockerfile requirements.

Your Dockerfile should look similar to the following:

    FROM alexdebrie/kclpy
    
    ENV AWS_ACCESS_KEY=<yourkey>
    ENV AWS_SECRET_KEY=<yourkey>

Make sure the credentials you use have the proper IAM permissions to 
perform the actions. If you are using the base RecordProcessor logic,
this includes read access to your Kinesis stream as well as access to
a DynamoDB table for checkpointing.

You may add additional steps to properly set up your environment (e.g.
install packages, set environment variables) as needed.

The base image will copy and `chmod` your root directory. It will also
run the CMD needed to start the KCL application. 
