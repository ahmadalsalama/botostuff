import boto
import os
import sys
from boto.s3.connection import S3Connection
#from boto.s3.key import key


LOCAL_PATH = '/Users/joelawson/tmp/'
AWS_ACCESS_KEY_ID = 'AKIAJ5SKM2FVXCNURXWQ'
AWS_SECRET_ACCESS_KEY = '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'
bucket_name = 'enterprise-ec2-describe-instances'

# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
# go through the list of files	
bucket_list = bucket.list()
for l in bucket_list:
    keyString = str(l.key)
    # check if file exists locally, if not: download it
    if not os.path.exists(LOCAL_PATH + keyString):
        l.get_contents_to_filename(LOCAL_PATH + keyString)
