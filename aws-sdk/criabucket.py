import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


def create_bucket(bucket_name, region=None):
    try:
        # Cria o cliente S3
        s3_client = boto3.client('s3', region_name=region)

        # Cria o bucket
        if region is None:
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': region}
            )
        print(f"Bucket '{bucket_name}' criado com sucesso.")
    except NoCredentialsError:
        print("Erro: Credenciais da AWS não encontradas.")
    except PartialCredentialsError:
        print("Erro: Credenciais da AWS incompletas.")
    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de uso
if __name__ == "__main__":
    bucket_name = "meu-novo-bucket"
    region = "us-east-1"
    create_bucket(bucket_name, region)