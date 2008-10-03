Summary:	Documentation Utilities
Summary(pl.UTF-8):	Narzędzia do tworzenia dokumentacji
Name:		docutils
Version:	0.5
Release:	2
License:	Public Domain, BSD, GPL (see COPYING.txt)
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/docutils/%{name}-%{version}.tar.gz
# Source0-md5:	dd72dac92fc8e3eb0f48c3effeef80f6
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

%description -l pl.UTF-8
Narzędzia do ogólnego i specjalnego dokumentowania, włączając
autodokumentację modułów pythona. Zawiera reStructuredText, łatwy do
odczytania, łatwy w użyciu, WYSIWYG język opisu tekstu.

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
%{py_sitescriptdir}/*.py[oc]
%{py_sitescriptdir}/%{name}
