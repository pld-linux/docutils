Summary:	Documentation Utilities
Summary(pl):	Narzêdzia do tworzenia dokumentacji
Name:		docutils
Version:	0.3.9
Release:	1
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	3b6727e4f53e88ae7cea7c296694fc6c
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel
%pyrequires_eq	python-libs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

%description -l pl
Narzêdzia do ogólnego i specjalnego dokumentowania, w³±czaj±c
autodokumentacjê modu³ów pythona. Zawiera reScructeredText, ³atwy do
odczytania, ³atwy w u¿yciu, WYSIWYG jêzyk opisu tekstu.

%prep
%setup -q

%build
python setup.py config
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/%{name}
%dir %{py_sitescriptdir}/%{name}/languages
%dir %{py_sitescriptdir}/%{name}/parsers
%dir %{py_sitescriptdir}/%{name}/parsers/rst
%dir %{py_sitescriptdir}/%{name}/parsers/rst/directives
%dir %{py_sitescriptdir}/%{name}/parsers/rst/languages
%dir %{py_sitescriptdir}/%{name}/readers
%dir %{py_sitescriptdir}/%{name}/readers/python
%dir %{py_sitescriptdir}/%{name}/writers
%dir %{py_sitescriptdir}/%{name}/transforms
%{py_sitescriptdir}/%{name}/*.py[oc]
%{py_sitescriptdir}/%{name}/languages/*.py[oc]
%{py_sitescriptdir}/%{name}/parsers/*.py[oc]
%{py_sitescriptdir}/%{name}/parsers/rst/*.py[oc]
%{py_sitescriptdir}/%{name}/parsers/rst/directives/*.py[oc]
%{py_sitescriptdir}/%{name}/parsers/rst/languages/*.py[oc]
%{py_sitescriptdir}/%{name}/readers/*.py[oc]
%{py_sitescriptdir}/%{name}/readers/python/*.py[oc]
%{py_sitescriptdir}/%{name}/writers/*.py[oc]
%{py_sitescriptdir}/%{name}/transforms/*.py[oc]
