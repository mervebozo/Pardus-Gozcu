USER=$(who am i | awk '{print $1}')
DIR=$(dirname "$(readlink -f "$0")")	
DESKTOP=$(su - $USER -c 'echo $(xdg-user-dir DESKTOP)')
if [ $(dpkg-query -W -f='${Status}' python-tk 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
	echo "Bu uygulama 'python-tk' paketinin kurulu olmasını gerektirir."; exit 0
fi
if [ $(dpkg-query -W -f='${Status}' iptables-persistent 2>/dev/null | grep -c "ok installed") -eq 0 ];
then
	echo "Bu uygulama 'iptables-persistent' paketinin kurulu olmasını gerektirir."; exit 0
fi
echo "Bu uygulamayı kurmak root parolası gerektirir."
mkdir /usr/local/pardusgozcu/appSettings
echo "[Desktop Entry]\nVersion=1.0\nName=Pardus Gözcü\nComment=Pardus için Ebeveyn Kontrolü Aracı\nIcon=$DIR/pardusgozcu.ico\nExec=gksu -u root $DIR/gui.py\nPath=$DIR/\nType=Application" > $DESKTOP/Pardus\ Gözcü.desktop
chown $USER $DESKTOP/Pardus\ Gözcü.desktop
chmod 700 $DESKTOP/Pardus\ Gözcü.desktop
cd /usr/local/pardusgozcu/appSettings
touch karaliste.txt kelime.txt netkisit.txt uygulamalar.txt zamankisit.txt ayarlar.txt
echo "$ sitesi sistem yoneticisi tarafindan engellendi.\n$ sitesine sistem yoneticisi tarafindan izin verildi.\n$ kelimesi sistem yoneticisi tarafindan engellendi.\n$ kelimesine sistem yoneticisi tarafindan izin verildi.\nInternet erisiminiz sistem yoneticisi tarafindan engellendi.\nInternet erisimine sistem yoneticisi tarafindan izin verildi.\n3 dk. sonra sistemden cikis yapacaksiniz. X dk. sonra sistemi tekrar kullanmaya baslayabilirsiniz.\n$ uygulamasi sistem yoneticisi tarafindan engellendi.\n$ uygulamasina sistem yoneticisi tarafindan izin verildi.\n$ uygulamasi sistem yoneticisi tarafindan durduruldu.\n$ uygulamasi sistem yoneticisi tarafindan durduruldu/yasaklandi.\nOxygen\nTrue\n5" > ayarlar.txt
echo $USER >> ayarlar.txt
mkdir log
echo $USER	ALL='(root)' NOPASSWD: $(which python) >> /etc/sudoers
echo $USER	ALL='(root)' NOPASSWD: /usr/local/pardusgozcu/gui.py >> /etc/sudoers
sudo su -c "cp -R /usr/lib/kde4/plugins/styles/ /usr/lib/qt4/plugins/styles; chmod 700 log; chmod 700 karaliste.txt; chmod 700 kelime.txt; chmod 700 netkisit.txt; chmod 700 uygulamalar.txt; chmod 700 zamankisit.txt; chmod 700 ayarlar.txt; cd ..; python gui.py&"
