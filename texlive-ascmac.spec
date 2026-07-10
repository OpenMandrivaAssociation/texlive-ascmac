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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The bundle provides boxes and picture macros with Japanese vertical
writing support. It uses only native picture macros and fonts for
drawing boxes and is thus driver-independent. Formerly part of the
Japanese pLaTeX bundle, it now supports all LaTeX engines.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/ascmac
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/source/latex/ascmac
%dir %{_datadir}/texmf-dist/tex/latex/ascmac
%dir %{_datadir}/texmf-dist/fonts/map/dvips/ascmac
%dir %{_datadir}/texmf-dist/fonts/source/public/ascmac
%dir %{_datadir}/texmf-dist/fonts/tfm/public/ascmac
%dir %{_datadir}/texmf-dist/fonts/type1/public/ascmac
%doc %{_datadir}/texmf-dist/doc/latex/ascmac/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/ascmac/README.md
%doc %{_datadir}/texmf-dist/doc/latex/ascmac/ascmac.pdf
%{_datadir}/texmf-dist/fonts/map/dvips/ascmac/ascmac.map
%doc %{_datadir}/texmf-dist/fonts/source/public/ascmac/ascgrp.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/ascmac/ascii.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/ascmac/ascii10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/ascmac/ascii36.mf
%{_datadir}/texmf-dist/fonts/tfm/public/ascmac/ascgrp.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/ascmac/ascii10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/ascmac/ascii36.tfm
%{_datadir}/texmf-dist/fonts/type1/public/ascmac/ascgrp.pfb
%{_datadir}/texmf-dist/fonts/type1/public/ascmac/ascii10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/ascmac/ascii36.pfb
%doc %{_datadir}/texmf-dist/source/latex/ascmac/Makefile
%doc %{_datadir}/texmf-dist/source/latex/ascmac/ascmac.dtx
%doc %{_datadir}/texmf-dist/source/latex/ascmac/ascmac.ins
%{_datadir}/texmf-dist/tex/latex/ascmac/ascmac.sty
%{_datadir}/texmf-dist/tex/latex/ascmac/tascmac.sty
