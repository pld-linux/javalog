Summary:	JavaLog
Summary(pl):	JavaLog
Name:		javalog
Version:	0.7.3
Release:	1
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Url:		http://javalog.sourceforge.net
Source0:	http://prdownloads.sourceforge.net/%{name}/grace-%{version}.tar.gz
License:	Mozilla Public License
BuildRequires:	gnu.regexp
Requires:	gnu.regexp
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java/

%description
The JavaLog is a set of Java classes that formats and writes events to
one or more log devices. JavaLog frees the programmer from coding
inflexible "print" statements in his code. It offers an abstract
interface to the various log devices and allows the user to configure
each log device at run time. Additionally, JavaLog allows the user to
dynamically filter and format the logged events to suit his particular
needs at run time.

%description -l pl
JavaLog jest zestawem klas, który formatuje i zapisuje zdarzenia do
jednego lub wiêcej urz±dzeñ loguj±cych. JavaLog daje programi¶cie o
wiele wiêksze mo¿liwo¶ci ni¿ ma³o elastyczne instrukcje 'print'.
Oferuje mu abstrakcyjny interfejs do ró¿nych urz±dzeñ loguj±cych oraz
umo¿liwa u¿ytkownikowi skonfigurowanie ka¿dego urz±dzenia w momencie
uruchomienia aplikacji. Dodatkowo, JavaLog umo¿liwia u¿ytkownikowi,
odpowiednio do jego potrzeb, filtrowanie i formatowanie logowanych
zdarzeñ.

%prep
%setup -q -n grace-%{version}

%build
find . -name \*.class -exec rm {} \;
install -d dist
find . -name \*.java | xargs javac -classpath classes:%{_libdir}/java/gnu-regexp.jar -d dist -O
( cd dist
  jar cf ../grace.jar .
)
find docs -name CVS | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javaclassdir}
install grace.jar $RPM_BUILD_ROOT%{_javaclassdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_javaclassdir}/grace.jar
