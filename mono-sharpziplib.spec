Name:		mono-sharpziplib
Version:	0.86.0
Release:	%mkrel 2
Summary:	Client Zip library written in C#
URL:		http://www.icsharpcode.net/OpenSource/SharpZipLib/Default.aspx
# Exception: Permission is given to use this library in commercial closed-source applications
# See: README.txt
License:	GPLv2+ with exceptions
Group:		Development/Other
Source0:	SharpZipLib_0860_SourceSamples.zip
Source1:	sharpziplib.pc
Patch0:		SharpZipLib-0.86-mono-build.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	nant 
BuildRequires:	unzip
BuildArch: noarch

%description
Gives C# projects the ability to work with Zip archives.

%package devel
Summary:	Client Zip library written in C#
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}


%description devel
Gives C# projects the ability to work witz Zip archives.

%prep
%setup -q -c -n %name-%{version}
# We need this to compile.
%patch0 -p0
# Get rid of the binary dlls
rm ./SrcSamples/samples/HttpCompressionModule/src/refs/SharpZipLib.dll

%build
cd SrcSamples
# Use the mono system key instead of generating our own here.
%if %mdvver >= 201100
cp -a /etc/pki/mono/mono.snk ICSharpCode.SharpZipLib.key
%endif
nant

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT/%_datadir/pkgconfig
cp %{S:1} $RPM_BUILD_ROOT/%_datadir/pkgconfig
%{__mkdir_p} $RPM_BUILD_ROOT/%_prefix/lib/mono/gac/
gacutil -i SrcSamples/bin/ICSharpCode.SharpZipLib.dll -f -package sharpziplib -root ${RPM_BUILD_ROOT}/%_prefix/lib

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%_prefix/lib/mono/gac/ICSharpCode.SharpZipLib*/
%_prefix/lib/mono/sharpziplib/

%files devel
%defattr(-,root,root,-)
%doc SrcSamples/doc/*
%_datadir/pkgconfig/sharpziplib.pc



%changelog
* Sat Oct 15 2011 Götz Waschk <waschk@mandriva.org> 0.86.0-2mdv2012.0
+ Revision: 704776
- rebuild

* Thu Oct 14 2010 Götz Waschk <waschk@mandriva.org> 0.86.0-1mdv2011.0
+ Revision: 585721
- import mono-sharpziplib

