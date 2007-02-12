Summary:	diffutils for binary files
Summary(pl.UTF-8):	diffutils dla plików binarnych
Name:		bdiff
Version:	1.0.5
Release:	1
License:	GPL
Group:		Applications/Console
Source0:	http://xoomer.virgilio.it/g_pochini/%{name}-%{version}.tgz
# Source0-md5:	55e52c93565db80f18d9aa2d39a0ed58
Patch0:		%{name}-Makefile.patch
URL:		http://xoomer.virgilio.it/g_pochini/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bdiff is a simple and small program to do what the very common
utilities "diff" and "patch" do with text files, but also works with
binary files.

%description -l pl.UTF-8
bdiff jest prostym i niewielkim programem służącym do tego, do czego
używane są popularne narzędzia "diff" oraz "patch" - z tą różnicą, że
działa nie tylko na plikach tekstowych, a także binarnych.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install bdiff $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Fileformat.txt README magic.txt
%attr(755,root,root) %{_bindir}/*
