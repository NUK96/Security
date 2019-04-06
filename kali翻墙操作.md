# kali翻墙操作记录 #

## 1、安装shadowsocket ##
    root@kali:~# apt-get install shadowsocks -y

## 2、安装privoxy ##
    root@kali:~# apt-get install privoxy 

## 3、编辑privoxy下的conf文件 ##
    root@kali:~# vi /etc/privoxy/config
查看privoxy监听的端口，一般是8118，如图所示 ：

