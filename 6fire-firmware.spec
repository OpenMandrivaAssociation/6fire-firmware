%define	module	6fire

Summary:	Firmware files for the Terratec DMX 6Fire usb sound card
Name:		%{module}-firmware
Version:	1.23.0.02
Release:	5
Url:		http://ftp.terratec.de/Audio/DMX_6fire_USB/Updates
Source0:	%{url}/DMX_6fire_USB_Setup_%{version}_XP_Vista_7.exe
License:	Proprietary
Group:		System/Kernel and hardware
BuildArch:	noarch
BuildRequires:	p7zip

%description
This package contains the firmware needed for the Terratec DMX 6Fire usb sound
card devices to work.

%prep
%setup -c -T -q
7z x -aot -o. %{SOURCE0}
mv '$[153]/$[153]/$[154]_17' dmx6fireap.ihx
echo "7497b6b80d43e68f13b6929934ab60f4 dmx6fireap.ihx" | md5sum -c
mv '$[153]/$[153]/$[154]_18' dmx6firecf.bin
echo "a65eecc11adc87af7307f5266ad31d65 dmx6firecf.bin" | md5sum -c
mv '$[153]/$[153]/$[154]_16' dmx6firel2.ihx
echo "fa80973cb8c02097712933bd1d1c23b2 dmx6firel2.ihx" | md5sum -c

%build

%install
install -m644 dmx6fireap.ihx -D %{buildroot}/lib/firmware/6fire/dmx6fireap.ihx
install -m644 dmx6firecf.bin -D %{buildroot}/lib/firmware/6fire/dmx6firecf.bin
install -m644 dmx6firel2.ihx -D %{buildroot}/lib/firmware/6fire/dmx6firel2.ihx

%files
/lib/firmware/6fire/dmx6fireap.ihx
/lib/firmware/6fire/dmx6firecf.bin
/lib/firmware/6fire/dmx6firel2.ihx
