#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jmxutils
Version  : 1.19
Release  : 1
URL      : https://github.com/martint/jmxutils/archive/1.19.tar.gz
Source0  : https://github.com/martint/jmxutils/archive/1.19.tar.gz
Source1  : https://repo1.maven.org/maven2/org/weakref/jmxutils/1.19/jmxutils-1.19.jar
Source2  : https://repo1.maven.org/maven2/org/weakref/jmxutils/1.19/jmxutils-1.19.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-jmxutils-data = %{version}-%{release}
Requires: mvn-jmxutils-license = %{version}-%{release}

%description
# Example
```java
class ManagedObject
@Managed
public int getValue()
{
...
}
@Managed
public void setValue(int value)
{
...
}

%package data
Summary: data components for the mvn-jmxutils package.
Group: Data

%description data
data components for the mvn-jmxutils package.


%package license
Summary: license components for the mvn-jmxutils package.
Group: Default

%description license
license components for the mvn-jmxutils package.


%prep
%setup -q -n jmxutils-1.19

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jmxutils
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-jmxutils/LICENSE
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/weakref/jmxutils/1.19
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/weakref/jmxutils/1.19/jmxutils-1.19.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/weakref/jmxutils/1.19
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/weakref/jmxutils/1.19/jmxutils-1.19.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/weakref/jmxutils/1.19/jmxutils-1.19.jar
/usr/share/java/.m2/repository/org/weakref/jmxutils/1.19/jmxutils-1.19.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jmxutils/LICENSE
