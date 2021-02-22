import boto3
import mimetypes
import json
import subprocess
import sys
import paramiko
import os
s3copyarg='aws s3 cp /home/ec2-user/kee/ s3://keerthana123cherry5/folder --exclude "*"  --include "*.json" --recursive'
#print(s3copyarg)
client = boto3.client('sts')
rolearn='arn:aws:iam::039262309645:role/awss3access'
response = client.assume_role(RoleArn=rolearn, RoleSessionName="mytestsession")['Credentials']
print(response)
accesskey=response['AccessKeyId']
secretkey=response['SecretAccessKey']
sessiontoken=response['SessionToken']
s3synclocal='aws s3 sync  /Users/keerthana/airflow/dags/keeprog s3://keerthana123cherry5/folder --exclude "*" --include "*.json"'
s3syncremote='aws s3 sync /home/ec2-user/kee/ s3://keerthana123cherry5/folder --exclude "*"  --include "*.json"'
class ec2tos3:
    def ssh(self,cmd):
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        key = paramiko.RSAKey.from_private_key_file('/Users/keerthana/Desktop/ec2instance/elasticcache.pem')
        client.connect('54.215.240.221','22','ec2-user', pkey=key)
        stdin, stdout, stderr = client.exec_command(cmd)
        return stdout.readlines()
    def __init__(self):
        return
    def name(self,c,d,command,check):
        if check==2:
            dir=set(c)-set(d)
            length=len(dir)
            if len(dir)==0: print ("BOTH FILES ARE SAME")
            else:
                while length > 0:
                    print ("BOTH FILES ARE DIFFERENT")
                    command
                    print('synced')
                    length=length-1
        if check==1:
            print(c,d)
            if c==d: print("files are same")
            else:
                while c<d:
                    print("files are not same")
                    syncfile=command
                    print(syncfile)
                    print('synced')
                    main=a.ssh('aws s3 ls s3://keerthana123cherry5/folder/ | wc -l')
                    print(main)
                    s3value=int(main.read().decode())
                    print(s3value)
                    #s3value=s3value+1
            if c>d:
                print("s3 contains more files than local or remote check file is empty")
a=ec2tos3()
var=a.ssh('export AWS_ACCESS_KEY_ID={access} ; ' \
                  'export AWS_SECRET_ACCESS_KEY={secret};' \
                  'export AWS_SESSION_TOKEN={session};' \
                  '{command}'.
                  format(access=accesskey, secret=secretkey, session=sessiontoken))
m = [i.split('\n')[0] for i in var]
print(m)
a.name(m[0],m[1],a.ssh(s3syncremote),1)

