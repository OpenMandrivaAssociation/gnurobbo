Summary:	Logic game ported from ATARI XE/XL
Name:		gnurobbo
Version:	0.66
Release:	%mkrel 1
License:	GPLv2+
Group:		Games/Arcade
Source0:		http://prdownloads.sourceforge.net/gnurobbo/%{name}-%{version}-source.tar.gz
Source10:	%{name}.16.png.bz2
Source11:	%{name}.32.png.bz2
Source12:	%{name}.48.png.bz2
Patch0:		gnurobbo-0.66.libm.patch

URL:		http://gnurobbo.sourceforge.net

BuildRequires:	libSDL-devel
BuildRequires:	libSDL_ttf-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libSDL_mixer-devel
#Requires: libSDL1.2 >= 1.2.5
#Requires: libSDL_ttf2.0_0 >= 2.0.5

%description
GNU Robbo is very addictive logic game. You must help
little robot to get out of unfriendly planet, collecting
parts of emergency capsule.

%prep
%setup -q
%apply_patches

%build
%make PACKAGE_DATA_DIR=%{_datadir}/%{name}

%install
rm -rf %buildroot 
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


%changelog
* Sun Nov 28 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.66-1mdv2011.0
+ Revision: 602481
- remove old tarball
- correct use of %%buildroot
- little clean of spec file
- new version 0.66

* Wed Dec 30 2009 Crispin Boylan <crisb@mandriva.org> 0.65-1mdv2010.1
+ Revision: 483836
- BuildRequires SDL_mixer
- New release

* Fri May 15 2009 Samuel Verschelde <stormi@mandriva.org> 0.62-1mdv2010.0
+ Revision: 376151
- new version 0.82

* Tue Mar 03 2009 Crispin Boylan <crisb@mandriva.org> 0.61-1mdv2009.1
+ Revision: 347659
- New version, does not use configure

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.57-13mdv2009.0
+ Revision: 246501
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed Mar 19 2008 Emmanuel Andry <eandry@mandriva.org> 0.57-11mdv2008.1
+ Revision: 189023
- Drop useless requires

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.57-10mdv2008.1
+ Revision: 170871
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Tue Jan 22 2008 Crispin Boylan <crisb@mandriva.org> 0.57-9mdv2008.1
+ Revision: 156329
- Fix requires

* Mon Jan 21 2008 Crispin Boylan <crisb@mandriva.org> 0.57-8mdv2008.1
+ Revision: 155922
- Rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Funda Wang <fwang@mandriva.org> 0.57-7mdv2008.1
+ Revision: 119618
- rebuild to fix menu

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Mon Apr 30 2007 Crispin Boylan <crisb@mandriva.org> 0.57-6mdv2008.0
+ Revision: 19463
- XDG menu
- Import gnurobbo



* Mon Apr 28 2005 Giuseppe Ghibò <ghibo@mandrakesoft.com> 0.57-5mdk
- Fixed dep for x86-64.

* Thu Sep 02 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.57-4mdk
- fix menu

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com 0.57-3mdk
- rebuild

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 0.57-2mdk
- rebuild

* Sun Nov 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.57-1mdk 
- 0.57

* Fri Nov 08 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.56-1mdk
- add menu
- from Arkadiusz Lipiec <alipiec@elka.pw.edu.pl> :
	- Created
