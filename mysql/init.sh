#!/bin/bash




# 根据HOSTNAME的值判断部署主或者从容器
if [ "$HOSTNAME" == "${DOMAIN_NAME}-mysql-0" ]; then
  if [ ! -e "/var/lib/mysql/mysql" ]; then
    # 初始化数据库
    mysql_install_db --user=mysql --datadir=/var/lib/mysql/
    # 启动数据库
    mysqld_safe --user=mysql --datadir=/var/lib/mysql/ &
    # 等待数据库启动完毕，等待/run/mysqld/mysqld.sock文件存在
    while [ ! -e "/run/mysqld/mysqld.sock" ]; do
      sleep 3
    done
    # 根据环境变量创建外联用户
    mysql -e "GRANT ALL PRIVILEGES ON ${DOMAIN_NAME}.* TO \"$MYSQL_ACC_USER\"@\"%\" IDENTIFIED BY \"$MYSQL_ACC_PASSWD\" WITH GRANT OPTION"
    # 根据环境变量创建同步用户
    mysql -e "GRANT REPLICATION SLAVE ON *.* TO \"$MYSQL_SYNC_USER\"@\"%\" IDENTIFIED BY \"$MYSQL_SYNC_PASSWD\""
    # 查看主数据库事件状态
    mysql -e "show master status"
    # 创建${DOMAIN_NAME}数据库并导入数据
    mysql -e "create database ${DOMAIN_NAME}"
    mysql ${DOMAIN_NAME} < /${DOMAIN_NAME}.sql
  else
    # 启动数据库
    mysqld_safe --user=mysql --datadir=/var/lib/mysql/ &
  fi
else
  if [ ! -e "/var/lib/mysql/mysql" ]; then
    # 关闭二进制日志
    sed -i "s/log-bin=${DOMAIN_NAME}/#log-bin=${DOMAIN_NAME}/g" /etc/my.cnf.d/mariadb-server.cnf
    sed -i "s/binlog_do_db=${DOMAIN_NAME}/#binlog_do_db=${DOMAIN_NAME}/g" /etc/my.cnf.d/mariadb-server.cnf
    # 修改集群ID为200-1000之间随机数
    sed -i "s/server-id=111/server-id=$(echo $RANDOM % 800 + 200 | bc)/g" /etc/my.cnf.d/mariadb-server.cnf
    # 初始化数据库
    mysql_install_db --user=mysql --datadir=/var/lib/mysql/
    # 启动数据库
    mysqld_safe --user=mysql --datadir=/var/lib/mysql/ &
    # 等待数据库启动完毕，等待/run/mysqld/mysqld.sock文件存在
    while [ ! -e "/run/mysqld/mysqld.sock" ]; do
      sleep 3
    done
    # 根据环境变量创建外联用户
    mysql -e "GRANT ALL PRIVILEGES ON ${DOMAIN_NAME}.* TO \"$MYSQL_ACC_USER\"@\"%\" IDENTIFIED BY \"$MYSQL_ACC_PASSWD\" WITH GRANT OPTION"
    # 与主数据库做同步对接
    mysql -e "CHANGE MASTER TO MASTER_HOST=\"$MYSQL_MASTER_ADDR\",MASTER_USER=\"$MYSQL_SYNC_USER\",MASTER_PASSWORD=\"$MYSQL_SYNC_PASSWD\",MASTER_LOG_FILE=\"$MYSQL_SYNC_FILE\",MASTER_LOG_POS=$MYSQL_SYNC_POS"
    # 开启同步，查看同步状态
    mysql -e "START SLAVE"
    mysql -e "SHOW SLAVE STATUS \G"
  else
    # 启动数据库
    mysqld_safe --user=mysql --datadir=/var/lib/mysql/ &
  fi
fi