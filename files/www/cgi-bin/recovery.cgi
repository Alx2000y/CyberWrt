#!/bin/sh
echo "Content-type: text/html; charset=utf-8"
echo
lib=`echo "$QUERY_STRING" | sed -n 's/^.*lib=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
www=`echo "$QUERY_STRING" | sed -n 's/^.*www=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
etc=`echo "$QUERY_STRING" | sed -n 's/^.*etc=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
all=`echo "$QUERY_STRING" | sed -n 's/^.*all=\([^&]*\).*$/\1/p' | sed "s/%20/ /g"`
if echo "$QUERY_STRING" | egrep -q "confirm=" ; then
if [ "$lib" = "ON" ] ; then
rm -rf /overlay/lib
rm -rf /overlay/usr
fi
if [ "$www" = "ON" ] ; then
rm -rf /overlay/www
fi
if [ "$etc" = "ON" ] ; then
rm -rf /overlay/etc
fi
if [ "$all" = "ON" ] ; then
for param in `ls /overlay` ; do
if [ "$param" != "www" -a "$param" != "etc" -a "$param" != "lib" -a "$param" != "usr" ] ; then
rm -rf /overlay/$param
fi
done
fi
sync
echo "Выполняется!<br>"
sleep 2
echo "Устройство перезагрузится через <b><span id="time"></span></b> секунд.
<script type="text/javascript">var i = 30; function time(){ document.getElementById(\"time\").innerHTML = i; i--; if (i < 0) location.href = \"/index.html\"; }
time(); setInterval(time, 1000); </script>"
`reboot`
exit 0
fi
echo "<script>function confirm1(f) { if (confirm(\"Откатить к первоначальному состоянию, с сохранением настроек? Это займет около 30 секунд.\")) f.submit(); }
function reboot() {if (confirm(\"Перезагрузть? Это займет около 30 секунд.\")) window.location.href = \"$SCRIPT_NAME?confirm=\";}
</script>`cat /www/menu.html`<h1>Востановление к начальным установкам</h1><form action=$SCRIPT_NAME methot=GET onsubmit=\"confirm1(this);return false;\"><input type=checkbox name=lib value=ON>Удалить установленные пакеты?<br>
<input type=checkbox name=www value=ON>Востановить папку www?<br>
<input type=checkbox name=etc value=ON onClick=\"javascript:alert('Это приведет к сбросу всех настроек!!!');\">Востановить настройки (удалить папку etc)?<br>
<input type=checkbox name=all value=ON>Удалить все пользовательские файлы?<br>
<button title=Восстановить? type=submit name=confirm>Выполнить и перезагрузить</button></form>
<button onClick=\"reboot();\">Перезагрузить</button>"