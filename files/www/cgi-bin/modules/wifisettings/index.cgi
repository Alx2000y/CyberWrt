#!/bin/sh
#Copyright (C) 2013 cyberwrt.ru, carduino.ru, cyber-place.ru, mp3car.ru
shif=$(uci get wireless.@wifi-iface[0].encryption)
radios=$(uci get wireless.@wifi-iface[0].mode)
case "$radios" in
	sta ) upsun_check=checked
		upsun_block=block
		uptime_block=none;;
	ap ) uptime_check=checked
		uptime_block=block
		upsun_block=none;;
esac
case "$shif" in
	psk2+tkip+aes ) psk2_tkip_aes=selected;;
	psk2+tkip ) psk2_tkip=selected;;
	psk2+aes ) psk2_aes=selected;;
	psk2 ) psk2=selected;;
	psk+tkip+aes ) psk_tkip_aes=selected;;
	psk+tkip ) psk_tkip=selected;;
	psk ) psk=selected;;
	psk+aes ) psk_aes=selected;;
	none ) none=selected;;
esac
echo "Content-type: text/html; charset=utf-8"
echo
echo "
<title>WiFi Settings</title>
<style>input[type="radio"]{display:none;}
input[type=radio]:checked + label span{background: url(/modules/wifisettings/checkbox.png) no-repeat 0 -43px;}
input[type=radio] + label span {display:inline-block;width:34px;height:34px;margin:4px 4px 18px 0;vertical-align:middle;background: url(/modules/wifisettings/checkbox.png) no-repeat 0px 0px;cursor:pointer;}
</style>
<body>"
echo "<script language="javascript">"
echo "function Display(which) {"
echo "ut=document.getElementById('uptime');"
echo "us=document.getElementById('upsun');"
echo "if (which=='uptime') ut.style.display='block';
else ut.style.display='none';
  if (which=='upsun') us.style.display='block';
    else us.style.display='none';
}"
echo "</script>"
echo ""
echo `cat /www/menu.html`
echo "<table border=0 width=320><tr><td align=center><b>Выбор режима Wi-Fi:</b>"
echo "<form method="POST" action="wifi.cgi">"
echo "<input type=radio name=uptype id=rb1 value="ap""
echo "$uptime_check"
echo "onClick=Display('uptime');><label for=rb1><span></span>Точка доступа</label>"
echo "<input type=radio name=uptype id=rb2 value="client""
echo "$upsun_check"
echo "onClick=Display('upsun');><label for=rb2><span></span>Клиент WiFi сети</label>"
echo "</td></tr></table>"
echo "<div ID=uptime style=display:$uptime_block"
echo ";>"
echo "<table><tr><td>Имя Wi-Fi сети </td><td><input type=text name=net size=15 disabled value="CyberBot"></td></tr>
<tr><td>IP адрес:</td><td><input type=text name="ip" size=15 disabled value="
uci get network.lan.ipaddr
echo "></td></tr>
<tr><td>Пароль:</td><td><input type=text name="pass" size=15 value="
uci get wireless.@wifi-iface[0].key
echo "></td></tr></table></div>
<div ID=upsun style=display:$upsun_block"
echo ";>
<table><tr>
<td>Имя Wi-Fi сети</td><td><input type=text name="net" size=15 value="
uci get wireless.@wifi-iface[0].ssid
echo "></td></tr>
<tr><td>Ключ:</td><td><input type=text name="pass" size=15 value="
uci get wireless.@wifi-iface[0].key
echo "></td></tr>
<tr><td>Тип безопастности:</td><td><select size=1 name="type_saf">
<option "
echo "$none"
echo ">none</option><option "
echo "$psk2_tkip_aes"
echo ">psk2+tkip+aes</option><option "
echo "$psk2_tkip"
echo ">psk2+tkip</option><option "
echo "$psk2_ccmp"
echo ">psk2+ccmp</option><option "
echo "$psk2_aes"
echo ">psk2+aes</option><option "
echo "$psk2"
echo ">psk2</option><option "
echo "$psk_tkip_aes"
echo ">psk+tkip+aes</option><option "
echo "$psk_tkip"
echo ">psk+tkip</option><option "
echo "$psk"
echo ">psk</option><option "
echo "$psk_aes"
echo ">psk+aes</option></select></td></tr>
<tr><td>IP адрес:</td><td><input type=text name="ip_cl" size=15 value="
uci get network.wwan.ipaddr
echo "></td></tr>
<tr><td>Маска:</td><td><input type=text name="mask" size=15 value="
uci get network.wwan.netmask
echo "></td></tr>
<tr><td>Шлюз:</td><td><input type=text name="gateway" size=15 value="
uci get network.wwan.gateway
echo "></td></tr></table></div>
<table border=0 width=320><tr><td align=center><br>
<input class=submit type=submit value=SAVE name=commit>
</td></tr></table></form>"
#echo "<iframe name=hidden src=/free.html style=width: 0px; height: 0px; visibility: hidden></iframe></body>"