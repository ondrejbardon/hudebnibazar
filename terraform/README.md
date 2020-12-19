# hudebnibazar lambda

Deploys infrastructure needed to periodically get check hudebnibazar.cz for interesting pedals.
 - Lambda itself
 - IAM role and policies
 - CloudWatch rule running in cron manner periodically triggering Lambda

## Requirements

- define 'name' variable that acts as common name for all resources
- manually create AWS Secrets Manager secret and insert it as argument

## TODO
- dynamodb
## Usage

```
module "contoso-smsbrana-backup" {
  name       = "contoso-smsbrana-backup"
  api_access_secret = "arn:aws:secretsmanager:eu-west-1:123451234567:secret:smsbrana/api-access-E3XLhK"
  source     = "../../modules/contoso-lambda-smsbrana-backup"

  lambda_env_vars = {
    SES_TO_ADDRESS = "user@contoso.com"
    AWS_SECRET_ID = "smsbrana/api-access"
    API_URL = "https://api.smsbrana.cz/smsconnect/http.php"
    S3_BUCKET = "contoso-smsbrana-backup"
    FILE_NAME = "smsbrana_daily_logs.txt"
    API_DOCUMENTATION = "https://www.smsbrana.cz/dokumenty/SMSconnect_dokumentace.pdf"
  }
}
```


