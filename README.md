# CyberWrt
CyberWrt OpenWrt package 

Оригинальная прошивка CyberWrt http://cyber-place.ru/showthread.php?t=720

Эта инструкция позволяет настроить установки под себя (сеть, набор модулей и т.д.)
добавить модули которые требуются
получить доступ к последним обновлениям openwrt


Инструкция для сборки на примере Сhaos Сalmer 15.05 и роутера TR-ML3020

если ещё не настраивалось окружение, то поставить зависимости
```
$ apt-get install subversion build-essential libncurses5-dev zlib1g-dev gawk git ccache gettext libssl-dev xsltproc
```
Требуется скачать SDK и ImageBuilder для выбранной ветки OpenWrt
```
$ cd /opt/
$ wget http://downloads.openwrt.org/chaos_calmer/15.05/ar71xx/generic/OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64.tar.bz2
$ tar -xvjf OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64.tar.bz2
$ wget https://downloads.openwrt.org/chaos_calmer/15.05/ar71xx/generic/OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64.tar.bz2
$ tar -xvjf OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64.tar.bz2
```
Далее получаем пакет CyberWrt
```
$ cd /opt/OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/package/
$ git clone https://github.com/Alx2000y/CyberWrt.git
```
Запуск сборки
```
$ cd /opt/OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64
$ make world
```
в папке /opt/OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/bin/ar71xx/packages/base/ появится файл CyberWrt_2_ar71xx.ipk который можно как установить на стандартный Openwrt, так и добавить в свою сборку.

Если требуется сборка:

закинуть полученный файл в папку:
```
$ cp /opt/OpenWrt-SDK-15.05-ar71xx-generic_gcc-4.8-linaro_uClibc-0.9.33.2.Linux-x86_64/bin/ar71xx/packages/base/CyberWrt_2_ar71xx.ipk /opt/OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64/packages/base/
```
Запустить сборку образа. Так как я сразу расширяю память на флешку, то добавляю модули ядра для поддержки флэшек
```
$ cd /opt/OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64
$ make image PROFILE=TLMR3020 PACKAGES="CyberWrt uhttpd kmod-usb-core kmod-usb-ohci kmod-usb-storage kmod-usb2 kmod-fs-ext4 block-mount"
```

Если не требуется поддержка флэшек, достаточно:
```
$ cd /opt/OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64
$ make image PROFILE=TLMR3020 PACKAGES="CyberWrt uhttpd"
```

Прошивка находится в /opt/OpenWrt-ImageBuilder-15.05-ar71xx-generic.Linux-x86_64/bin/ar71xx/

