#
# Conditional build:
%bcond_without	python2	# CPython 2.x version
%bcond_without	python3	# CPython 3.x version
%bcond_without	tests	# unit tests

Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.18.1
Release:	2
License:	Public Domain, BSD, GPL v3 (see COPYING.txt)
Group:		Development/Tools
# original URL, but only with major releases: http://downloads.sourceforge.net/docutils/%{name}-%{version}.tar.gz
#Source0Download: https://pypi.org/simple/docutils/
Source0:	https://files.pythonhosted.org/packages/source/d/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	ca5827e2432fd58f4c8d74a6591135de
URL:		http://docutils.sourceforge.net/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
# py3 patch assumes python3 lexer is the default, as it is since pygments 2.5.0
BuildRequires:	python-pygments >= 2.5.0
# a few tests fail with _xmlplus implementation of xml
BuildConflicts:	python-PyXML
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
# py3 patch assumes python3 lexer is the default, as it is since pygments 2.5.0
BuildRequires:	python3-pygments >= 2.5.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-%{name} = %{version}-%{release}
Obsoletes:	docutils-3 < 0.16-4
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
Requires:	python-libs >= 1:2.7

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

%package 2
Summary:        Documentation Utilities for Python 2.x
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji dla Pythona 2.x
Group:		Development/Tools
Requires:	python-%{name} = %{version}-%{release}

%description 2
Utilities for general- and special-purpose documentation, including
autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext
markup language.

This package provides the Docutils for Python 2.

%description 2 -l pl.UTF-8
Narzędzia do dokumentowania ogólnego i specjalnego zastosowania, w tym
autodokumentacji modułów Pythona. Zawierają reStructuredText - łatwy
do odczytania, łatwy w użyciu język opisu tekstu typu WYSIWYG.

Ten pakiet zawiera Docutils dla Pythona 2.

%package -n python3-%{name}
Summary:        Text documents processing modules for Python 3.x
Summary(pl.UTF-8):      Moduły Pythona 3.x do przetwarzania dokumentów tekstowych
Group:          Development/Languages/Python
Requires:	python3-libs >= 1:3.5

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

%if %{with tests}
PYTHONPATH=$(pwd)/build-2/lib \
%{__python} test/alltests.py
%endif
%endif

%if %{with python3}
%{__python3} setup.py config build -b build-3

%if %{with tests}
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} test/alltests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	%{__mv} "${f}" "${f%.py}-2"
done

%py_postclean
%endif

%if %{with python3}
%py3_install

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	%{__mv} "${f}" "${f%.py}"
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%files
%defattr(644,root,root,755)
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

%files -n python3-%{name}
%defattr(644,root,root,755)
%doc BUGS.txt COPYING.txt README.txt RELEASE-NOTES.txt THANKS.txt docs
%{py3_sitescriptdir}/docutils
%{py3_sitescriptdir}/docutils-%{version}-py*.egg-info
%endif

%if %{with python2}
%files 2
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rst*-2

%files -n python-%{name}
%defattr(644,root,root,755)
%doc BUGS.txt COPYING.txt README.txt RELEASE-NOTES.txt THANKS.txt docs
%{py_sitescriptdir}/docutils
%{py_sitescriptdir}/docutils-%{version}-py*.egg-info
%endif
