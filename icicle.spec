#
# $Id: icicle.spec,v 1.1 2001-05-06 14:28:06 jack Exp $
#
%define prefix          /usr
%define sysconfdir      /etc
%define  RELEASE 1
%define  rel     %{?CUSTOM_RELEASE} %{!?CUSTOM_RELEASE:%RELEASE}

Name: icicle
Version: 0.9
Summary: A simple streamer for IceCast
Release: %rel
Source: http://retrogra.de/icicle-%{version}.tar.gz

Copyright: GPL
Group: Console/Multimedia
URL: http://icicle.retrogra.de/
Vendor: Alexander Gräfe <nachtfalke@retrogra.de>
BuildRoot: /var/tmp/icicle-%{version}.root

%description
This is a very simple streamer for IceCast.


%prep
%setup  -n icicle-%{version}



%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=/usr
make

%install
mkdir -p $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT/usr install

%files
%defattr(-,root,root)
/usr/bin/icicle
%doc README AUTHORS COPYING ChangeLog INSTALL NEWS TODO 

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Jan 13 2001 Alexander Gräfe <nachtfalke@retrogra.de>
 - inital version of the RPM.
