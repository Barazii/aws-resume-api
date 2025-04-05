aws cloudformation create-stack \
  --stack-name resume \
  --template-body file://resources-cfn.yaml \
  --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND\
  --region eu-north-1