%global tl_name ascmac
%global tl_revision 79461
%global tl_version 2.1

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Boxes and picture macros with Japanese vertical writing support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ascmac
License:	bsd3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascmac.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascmac.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ascmac.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The bundle provides boxes and picture macros with Japanese vertical
writing support. It uses only native picture macros and fonts for
drawing boxes and is thus driver-independent. Formerly part of the
Japanese pLaTeX bundle, it now supports all LaTeX engines.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from ascmac:
Map ascmac.map
TL_DROPIN_EOF
