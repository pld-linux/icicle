Summary:	A simple streamer for IceCast
Name:		icicle
Version:	0.9
Release:	1
License:	GPL
Vendor:		Alexander Gräfe <nachtfalke@retrogra.de>
Group:		Applications/Graphics
Group(de):	Applikationen/Grafik
Group(pl):	Aplikacje/Grafika
Source0:	http://icicle.retrogra.de/%{name}-%{version}.tar.gz
URL:		http://icicle.retrogra.de/
BuildRequires:	lame-libs-devel
BuildRequires:	libshout-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple streamer for IceCast.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} -I%{_includedir}/lame"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/icicle
