%define name	gnurobbo
%define version	0.62
%define release	%mkrel 1

Summary: Logic game ported from ATARI XE/XL
Name:      %{name}
Version:   %{version}
Release:   %{release}
License: GPLv2+
Group: Games/Arcade
Source: http://prdownloads.sourceforge.net/gnurobbo/%{name}-%{version}.tar.gz
Source10: %{name}.16.png.bz2
Source11: %{name}.32.png.bz2
Source12: %{name}.48.png.bz2

URL: http://gnurobbo.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-buildroot

BuildRequires: libSDL-devel
BuildRequires: libSDL_ttf-devel
#Requires: libSDL1.2 >= 1.2.5
#Requires: libSDL_ttf2.0_0 >= 2.0.5

%description
GNU Robbo is very addictive logic game. You must help
little robot to get out of unfriendly planet, collecting
parts of emergency capsule.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%make PACKAGE_DATA_DIR=%{_datadir}/%{name}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall BINDIR=$RPM_BUILD_ROOT/%{_bindir} \
PACKAGE_DATA_DIR=$RPM_BUILD_ROOT/%{_datadir}/%{name} \
DOCDIR=$RPM_BUILD_ROOT/%{_docdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=GNU Robbo
Comment=%{summary}
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;
EOF

mkdir -p $RPM_BUILD_ROOT/%{_miconsdir}
mkdir -p $RPM_BUILD_ROOT/%{_liconsdir}
bzcat %{SOURCE10} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
bzcat %{SOURCE11} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE12} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
