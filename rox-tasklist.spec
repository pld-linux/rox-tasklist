%define _name ROX-Tasklist
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Simple tasklist
Summary(pl):	Prosta lista zadañ
Name:		rox-tasklist
Version:	0.1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://metabocks.port5.com/rox/%{name}.tar.gz
# Source0-md5:	d14e853551be5ab45e7e9b3ae0b80492
URL:		http://www.metabocks.com/rox/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gtk+-devel
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
This is a tasklist, much like the one that GNOME has.

%description -l pl
Jest to lista zadañ, podobna do tej, jak± posiada GNOME.

%prep
%setup -q -n %{name}

%build
echo -ne "\n" | ./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

install App* rox-tasklist $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/{BUGS,TODO}
%attr(755,root,root) %{_appsdir}/%{_name}/App*
%attr(755,root,root) %{_appsdir}/%{_name}/rox-tasklist
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
