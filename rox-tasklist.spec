%define _name Tasklist
%define _platform %(echo `uname -s`-`uname -m|sed 's/i.86/ix86/'`)
Summary:	Simple tasklist
Summary(pl):	Prosta lista zadañ
Name:		rox-tasklist
Version:	0.5
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://sheen.fallingsnow.net/Software/%{_name}-%{version}.tgz
# Source0-md5:	b84faa84cb7a79e72b8b08f1aebf717f
URL:		http://rox.sourceforge.net/phpwiki/index.php/Tasklist
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libwnck-devel >= 0.14
BuildRequires:	libxml2-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	rox >= 2.2.0-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
This is a tasklist, much like the one that GNOME has.

%description -l pl
Jest to lista zadañ, podobna do tej, jak± posiada GNOME.

%prep
%setup -q -n %{_name}-%{version}

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/{%{_platform},Help}

install .DirIcon *Run *.xml $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install %{_platform}/Tasklist $RPM_BUILD_ROOT%{_appsdir}/%{_name}/%{_platform}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Help/Changes
%attr(755,root,root) %{_appsdir}/%{_name}/*Run
%attr(755,root,root) %{_appsdir}/%{_name}/%{_platform}
%{_appsdir}/%{_name}/Help
%{_appsdir}/%{_name}/.DirIcon
%{_appsdir}/%{_name}/*.xml
%dir %{_appsdir}/%{_name}
