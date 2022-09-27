import boto3

dryRun = False;

responseRegions = boto3.client('ec2').describe_regions()
for region in responseRegions['Regions']:
    regionName = region['RegionName']
    print(" -- ", regionName)
    client = boto3.client('logs', region_name=regionName)
    responseLogGroups = client.describe_log_groups()
    for logs in responseLogGroups['logGroups']:
        logGroupName = logs['logGroupName']
        print("   -- ", logGroupName)
        if not dryRun:
            client.put_retention_policy(
	        logGroupName=logGroupName,
    	        retentionInDays=30
    	    )
