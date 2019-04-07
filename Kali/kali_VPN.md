# kali翻墙操作记录 #

## 1、安装shadowsocket ##
    root@kali:~# apt-get install shadowsocks -y

## 2、安装privoxy ##
    root@kali:~# apt-get install privoxy 

## 3、编辑privoxy下的conf文件 ##
    root@kali:~# vi /etc/privoxy/config
查看privoxy监听的端口，一般是8118，如图所示 ：  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/%E7%9B%91%E5%90%AC%E7%AB%AF%E5%8F%A3.jpg)  
然后启用socks5转发，如图所示：  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/%E5%90%AF%E7%94%A8socks5.png)  
## 4、配置shadowsocks的json文件 ##
修改json中的服务器端的配置：

	root@kali:~# cd /etc/shadowsocks/
	root@kali:/etc/shadowsocks# cp local.json US.json
然后修改US,json文件：
  
    root@kali:/etc/shadowsocks# vi US.json
修改信息如图所示：  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/USJson%E4%BF%AE%E6%94%B9%E4%BF%A1%E6%81%AF.png)  
## 5、启动privoxy服务 ##    
    root@kali:/etc/shadowsocks# service privoxy start

## 6、编译运行US.json文件 ##
    root@kali:/etc/shadowsocks# sslocal -c US.json

## 7、验证 ##
打开firefox，在VPN中设置如下：  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/firefox.png)  

打开油瓶网验证一下  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/youtube.png)

OK，完毕！
但其实到这不能说完全完毕，因为当你在kali中使用其他的软件需要翻墙时，需要provixychains来进行代理，所以接下来我们继续配置provixychains

## 8、设置proxychain.conf文件##
    root@kali:vi /etc/proxychain.conf
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/proxychains.png)

## 9、再次验证 ##
通过proxyresolv对谷歌网站进行解析验证，但是由于proxyresolv默认实在proxychains3中，所以我们需要将他移到/usr/bin中

    root@kali:/etc/shadowsocks# cp /usr/lib/proxychains3/proxyresolv /usr/bin/

## 10、再再次验证 ##
启动US.json

    root@kali:/etc/shadowsocks# sslocal -c US.json -d start
解析验证  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/jiexi.png)  
![](https://github.com/NuLiDeXiaoBai/Security/blob/master/Kali/images/daili.png)  

完成，大功告成！

注：  
1、关于免费的VPN服务器的获取，可以去https://free-ss.site网站  
2、以后使用的步骤如下：  

	root@kali:~# cd /etc/shadowsocks/
	root@kali:/etc/shadowsocks# sslocal -c US.json -d start
	root@kali:/etc/shadowsocks# proxyresolv www.google.com
