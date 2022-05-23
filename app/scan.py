import boto3
client=boto3.client("ecr")
response=client.describe_images(
repositoryName='demo_python_app',
    filter={
        'tagStatus':'ANY'
    }
)
print(response["imageDetails"])