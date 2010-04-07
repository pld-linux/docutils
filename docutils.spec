#
# TODO:
#	- check if ".py" suffix can be striped from the %{_bindir} scripts
#	  (*.py in %{_bindir} is generally a very bad idea)
#
Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.6
Release:	2
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	5c615479a965bc773892f585e0e08119
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

%description -l pl.UTF-8
Narzędzia do ogólnego i specjalnego dokumentowania, włączając
autodokumentację modułów pythona. Zawiera reStructuredText, łatwy do
odczytania, łatwy w użyciu, WYSIWYG język opisu tekstu.

%package -n python-%{name}
Summary:        Text documents processing modules for Python
Summary(pl.UTF-8):      Moduły Pythona do przetwarzania dokumentów tekstowych
Group:          Development/Languages/Python
%pyrequires_eq	python-libs

%description -n python-%{name}
Docutils are utilities for general- and special-purpose documentation,
including autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext markup
language.

This package provides the Docutils python modules.

%description -l pl.UTF-8 -n python-%{name}
Docutils to narzędzia do ogólnego i specjalnego dokumentowania, włączając
autodokumentację modułów pythona. Zawiera reStructuredText, łatwy do
odczytania, łatwy w użyciu, WYSIWYG język opisu tekstu.

Ten pakiet dostarcza modułów pythona Docutils.

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

install extras/roman.py $RPM_BUILD_ROOT%{py_sitescriptdir}
install tools/rstpep2html.py $RPM_BUILD_ROOT%{_bindir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/*

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[oc]
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*.egg-info
