%define	name	xbill
%define	version	2.1
%define	release	%mkrel 5
%define	Summary	Defend your computers from Wingdows Viruses

Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Games/Arcade
Source0:	%{name}-%{version}.tar.bz2
Url:		http://www.xbill.org/
Summary:	%{Summary}
License:	GPL
BuildRequires:	X11-devel Xaw3d-devel imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Ever get the feeling that nothing is going right?  You're a sysadmin,
and someone's trying to destroy your computers.  The little people
running around the screen are trying to infect your computers with
Wingdows [TM], a virus cleverly  designed to resemble a popular
operating system.  Your objective is to click the mouse on them, ending
the potential threat. If one of the people reaches a computer, it will
attempt to replace your operating system with the virus it carries.
It will then attempt to run off the screen with your vital software.
If one of the people reaches a computer, it will attempt to replace
your operating system with the virus it carries. It will then attempt
to run off the screen with your vital software..

%prep
%setup -q

%build
%configure	--disable-gtk \
		--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--localstatedir=%{_localstatedir}/lib/games
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XBill
Comment=%{Summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -d $RPM_BUILD_ROOT{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 16x16 %{name}.gif $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert -size 32x32 %{name}.gif $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert -size 48x48 %{name}.gif $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.Ports ChangeLog
%attr(2755,root,games) %{_gamesbindir}/%{name}
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/xbill.6*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%attr(0664,root,games) %{_localstatedir}/lib/games/xbill/scores
%{_datadir}/applications/mandriva-%{name}.desktop
