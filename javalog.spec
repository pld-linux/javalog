Summary:	JavaLog
Summary(pl.UTF-8):   JavaLog
Name:		javalog
Version:	0.7.3
Release:	2
License:	MPL
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/%{name}/grace-%{version}.tar.gz
# Source0-md5:	bd444dbd1e6b9ad7eeafcb1978c2feb8
URL:		http://javalog.sourceforge.net/
BuildRequires:	gnu.regexp
BuildRequires:	jdk
Requires:	gnu.regexp
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
The JavaLog is a set of Java classes that formats and writes events to
one or more log devices. JavaLog frees the programmer from coding
inflexible "print" statements in his code. It offers an abstract
interface to the various log devices and allows the user to configure
each log device at run time. Additionally, JavaLog allows the user to
dynamically filter and format the logged events to suit his particular
needs at run time.

%description -l pl.UTF-8
JavaLog jest zestawem klas, który formatuje i zapisuje zdarzenia do
jednego lub więcej urządzeń logujących. JavaLog daje programiście o
wiele większe możliwości niż mało elastyczne instrukcje 'print'.
Oferuje mu abstrakcyjny interfejs do różnych urządzeń logujących oraz
umożliwia użytkownikowi skonfigurowanie każdego urządzenia w momencie
uruchomienia aplikacji. Dodatkowo, JavaLog umożliwia użytkownikowi,
odpowiednio do jego potrzeb, filtrowanie i formatowanie logowanych
zdarzeń.

%prep
%setup -q -n grace-%{version}

%build
#install -d dist
#find . -name \*.java | xargs javac -classpath classes:%{_javaclassdir}/gnu-regexp.jar -d dist -O
#( cd dist
#  jar cf ../grace.jar .
#)
find docs -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install lib/grace.jar $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_javaclassdir}/grace.jar
