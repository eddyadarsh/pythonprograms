#!/usr/bin/env python
# boto need to be installed and .boto need to be created in home directory which contains AWS crednetials like 
#[Credentials]
#aws_access_key_id = skjfnA
#aws_secret_access_key = ksfjsdjkf
# aws_del_config.txt contains names of all folders for which deletion policy need to be applied

import boto
import boto.s3.lifecycle
from boto.s3.lifecycle import Lifecycle, Expiration
lifecycle = Lifecycle()

for text in open("/opt/dbops/aws_del_policy/cfg/aws_del_config.txt","r"):
        words = text.split(':')
        duration = words[1]
        dbname = words[0]
        lifecycle.add_rule(dbname, prefix=''+ dbname + '/', status='Enabled', expiration=Expiration(days=duration))
s3 = boto.connect_s3(debug=2)
bucket = s3.get_bucket('databasedumps', validate=False)
bucket.configure_lifecycle(lifecycle)
