#!/usr/bin/awk -f
#Copyright (C) 2013 cyberwrt.ru, carduino.ru, cyber-place.ru, mp3car.ru
function unescape(s)
{
gsub(/\+/," ",s)
res = ""
	do {
	  p = match(s,/%[0-9a-fA-F]{2}/)
	  if(p>0) {
	  res = res substr(s,0,p-1) sprintf("%c",0+("0x" substr(s,p+1,2)))
	  s = substr(s,p+3)
	  }
	} while(p>0)
	return res s
}
BEGIN
{
RS = "&"
FS = "="
print "Content-type: text/html; charset=utf-8"
print ""
}
{
	system("uci set wireless.radio0.channel=auto")
	system("uci set wireless.radio0.disabled=0")
	system("uci set wireless.radio0.country=RU")
	system("uci set wireless.@wifi-iface[0]=wifi-iface")
	system("uci set wireless.@wifi-iface[0].device=radio0")
	system("uci set network.wwan=interface")
	system("uci set network.wwan.dns=8.8.8.8")

	if($1 == "uptype" && $2 == "client")
	{
	stat = 0
	system("uci set network.wwan.proto=static")
	system("uci set wireless.@wifi-iface[0].mode=sta")
	system("uci set wireless.@wifi-iface[0].network=wwan")
	system("uci set network.lan.ipaddr=192.168.100.100")
	}

	if($1 == "uptype" && $2 == "ap")
	{
	stat = 1
	system("uci set wireless.@wifi-iface[0].mode=ap")
	system("uci set wireless.@wifi-iface[0].network=lan")
	system("uci set wireless.@wifi-iface[0].ssid=CyberWrt")
	}
	if($1 == "net" && stat == 0)
	{
	system("uci set wireless.@wifi-iface[0].ssid='" unescape($2) "'")
	}
	if($1 == "type_saf")
	{
	system("uci set wireless.@wifi-iface[0].encryption='" unescape($2) "'")
	}
	if($1 == "pass")
	{
	system("uci set wireless.@wifi-iface[0].key='" unescape($2) "'")
	}
	if($1 == "ip_cl")
	{
	system("uci set network.wwan.ipaddr='" unescape($2) "'")
	}
	if($1 == "gateway")
	{
	system("uci set network.wwan.gateway='" unescape($2) "'")
	}
	if($1 == "mask")
	{
	system("uci set network.wwan.netmask='" unescape($2) "'")
	}
	print "Сохранено - "
	print $2
	print "<br>"

	if($1 == "commit")
	{
	system("uci commit network")
	system("uci commit wireless; wifi")
	print "<br>Ожидайте 5 секунд..."
	system("/etc/init.d/network restart")
	system("wifi up")
	}
}
END
{
print "202"
print "<br>Готово."
print "<br><a href=index.cgi>К настройкам</a>"
}