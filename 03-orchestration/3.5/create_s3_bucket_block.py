from time import sleep
# from prefect_aws import S3Bucket, AwsCredentials
from prefect_gcp import GcpCredentials,GcsBucket

def create_gcp_creds_block():
    service_account_info = {
    }

    GcpCredentials(
        service_account_info=service_account_info
    ).save("my-gcp-creds",overwrite=True)


def create_gcs_bucket_block():
    # aws_creds = AwsCredentials.load("my-aws-creds")
    # my_s3_bucket_obj = S3Bucket(
    #     bucket_name="my-first-bucket-abc", credentials=aws_creds
    # )
    # my_s3_bucket_obj.save(name="s3-bucket-example", overwrite=True)
    gcs_bucket = GcsBucket(
    bucket="mlops-data-2023",
    gcp_credentials=GcpCredentials.load("my-gcp-creds"),
    )
    gcs_bucket.save(name="gcs-data-block", overwrite=True)


if __name__ == "__main__":
    create_gcp_creds_block()
    sleep(5)
    create_gcs_bucket_block()
