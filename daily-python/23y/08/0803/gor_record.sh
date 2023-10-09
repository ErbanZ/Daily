echo "execute_param: $1"

export $1
echo "path $execute_path"
echo "uri  $record_uri"
echo "time $execute_time"

# 
if [ ! -n "$execute_path" ]; then  
  echo "execute_path IS NULL, exit shell"  
  exit 0
fi 

if [ ! -n "$record_uri" ]; then  
  echo "record_uri IS NULL, exit shell"  
  exit 0
fi 

if [ ! -n "$execute_time" ]; then  
  echo "execute_time IS NULL, exit shell"  
  exit 0
fi 

if [ ! -d "./gor" ]; then
  mkdir ./gor
fi
cd ./gor
mkdir $execute_path
echo "create dir $execute_path"
cd $execute_path
echo "cd dir $execute_path"

ip=`ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"`_;
date=`date "+%Y%m%d%H%M%S"`;
path="${record_uri///}"_;

echo "gorFileName $ip$path$date.gor"
echo $record_uri

if [ "$record_uri" == '*' ] ; then
echo "record all uri"
gor --input-raw :80 --output-file=$ip$path$date.gor --exit-after $execute_time;
else 
echo "record allow url"
gor --input-raw :80 --output-file=$ip$path$date.gor --http-allow-url $record_uri --exit-after $execute_time;
fi

for gor_file in `find ./ -name "*.gor"`;  
do
upload_name=${gor_file//.\//}
echo "************upload_gorFileName $upload_name"
obsutil cp $gor_file obs://pub-obs-test-1/gor/$execute_path/$upload_name -e https://obs.cn-east-3.myhuaweicloud.com -i ME0AVBTNJTSJB2LH0EGI -k eCGffrwdx3Rt5QEmKbtEvruvGgg1mCUjMsnHfjWo
rm -rf  $gorFile
done
cd ../
rm -rf $execute_path
exit 0


