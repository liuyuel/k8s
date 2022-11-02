# 基于alpine镜像
FROM alpine

# 替换为国内的软件（清华大学）
RUN sed -i 's/https:\/\/dl-cdn.alpinelinux.org/http:\/\/mirrors.tuna.tsinghua.edu.cn/g' /etc/apk/repositories

# 更新软件包列表，安装数据库服务
RUN apk update && apk add mysql mysql-client bash

# 拷贝数据库数据文件
COPY mydomain.sql /

# 拷贝配置文件
COPY mariadb-server.cnf /etc/my.cnf.d/mariadb-server.cnf

# 拷贝启动脚本，开机自动执行
COPY init.sh /
ENTRYPOINT ["bash", "-x", "/init.sh"]