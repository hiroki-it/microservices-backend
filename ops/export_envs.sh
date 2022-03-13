#!/bin/bash

set -xeuo pipefail

# 環境変数を定義します．
echo 'export AWS_ECR_ACCOUNT_URL="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"' >> $BASH_ENV

# 環境変数を出力します．
source $BASH_ENV
