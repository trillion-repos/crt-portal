"""" putting the basic set up instructions into a script """"
SPACE=$1


# create DB
if service_exists "crt-db" ; then
  echo crt-db already created
else
  if [ $SPACE = "prod" ] ; then
    cf create-service aws-rds medium-mysql crt-db
  else
    cf create-service aws-rds shared-mysql crt-db
  fi
fi

# Create file storeage
if service_exists "crt-s3" ; then
  echo crt-s3 already created
else
    cf create-service s3 basic-public crt-s3
fi

# create key to update file storage assumes you have the jq tool https://stedolan.github.io/jq/
SERVICE_INSTANCE_NAME=crt-s3
KEY_NAME=crt-s3-key

if not service_exists "crt-s3-key" ; then
    cf create-service-key "${SERVICE_INSTANCE_NAME}" "${KEY_NAME}"
fi

S3_CREDENTIALS=`cf service-key "${SERVICE_INSTANCE_NAME}" "${KEY_NAME}" | tail -n +2`

export AWS_ACCESS_KEY_ID=`echo "${S3_CREDENTIALS}" | jq -r .access_key_id`
export AWS_SECRET_ACCESS_KEY=`echo "${S3_CREDENTIALS}" | jq -r .secret_access_key`
export BUCKET_NAME=`echo "${S3_CREDENTIALS}" | jq -r .bucket`
export AWS_DEFAULT_REGION=`echo "${S3_CREDENTIALS}" | jq -r '.region'`

cat << EOF > cors.json
{
  "CORSRules": [
    {
      # to do make real name based on environment
      "AllowedOrigins": ["crt-portal-django-{$SPACE}.app.cloud.gov"],
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["HEAD", "GET"],
      "ExposeHeaders": ["ETag"]
    }
  ]
}
EOF

aws s3api put-bucket-cors --bucket $BUCKET_NAME --cors-configuration file://cors.json
# delete key now that you updated the bucket
delete-service-key crt-s3 crt-s3-key

# build deploy keys
if not service_exists crt-service-account-{$SPACE} ; then
    ccloud-gov-service-account space-deployer crt-service-account-{$SPACE}
fi

if not service_exists crt-portal-{$SPACE}-key ; then
    cf create-service-key crt-service-account-{$SPACE} crt-portal-{$SPACE}-key
fi

echo "Add these keys to Circle CI for automated deploys"
cf service-key crt-service-account-{$SPACE} crt-portal-{$SPACE}-key

echo "Now you can set the secret key to VCAP_SERVICES"
