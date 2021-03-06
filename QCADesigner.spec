Summary: A QCA design and simulation tool
Name: QCADesigner
Version: 2.0.3
Release: 1
License: GPL
Group: Development/Tools
Source: http://qcadesigner.ca/dl/releases/2.0.3/QCADesigner-2.0.3-src.tar.gz
BuildRoot: /var/tmp/%{name}-buildroot
Vendor: Konrad Walus <qcadesigner@gmail.com> University of Calgary
Packager: Gabriel Schulhof <schulhof@atips.ca> University of Calgary
Requires: gtk2 >= 2.0

%description
QCADesigner allows you to create QCA-based circuit designs whose function
you can then simulate with the various built-in simulation engines. It is
a full-featured design tool, and it comes with three different simulation 
engines.

%prep
%setup -q

%build
./autogen.sh
CFLAGS="%optflags" CXXFLAGS="%optflags" ./configure --prefix=/usr
make

%install
make DESTDIR=%buildroot install

%clean
[ "/" != $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog CurrentVerChangeLog INSTALL README TODO docs/manual

/usr/bin/*
/usr/share/QCADesigner
/usr/share/locale/*/LC_MESSAGES/QCADesigner.mo
/usr/share/applications/*.desktop

%changelog
* Wed Jul 27 2005 Gabriel Schulhof <schulhof@atips.ca>
- Version 2.0.3
- Updated Windows version to use Gaim's GTK+ distribution
- Made Windows internationalization work
- Converted the layer mapping dialog to GtkTreeView, including a cell renderer for choosing a destination layer
- Fixed gtk_preamble, especially for Windows
- Updated manual to reflect new layer mapping dialog behaviour
- Version 2.0.2
- Brand new, more stable, better, cleaner, sharper, neater, greener, vector table dialog using GtkTreeView
- Fixed bugs related to cell function conversion
* Fri May 27 2005 Gabriel Schulhof <schulhof@atips.ca>
- Version 2.0.1
- Sub-nanometer cell sizes (via more digits and non-snap-to-tics in spin button)
- Ctrl+Shift+S == Save As
- Set file selection dialog to a more sensible default
- Both honeycomb and waveform drawing areas get created the same way - factor out the code
- Move the pixmap registration code out of main.c so other gtk targets can benefit from it
- Ability to horizontally stretch traces
* Fri May 27 2005 Gabriel Schulhof <schulhof@atips.ca>
- Packaging version 2.0.0
* Sat Oct 11 2003 Gabriel Schulhof <schulhof@atips.ca> 
- added RPM support
