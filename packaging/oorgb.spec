Name:           oorgb
Version:        0.1.0
Release:        1%{?dist}
Summary:        Terminal interactive color picker outputting exact hex and rgb tokens.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oorgb
Source0:        oorgb-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oorgb is a sovereign, capability-bounded COLOR PICKER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oorgb
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oorgb-uninstall

%files
/usr/bin/oorgb
/usr/bin/oorgb-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
