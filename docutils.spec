#
Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.8
Release:	1
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	f57474b69bfbf0eb608706a104f92dda
URL:		http://docutils.sourceforge.net/
BuildRequires:	python-devel
BuildRequires:	python3-2to3
BuildRequires:	python3-devel
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

%description -n python-%{name} -l pl.UTF-8
Docutils to narzędzia do ogólnego i specjalnego dokumentowania, włączając
autodokumentację modułów pythona. Zawiera reStructuredText, łatwy do
odczytania, łatwy w użyciu, WYSIWYG język opisu tekstu.

Ten pakiet dostarcza modułów pythona Docutils.

%package -n python3-%{name}
Summary:        Text documents processing modules for Python
Summary(pl.UTF-8):      Moduły Pythona do przetwarzania dokumentów tekstowych
Group:          Development/Languages/Python
%pyrequires_eq	python-libs

%description -n python3-%{name}
Docutils are utilities for general- and special-purpose documentation,
including autodocumentation of Python modules. Includes reStructuredText, the
easy to read, easy to use, what-you-see-is-what-you-get plaintext markup
language.

This package provides the Docutils python modules.

%description -n python3-%{name} -l pl.UTF-8
Docutils to narzędzia do ogólnego i specjalnego dokumentowania, włączając
autodokumentację modułów pythona. Zawiera reStructuredText, łatwy do
odczytania, łatwy w użyciu, WYSIWYG język opisu tekstu.

Ten pakiet dostarcza modułów pythona Docutils.

%prep
%setup -q

%build
%{__python} setup.py build -b build-2 config
%{__python} setup.py build -b build-2

%{__python3} setup.py build -b build-3 config
%{__python3} setup.py build -b build-3

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py \
    build -b build-2 \
    install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	mv "${f}" "${f%.py}-%{py_ver}"
done

%{__python3} setup.py \
    build -b build-3 \
    install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

for f in $RPM_BUILD_ROOT%{_bindir}/*.py ; do
	mv "${f}" "${f%.py}-%{py3_ver}"
done

install extras/roman.py $RPM_BUILD_ROOT%{py_sitescriptdir}
install extras/roman.py $RPM_BUILD_ROOT%{py3_sitescriptdir}

%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/*-2.?

%files -n docutils
%defattr(644,root,root,755)
%doc PKG-INFO *.txt docs
%attr(755,root,root) %{_bindir}/*-3.?

%files -n python-%{name}
%defattr(644,root,root,755)
%{py_sitescriptdir}/*.py[oc]
%{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}*.egg-info

%files -n python3-%{name}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/*.py
%{py3_sitescriptdir}/__pycache__
%{py3_sitescriptdir}/%{name}
%{py3_sitescriptdir}/%{name}*.egg-info
