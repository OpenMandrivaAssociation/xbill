Summary:	Defend your computers from Wingdows Viruses
Name:		xbill
Version:	2.1
Release:	8
Group:		Games/Arcade
Source0:	http://www.xbill.org/download/%{name}-%{version}.tar.gz
Url:		http://www.xbill.org/
License:	GPL
BuildRequires:	pkgconfig(x11)
BuildRequires:	Xaw3d-devel
BuildRequires:	pkgconfig(xpm)
BuildRequires:	pkgconfig(xt)
BuildRequires:	libxaw-devel
BuildRequires:	lesstif-devel
BuildRequires:	imagemagick

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
%configure2_5x	--disable-gtk \
		--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--localstatedir=%{_localstatedir}/lib/games
%make

%install
%{makeinstall_std}

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=XBill
Comment=%{Summary}
Exec=%_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

install -d %{buildroot}{%{_iconsdir},%{_miconsdir},%{_liconsdir}}
convert -size 16x16 %{name}.gif %{buildroot}%{_miconsdir}/%{name}.png
convert -size 32x32 %{name}.gif %{buildroot}%{_iconsdir}/%{name}.png
convert -size 48x48 %{name}.gif %{buildroot}%{_liconsdir}/%{name}.png

%files
%doc README README.Ports ChangeLog
%attr(2755,root,games) %{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/xbill.6*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%attr(0664,root,games) %{_localstatedir}/lib/games/xbill/scores
%{_datadir}/applications/mandriva-%{name}.desktop
