#!/bin/bash 

set -e 

if [ command -v aws >/dev/null 2>&1 ]; then
    echo "aws cli is not installed"
    exit 1
else
    echo "aws cli is installed"
fi

aws s3api create-bucket --bucket $1 --region $2 
aws s3api put-bucket-versioning --bucket $1 --versioning-configuration Status=Enabled 
#  create a folder in s3 bucket 

aws s3api put-object --bucket $1 --key "input/" 

aws s3api put-object --bucket $1 --key "results/"

aws s3 cp ..\\Comprehend\\wallmarts_tweets.csv s3://$1/input/wallmarts_tweets.csv

exit 0
