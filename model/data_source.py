# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 10:32:21 2022

@author: akhil
"""


import boto3
import os
session = boto3.Session(
aws_access_key_id="AKIA4VVXTVMKBN7UK3KM",
aws_secret_access_key="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"
)

s3 = session.resource('s3')

#s3.Bucket('stockmarket4').download_file("data/TATASTEEL.csv","data/TATASTEEL.csv")

def downloadfile(file_name):
    s3.Bucket('stockmarket4').download_file(file_name,file_name)