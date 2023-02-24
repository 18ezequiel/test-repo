import boto3

# Crear un cliente S3
s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAXRYNTY2XHJGTAXYG',
    aws_secret_access_key='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',
    region_name='us-west-2'
)

# Nombre de los buckets
bucket_name1 = 'datalake-raw'
bucket_name2 = 'datalake-stage'
bucket_name3 = 'datalake-analytics'
bucket_name4 = 'datalake-disc'


# Especificar la región
bucket_config = {
    'LocationConstraint': s3.meta.region_name
}

# Crear los buckets
s3.create_bucket(Bucket=bucket_name1, CreateBucketConfiguration=bucket_config)
s3.create_bucket(Bucket=bucket_name2, CreateBucketConfiguration=bucket_config)
s3.create_bucket(Bucket=bucket_name3, CreateBucketConfiguration=bucket_config)
s3.create_bucket(Bucket=bucket_name4, CreateBucketConfiguration=bucket_config)


print(f'Bucket {bucket_name1} creado en la región {s3.meta.region_name} con éxito.')
print(f'Bucket {bucket_name2} creado en la región {s3.meta.region_name} con éxito.')
print(f'Bucket {bucket_name3} creado en la región {s3.meta.region_name} con éxito.')
print(f'Bucket {bucket_name4} creado en la región {s3.meta.region_name} con éxito.')