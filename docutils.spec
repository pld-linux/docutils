#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.21.2
Release:	3
License:	Public Domain, BSD, GPL v3 (see COPYING.txt)
Group:		Development/Tools
# original URL, but only with major releases: http://downloads.sourceforge.net/docutils/%{name}-%{version}.tar.gz
#Source0Download: https://pypi.org/simple/docutils/
Source0:	https://pypi.debian.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	c4064e1e0e3cd142951fd2b95b830874
URL:		http://docutils.sourceforge.net/
BuildRequires:	python3-build
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-installer
%if %{with tests}
# py3 patch assumes python3 lexer is the default, as it is since pygments 2.5.0
BuildRequires:	python3-pygments >= 2.5.0
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

%package -n python3-%{name}
Summary:        Text documents processing modules for Python 3.x
Summary(pl.UTF-8):      Moduły Pythona 3.x do przetwarzania dokumentów tekstowych
Group:          Development/Languages/Python
Requires:	python3-modules >= 1:3.5
Requires:	python3-pygments

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

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      docutils/__main__.py \
      docutils/parsers/commonmark_wrapper.py \
      docutils/parsers/recommonmark_wrapper.py \
      docutils/utils/error_reporting.py \
      docutils/utils/math/math2html.py \
      docutils/utils/math/mathalphabet2unichar.py \
      docutils/utils/math/tex2unichar.py \
      docutils/writers/_html_base.py \
      docutils/writers/odf_odt/prepstyles.py \
      docutils/writers/xetex/__init__.py

%build
%{__python3} -m build --wheel --no-isolation --outdir build-3

%if %{with tests}
PYTHONPATH=$(pwd)/build-3/lib \
%{__python3} test/alltests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} -m installer --destdir=$RPM_BUILD_ROOT build-3/*.whl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/docutils
%attr(755,root,root) %{_bindir}/rst2html
%attr(755,root,root) %{_bindir}/rst2html4
%attr(755,root,root) %{_bindir}/rst2html5
%attr(755,root,root) %{_bindir}/rst2latex
%attr(755,root,root) %{_bindir}/rst2man
%attr(755,root,root) %{_bindir}/rst2odt
%attr(755,root,root) %{_bindir}/rst2pseudoxml
%attr(755,root,root) %{_bindir}/rst2s5
%attr(755,root,root) %{_bindir}/rst2xetex
%attr(755,root,root) %{_bindir}/rst2xml

%files -n python3-%{name}
%defattr(644,root,root,755)
%doc BUGS.txt COPYING.txt README.txt RELEASE-NOTES.txt THANKS.txt docs
%{py3_sitescriptdir}/docutils
%{py3_sitescriptdir}/docutils-%{version}*.dist-info
