Summary:	Tool to convert guest from a foreign hypervisor to run on KVM
Summary(pl.UTF-8):	Narzędzie do konwersji gości z obcych hipernadzorców na KVM
Name:		virt-v2v
Version:	2.2.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	https://download.libguestfs.org/virt-v2v/2.2-stable/%{name}-%{version}.tar.gz
# Source0-md5:	01e1164e0380311199f3cdbf3aafc6ca
URL:		https://libguestfs.org/
BuildRequires:	bash-completion-devel >= 1:2.0
BuildRequires:	gettext-tools
BuildRequires:	jansson-devel >= 2.7
BuildRequires:	libguestfs-devel >= 1.44
BuildRequires:	libosinfo-devel
BuildRequires:	libvirt-devel >= 0.10.2
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	ocaml >= 1:4.04
BuildRequires:	ocaml-gettext-devel
BuildRequires:	ocaml-libguestfs-devel >= 1.44
BuildRequires:	ocaml-libnbd-devel >= 1.9.3
BuildRequires:	ocaml-libvirt-devel
BuildRequires:	pcre2-8-devel
BuildRequires:	perl-modules
BuildRequires:	pkgconfig
Requires:	nbdkit
Requires:	nbdkit-plugin-curl
Requires:	nbdkit-plugin-python
%ifarch %{x8664}
Suggests:	nbdkit-plugin-vddk
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Virt-v2v is a program that converts a single guest from a foreign
hypervisor to run on KVM. It can read Linux and Windows guests running
on VMware, Xen, Hyper-V and some other hypervisors, and convert them
to KVM managed by libvirt, OpenStack, oVirt, Red Hat Virtualisation
(RHV) or several other targets. It can modify the guest to make it
bootable on KVM and install virtio drivers so it will run quickly.

%description -l pl.UTF-8
Virt-v2v to program konwertujący pojedynczego gościa z obcego
hipernadzorcy, aby działał pod kontrolą KVM. Potrafi czytać gości z
Linuksem i Windows, działających pod kontrolą VMware, Xena, Hyper-V
oraz kilku innych hipernadzorców i konwertować ich na KVM zarządzany
przez libvirt, OpenStack, oVirt, RHV (Red Hat Virtualisation) lub
inne narzędzie. Potrafi modyfikować gościa, aby dawał się uruchomić
pod KVM i instalować sterowniki virtio.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# useless in binary package
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/virt-v2v-hacking.1

%{__rm} $RPM_BUILD_ROOT%{_mandir}/{ja,uk}/man1/virt-v2v-test-harness.1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/virt-v2v
%attr(755,root,root) %{_bindir}/virt-v2v-in-place
%attr(755,root,root) %{_bindir}/virt-v2v-inspector
%{bash_compdir}/virt-v2v
%{_mandir}/man1/virt-v2v.1*
%{_mandir}/man1/virt-v2v-in-place.1*
%{_mandir}/man1/virt-v2v-input-vmware.1*
%{_mandir}/man1/virt-v2v-input-xen.1*
%{_mandir}/man1/virt-v2v-inspector.1*
%{_mandir}/man1/virt-v2v-output-local.1*
%{_mandir}/man1/virt-v2v-output-openstack.1*
%{_mandir}/man1/virt-v2v-output-rhv.1*
%{_mandir}/man1/virt-v2v-release-notes-1.42.1*
%{_mandir}/man1/virt-v2v-release-notes-2.0.1*
%{_mandir}/man1/virt-v2v-release-notes-2.2.1*
%{_mandir}/man1/virt-v2v-support.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-copy-to-local.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-input-vmware.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-input-xen.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-output-local.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-output-openstack.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-output-rhv.1*
%lang(ja) %{_mandir}/ja/man1/virt-v2v-support.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-copy-to-local.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-input-vmware.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-input-xen.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-output-local.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-output-openstack.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-output-rhv.1*
%lang(uk) %{_mandir}/uk/man1/virt-v2v-support.1*
