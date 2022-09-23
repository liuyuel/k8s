k8s部署mysql一主两从集群
1、安装NFS
yum -y install rpcbind nfs-utils #安装rpc跟nfs服务

mkdir /nfs && chmod 666 /nfs #创建指定共享目录并修改相应权限

vim /etc/exports #编辑文件 /nfs 10.1.2.0/24(insecure,rw,sync,no_root_squash,fsid=0) #保存退出

exportfs -rv #载入配置

启动服务： systemctl enable rpcbind --now #启动rpc服务并加入开机自启 systemctl enable nfs --now #启动nfs服务并加入开机自启

服务检查： showmount -e Export list for master: /nfs 10.1.2.0/24

客户端配置： mount -t nfs 10.1.2.20:/nfs /mnt #将服务nfs目录挂载至本机/mnt df -h #查看挂载结果

2、部署storageclass
编辑storageclass.yaml,确定provisioner的值

kubectl apply -f storageclass.yaml

kubectl get storageclass

3、部署nfs-client-provisioner
编辑nfs-client-provisioner.yaml,修改NFS服务器所在ip，共享存储目录，根据自己的名称来修改，与 storageclass.yaml 中的 provisioner 名字一致

kubect apply -f nfs-client-provisioner.yaml

kubectl get po -n kube-system

4、创建用于Mysql数据持久化的pvc
kubectl apply -f mysql-pvc.yaml

kubectl get pv,pvc

5、创建configmap
kubectl apply -f mysql-configmap.yaml

kubectl get cm

6、创建service
kubectl apply -f mysql-services.yaml

kubectl get svc

7、创建mysql-statefulset
yaml文件中的两个基础镜像需要提前准备，环境演示的时候会导出为tar包。 kubectl apply -f mysql-statefulset.yaml

kubectl get sts

kubectl get po 查看mysql pod有没有运行起来

kubectl get po

如果是3个pod都running,ready的状态，就表示集群创建成功了。