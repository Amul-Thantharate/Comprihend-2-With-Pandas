# Amazon Comprehend for Natural Language Processing (NLP)

# What is Amazon Comprehend? 

Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and relationships in text. No machine learning experience required. There is a console and API access. 

## Cost
If you are using free AWS tier, you can analyze 50K units a month free. A unit is 100 characters. In my example, every tweet is ~2 units. In the scheduled job I am analyzing 10K tweets at once, so the free tier limit runs out pretty fast, and then it's \$1 per 10K. Be sure to check pricing before you proceed. https://aws.amazon.com/comprehend/pricing/

### Preparation steps for using Comprehend through the console
1. Create account at Amazon AWS
2. Create an S3 bucket for your files

### Preparation steps for using Comprehend through the API
2. Create account at Amazon AWS
2. Create an admin user in IAM and get the access keys
3. Install AWS Command Line Interface (AWS CLI) and configued it to use your access keys
4. Create an S3 bucket for your file
5. Install python packages: boto3, pandas, json,tarfile

### For Creating acess keys and configuring AWS CLI follow the steps below 

1. Create an admin user in IAM and get the access keys 
2. Install AWS Command Line Interface (AWS CLI) and configued it to use your access keys 
3. Then aws configure 
### Boto3 Comrehend
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/comprehend.html
### Boto3 S3
https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)