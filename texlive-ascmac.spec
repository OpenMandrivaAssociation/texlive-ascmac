Name:		texlive-ascmac
Version:	53411
Release:	2
Summary:	Boxes and picture macros with Japanese vertical writing support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ascmac
License:	bsd3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascmac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascmac.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ascmac.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides boxes and picture macros with Japanese
vertical writing support. It uses only native picture macros
and fonts for drawing boxes and is thus driver-independent.
Formerly part of the Japanese pLaTeX bundle, it now supports
all LaTeX engines.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/ascmac
%{_texmfdistdir}/tex/latex/ascmac
%{_texmfdistdir}/fonts/type1/public/ascmac
%{_texmfdistdir}/fonts/tfm/public/ascmac
%doc %{_texmfdistdir}/fonts/source/public/ascmac
%{_texmfdistdir}/fonts/map/dvips/ascmac
%doc %{_texmfdistdir}/doc/latex/ascmac

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
