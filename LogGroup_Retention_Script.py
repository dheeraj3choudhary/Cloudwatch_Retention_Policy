import boto3

client = boto3.client('logs')

response = client.describe_log_groups()

newlist=[]

for logs in response['logGroups']:
    newlist.append(logs['logGroupName'])

print("Log group name is appended in newlist as follows")
print(newlist)

for i in newlist:
    log=client.put_retention_policy(
        logGroupName=i,
        retentionInDays=30
    )
    print(log)

