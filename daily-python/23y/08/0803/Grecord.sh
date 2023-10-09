#!/bin/bash
echo "xxl-job: hello shell"
echo "执行参数：$1"
echo "当前脚本路径：$(cd `dirname $0`; pwd)"

if [ ! -d "./gor" ]; then
  mkdir ./gor
fi

cd ./gor
clear_path=`pwd`

obsutil cp obs://pub-obs-test-1/gor/gor_record.sh  gor_record.sh -e https://obs.cn-east-3.myhuaweicloud.com -i ME0AVBTNJTSJB2LH0EGI -k eCGffrwdx3Rt5QEmKbtEvruvGgg1mCUjMsnHfjWo
sh gor_record.sh "$1"
cd $clear_path

# rm -rf *
exit 0
