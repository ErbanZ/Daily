echo "execute_param: $1"
export $1

echo "path $execute_path"
echo "time $execute_time"
echo "http $execute_http"

if [ ! -n "$execute_path" ]; then  
  echo "execute_path IS NULL, exit shell"  
  exit 0
fi 
if [ ! -n "$execute_time" ]; then  
  echo "execute_time IS NULL, exit shell"  
  exit 0
fi 

if [ ! -n "$execute_http" ]; then  
  echo "execute_http IS NULL, exit shell"  
  exit 0
fi 



if [ ! -d "./gor" ]; then
  mkdir ./gor
fi
cd ./gor
mkdir $execute_path
cd $execute_path

touch execute.gor;
obsutil cp  obs://pub-obs-test-1/gor/$execute_path/  ../ -f -r -e  https://obs.cn-east-3.myhuaweicloud.com -i ME0AVBTNJTSJB2LH0EGI -k eCGffrwdx3Rt5QEmKbtEvruvGgg1mCUjMsnHfjWo

for gor_file in `find 10.*.gor`
do 
 cat $gor_file >> execute.gor;
done

obsutil cp obs://pub-obs-test-1/gor/gor-format-transfer.jar  gor-format-transfer.jar  -e https://obs.cn-east-3.myhuaweicloud.com -i ME0AVBTNJTSJB2LH0EGI -k eCGffrwdx3Rt5QEmKbtEvruvGgg1mCUjMsnHfjWo
java -jar gor-format-transfer.jar execute.gor format.gor
echo "format complete"
if [ -n "$execute_qps" ]; then  
  echo "qps replay: gor --input-file 'format.gor' --output-http  '$execute_http|$execute_qps' --exit-after $execute_time"
  gor --input-file "format.gor" --output-http  "$execute_http|$execute_qps" --exit-after $execute_time
elif [ -n "$execute_speed" ]; then
  echo "speed replay: gor --input-file 'format.gor|$execute_speed' --output-http  '$execute_http' --exit-after $execute_time"
  gor --input-file "format.gor|$execute_speed" --output-http  "$execute_http" --exit-after $execute_time
else
  echo "common replay: gor --input-file 'format.gor' --output-http  '$execute_http' --exit-after $execute_time"
  gor --input-file "format.gor" --output-http  "$execute_http" --exit-after $execute_time
fi 

cd ../ 
rm -rf $execute_path
exit 0

