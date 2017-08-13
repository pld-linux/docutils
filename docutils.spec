#
# Conditional build:
%bcond_without	python2	# CPython 2.x version
%bcond_without	python3	# CPython 3.x version

Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.14
Release:	1
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	c53768d63db3873b7d452833553469de
URL:		http://docutils.sourceforge.net/
%if %{with python2}
BuildRequires:	python-devel >= 2.3
%endif
%if %{with python3}
BuildRequires:	python3-2to3 >= 1:3.6
BuildRequires:	python3-2to3 < 1:3.7
BuildRequires:	python3-devel >= 3.6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-%{name} = %{version}-%{release}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

%description -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

%package -n python-%{name}
Summary:        Text documents processing modules for Python 2.x
Summary(pl.UTF-8):      Moduły Pythona 2.x do przetwarzania dokumentów tekstowych
Group:          Development/Languages/Python
%pyrequires_eq	python-libs

%description -n python-%{name}
Docutils are utilities for general- and special-purpose documentation,
including autodocumentation of Python modules. Includes
reStructuredText, the easy to read, easy to use,
what-you-see-is-what-you-get plaintext markup language.

This package provides the Docutils modules for Python 2.

%description -n python-%{name} -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

Ten pakiet dostarcza moduły Docutils dla Pythona 2.

%package 3
Summary:        Documentation Utilities for Python 3.x
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji dla Pythona 3.x
Group:		Development/Tools
Requires:	python3-%{name} = %{version}-%{release}

%description 3
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

This package provides the Docutils for Python 3.

%description 3 -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

Ten pakiet zawiera Docutils dla Pythona 3.

%package -n python3-%{name}
Summary:        Text documents processing modules for Python 3.x
Summary(pl.UTF-8):      Moduły Pythona 3.x do przetwarzania dokumentów tekstowych
Group:          Development/Languages/Python

%description -n python3-%{name}
Docutils are utilities for general- and special-purpose documentation,
including autodocumentation of Python modules. Includes
reStructuredText, the easy to read, easy to use,
what-you-see-is-what-you-get plaintext markup language.

This package provides the Docutils modules for Python 3.

%description -n python3-%{name} -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

Ten pakiet dostarcza moduły Docutils dla Pythona 3.

%prep
%setup -q

%build
%if %{with python2}
%{__python} setup.py config build -b build-2
%endif

%if %{with python3}
%{__python3} setup.py config build -b build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	%{__mv} "${f}" "${f%.py}"
done

%py_postclean
%endif

%if %{with python3}
%py3_install

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	%{__mv} "${f}" "${f%.py}-3"
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/rst2html
%attr(755,root,root) %{_bindir}/rst2html4
%attr(755,root,root) %{_bindir}/rst2html5
%attr(755,root,root) %{_bindir}/rst2latex
%attr(755,root,root) %{_bindir}/rst2man
%attr(755,root,root) %{_bindir}/rst2odt
%attr(755,root,root) %{_bindir}/rst2odt_prepstyles
%attr(755,root,root) %{_bindir}/rst2pseudoxml
%attr(755,root,root) %{_bindir}/rst2s5
%attr(755,root,root) %{_bindir}/rst2xetex
%attr(755,root,root) %{_bindir}/rst2xml
%attr(755,root,root) %{_bindir}/rstpep2html

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/docutils
%{py_sitescriptdir}/docutils-%{version}-py*.egg-info
%endif

%if %{with python3}
%files 3
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/rst*-3

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/docutils
%{py3_sitescriptdir}/docutils-%{version}-py*.egg-info
%endif
