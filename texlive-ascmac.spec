%global tl_name ascmac
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
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
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides boxes and picture macros with Japanese vertical
writing support. It uses only native picture macros and fonts for
drawing boxes and is thus driver-independent. Formerly part of the
Japanese pLaTeX bundle, it now supports all LaTeX engines.

