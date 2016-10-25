Name:       sailfishos-fake-data-patch

BuildArch: noarch

Summary:    Fake data for presentation purposes
Version:    0.1.0
Release:    1
Group:      Qt/Qt
License:    Other
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:   sailfish-version = 2.0.4

%description
Fake data for presentation purposes. Allow changing Operator names, IMEI, Bluetooth and WLAN MAC

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/sailfishos-fake-data-patch
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/sailfishos-fake-data-patch
#mkdir -p %{buildroot}/usr/share/jolla-settings/pages/sailfishos-fake-data-patch
#cp -r settings/*.qml %{buildroot}/usr/share/jolla-settings/pages/sailfishos-fake-data-patch
#cp -r settings/*.png %{buildroot}/usr/share/jolla-settings/pages/sailfishos-fake-data-patch
#mkdir -p %{buildroot}/usr/share/jolla-settings/entries
#cp -r settings/*.json %{buildroot}/usr/share/jolla-settings/entries/

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-fake-data-patch ]; then
/usr/sbin/patchmanager -u sailfishos-fake-data-patch || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/sailfishos-fake-data-patch ]; then
/usr/sbin/patchmanager -u sailfishos-fake-data-patch || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/sailfishos-fake-data-patch
#%{_datadir}/jolla-settings/entries
#%{_datadir}/jolla-settings/pages