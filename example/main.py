#!/usr/bin/env python
from amazon_kclpy import kcl
from base import RecordProcessor

class StdoutProcessor(RecordProcessor):
    
    def process_record(self, data, partition_key, sequence_number):
        print data

if __name__ == "__main__":
    kclprocess = kcl.KCLProcess(StdoutProcessor())
    kclprocess.run()
