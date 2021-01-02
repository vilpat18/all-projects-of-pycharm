import boto3

# ceate an s3 client
s3 = boto3.client('s3')

# Call s3 to list current bucket
response = s3.list_buckets()

# Get a list of all bucket nmaes from the response
buckets = [bucket['names'] for bucket in response['Buckets']]

# Print out the bucket list
print('bucket list: %s' % buckets)