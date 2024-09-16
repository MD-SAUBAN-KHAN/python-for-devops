import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='mdsk-boto3-dummy1',

)
print("===>>>BUCKET CREATED<<<===")

"""response = client.get_bucket_acl(
    Bucket='mdsk-boto3-dummy1',
    
)
print(response)"""

print("===>>>buckets ::")
response = client.list_buckets()
print(response)
response = client.delete_bucket(
    Bucket="mdsk-boto3-dummy1",
      
)
print("===>>>BUCKET DELETED<<<===")
print(response)  