Summary:	A simple streamer for IceCast
Summary(pl.UTF-8):	Prosty generator strumieni IceCast
Name:		icicle
Version:	0.9
Release:	1
License:	GPL
Vendor:		Alexander Gräfe <nachtfalke@retrogra.de>
Group:		Applications/Graphics
Source0:	http://icicle.retrogra.de/%{name}-%{version}.tar.gz
# Source0-md5:	88749e610407a96a370085cdb119c758
URL:		http://icicle.retrogra.de/
BuildRequires:	lame-libs-devel
BuildRequires:	libshout-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a very simple streamer for IceCast.

%description -l pl.UTF-8
To jest bardzo prosty generator strumieni IceCast.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/icicle
