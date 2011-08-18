Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.8
Release:	1
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	f57474b69bfbf0eb608706a104f92dda
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel >= 2.3
BuildRequires:	python3-2to3 >= 3.2
BuildRequires:	python3-devel >= 3.2
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
%{__python} setup.py config build -b build-2
%{__python3} setup.py config build -b build-3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py build -b build-2 install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	mv "${f}" "${f%.py}"
done

%{__python3} setup.py build -b build-3 install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	mv "${f}" "${f%.py}-3"
done

install extras/roman.py $RPM_BUILD_ROOT%{py_sitescriptdir}
install extras/roman.py $RPM_BUILD_ROOT%{py3_sitescriptdir}
2to3-3.2 -n -w $RPM_BUILD_ROOT%{py3_sitescriptdir}/roman.py
# clean some 2to3 leftovers
%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/{test,tools}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/rst2html
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
%{py_sitescriptdir}/roman.py[oc]
%{py_sitescriptdir}/docutils
%{py_sitescriptdir}/docutils-%{version}-py*.egg-info

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/roman.py
%{py3_sitescriptdir}/__pycache__/roman.cpython-*.py[co]
%{py3_sitescriptdir}/docutils
%{py3_sitescriptdir}/docutils-%{version}-py*.egg-info
