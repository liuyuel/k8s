#!/bin/bash

#初始化环境变量
eval $(awk -F'=' '/^[^#].*/{print $0}' app/test.env)
#获取环境变量列表
VAR_LIST=($(awk -F'=' '/^[^#].*/{print $1}' app/test.env))
#获取配置文件列表
FILE_NAME=($(find  /root/app/  -name '*.*'|grep -v 'replace.sh'))

#替换配置文件引用的环境变量 sed -i "s/\${DOAMIN_NAME}/${DOMAIN_NAME}/g" app/mysql-storage.yaml
#sed -i "s/\${$(echo ${VAR_LIST[1]})}/$(eval $(echo "echo \$${VAR_LIST[1]}"))/g" 2.txt

for ((i=0;i<${#VAR_LIST[@]};i++)) do
 echo ${VAR_LIST[$i]}
 echo "${FILE_NAME[@]}" |xargs sed -i "s/\${$(echo ${VAR_LIST[1]})}/$(eval $(echo "echo \$${VAR_LIST[1]}"))/g" app/mysql-storage.yaml
done

