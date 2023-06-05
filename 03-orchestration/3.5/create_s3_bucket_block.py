from time import sleep
# from prefect_aws import S3Bucket, AwsCredentials
from prefect_gcp import GcpCredentials,GcsBucket

def create_gcp_creds_block():
    # my_aws_creds_obj = AwsCredentials(
    #     aws_access_key_id="123abc", aws_secret_access_key="abc123"
    # )
    # my_aws_creds_obj.save(name="my-aws-creds", overwrite=True)
    service_account_info = {
    "type": "service_account",
  "project_id": "mlops-demo-387018",
  "private_key_id": "3529df3917d0277a5ac20b6ee9640991bcd98ad4",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCnt5MRzU53BnH9\n7hHTIaUVE1Xb8iYEoVyrrmhS5ETAffWMdz67bF+nJU27Pkdd+a9F0HkPNV2zms8B\nFhtDxVaTrFAA93HiKPzyo7gmDyx+hRuKp9WkPEGhbWgzOVZGeFz/AH+xumtNd/nM\nf1DUI8L2xefv9O6BfwfosLVk7TTY2kLNNaJQ68rp6ipubGWAgrAqCRj1CBcfS1c5\nbzpnbQOwL5yYjSj8sO50WWVoE0jBjGefXP+2p9jtOfUuvoPI1UFAN87CbRdz9luZ\ntTD0sQSB3xsz4lqYZF5VFfQPDYNi34vqgZIgMeIkXSHtnE6oOD4UrsS9YfFqIRsi\nfszsx8LdAgMBAAECggEAGl4upZRZGzZssob8z2xRN2yISaGa34x89NLhPPL9aiQD\neFeBCddifHVNcLw8XSZ1q2y4s67oseWLWPjgRXnfgC0NkPFWOr/F8OHTgExPav7D\nUzvKx1zf1qDMSo1fpomi2UZ7TPZpi07q+38ito9+xexcaCniW4KcvDUX96uhbNw2\ngTVcunKN5ma8eIkWJwSuqsHtxO1ghoqymliRO4u/rHyYG8Nk7E/ldp5f5mgAVrB+\nKUugq0McPBRpX7ahaCGVHvVJhibnP2eLCOf8jinjFIvHNg1jzGbc0eeWbjK/wcz8\nFw0+McMY4uh6AL0Kpm62NCd9x4XaQzGczPRt9cApEwKBgQDYF4bloJ9Tr7gurEm3\n+RO3Rw7l0zxvmon1qfb8xw+oC/+quZiAdcvSTmFR1CvqbC9c2lW3wxtIQgV+Xb7R\nd96T7rLptBYopECYOOBRA9y+f8NNCOjn1/HEM9jn7X/y9mmEOXnyTiA5DjsDnNem\nwKVWVuzWamH+r5AUFETz7wpGhwKBgQDGsPcT2lfpO+TQrmGrhr3tjvIvrpgAOHXe\n6DPjO/Aa3+XW53pP9WB5vheeL6pUET13c3O8AmmVBkYn0/4dqBYJ6w6Kp9bqreZg\nMc9igJoA8123FxhcO+2L76kkyJZym3nYu1hRWDeiQPI66GbaVH1JMLb867yiKipD\n07hzwIEgewKBgQDK7DUCV/ammMHGGoZTnDQWjUUBL392clIRfx1wPOKH9VSOlyEN\nqRDRGkerlynyRsunT2TlXvO0xELyasgxXnaGxsX+Tt3sJmp+SBLmIVFfFw1ovvAw\nH4pqrCGJkm7v0tQ9ldfdYd5Clgl3GAcvEYNx88kOhPInP+h14p7pz1T/6wKBgAx4\nNLlxPY0srhqOpyCNr0PGcdqeOXniETuxFPiQ3WvCW3lWQ63a93gMfwz1btohztq9\nSykkeZ3Zq/N58XvI/cEXmG0JRYqq6UdmON60tXWT0HDaKTQ4qpraqqHdWNvOeCIq\n98r7H1q2er1JspLHNKmwPfu3i7odrVNeaTgSf8gbAoGBAJDDIOGG+MzGLHpNISgr\n/VZwmWHPjYM9sYT1E5I01lnTzP+jftSh1RWLmXe4yrEdGO4nVlzavMECyosOKRVY\nflp25RPLXxr/+p6FjqqY61HFD4igHwLXkoO3PUnyutxQS4i19a6FUfJUXOj3TJAF\nqyeO0Xos9LBahjSBKX9BzP8d\n-----END PRIVATE KEY-----\n",
  "client_email": "463529954799-compute@developer.gserviceaccount.com",
  "client_id": "107023639331421979075",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/463529954799-compute%40developer.gserviceaccount.com",
  "universe_domain": "googleapis.com"
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
