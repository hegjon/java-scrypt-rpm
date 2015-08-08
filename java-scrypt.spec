Name: java-scrypt
Version: 1.4.0
Release: 1%{?dist}
Summary: Java implementation of scrypt

License: ASL 2.0
URL: http://github.com/wg/scrypt
Source0: https://github.com/wg/scrypt/archive/1.4.0.tar.gz
Patch0: no-jni.patch
BuildArch: noarch

BuildRequires: maven-local

%description
A pure Java implementation of the scrypt key derivation function.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n scrypt-%{version}

%patch0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.jar' -print -delete

%build
#Disble tests, since of them are releated to JNI
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc README
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README
%license LICENSE

%changelog
* Sat Aug 08 2015 Jonny Heggheim <hegjon@gmail.com> - 1.4.0-1
- Inital packaging
