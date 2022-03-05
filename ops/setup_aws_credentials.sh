#!/bin/bash

set -xeuo pipefail

# defaultプロファイルにクレデンシャル情報を設定する．
aws configure << EOF
$(echo $AWS_ACCESS_KEY_ID)
$(echo $AWS_SECRET_ACCESS_KEY)
$(echo $AWS_DEFAULT_REGION)
json
EOF

# 正しく設定されたかを確認する．
aws configure list

