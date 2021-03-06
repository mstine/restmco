%define gitrev b9d4a55

Name:      kermit-restmco 
Summary:   A simple REST server used to communicate with Mcollective 
Version:   1.0
Release:   6%{?dist}
License:   GPLv3
Group:     System Tools 
#Source0:   %{name}-%{version}.tar.gz 
Source0:   thinkfr-restmco-%{gitrev}.tar.gz 
Requires:  rubygem-daemons, rubygem-sinatra, mcollective-common
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: noarch

%description
A simple REST server in ruby and sinatra, used to communicate with Mcollective 

%prep
%setup -n thinkfr-restmco-%{gitrev}

%build

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/usr/local/bin/kermit/restmco/
install -d -m 755 %{buildroot}/etc/init.d
install mc-rpc-restserver.rb %{buildroot}/usr/local/bin/kermit/restmco
install mc-rpc-restserver-control.rb %{buildroot}/usr/local/bin/kermit/restmco
install service/kermit-restmco %{buildroot}/etc/init.d 

%clean
rm -rf %{buildroot}

%pre
mkdir -p /usr/local/bin/kermit/restmco

%files
%defattr(0644,root,root,-)
%attr(0755, root, root) /usr/local/bin/kermit/restmco/mc-rpc-restserver-control.rb
/usr/local/bin/kermit/restmco/mc-rpc-restserver.rb
%attr(0755,root,root) /etc/init.d/kermit-restmco

%changelog
* Fri Nov 11 2011 Louis Coilliot
- identity_filter=host01_OR_host02 
* Mon Oct 24 2011 Louis Coilliot
- fixed problem with multiple options
* Wed Aug 24 2011 Louis Coilliot 
- fixed problem with limit filter
* Sat Aug 20 2011 Louis Coilliot
- credits and improved comments
* Thu Aug 18 2011 Louis Coilliot
- enable multiple filters in one request
* Thu Aug 18 2011 Louis Coilliot
- Initial build

