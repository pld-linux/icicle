Summary:	A simple streamer for IceCast
Name:		icicle
Version:	0.9
Release:	1
Source0:	http://icicle.retrogra.de/%{name}-%{version}.tar.gz
URL:		http://icicle.retrogra.de/
License:	GPL
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Vendor:		Alexander Gräfe <nachtfalke@retrogra.de>
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple streamer for IceCast.

%prep
%setup -q


%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/icicle
%doc README AUTHORS COPYING ChangeLog INSTALL NEWS TODO 

%clean
rm -rf $RPM_BUILD_ROOT
