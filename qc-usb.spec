Name:           qc-usb
Version:        0.6.6
Release:        3%{?dist}
Summary:        Utility for setting Logitech Quickcam Express

Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://qce-ga.sourceforge.net/
Source0:        http://downloads.sourceforge.net/qce-ga/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       %{name}-kmod >= %{version}
Provides:       %{name}-kmod-common = %{version}

%description
Utility qcset that complements kernel driver for Logitech Quickcam Express.


%prep
%setup -q

%build
# The included Makefile is badly written
%{__cc} %{optflags} -lm -o qcset qcset.c


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp qcset $RPM_BUILD_ROOT%{_bindir}


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_bindir}/qcset
%doc APPLICATIONS COPYING CREDITS FAQ README.qce TODO


%changelog
* Fri Oct 03 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.6.6-3
- rebuild for rpm fusion

* Sun Dec 02 2007 Lubomir Kundrak <lkundrak@redhat.com> - 0.6.6-2
- Rename kernel module from kmod-qc-usb to qc-usb-kmod

* Sat Dec 01 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.6.6-1
- Version bump

* Mon Sep 17 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.6.5-1
- Initial package
