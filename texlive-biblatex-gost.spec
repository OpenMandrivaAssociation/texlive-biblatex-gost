# revision 32980
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/biblatex-gost
# catalog-date 2014-02-16 17:29:08 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-biblatex-gost
Version:	1.0.0
Release:	3
Summary:	Biblatex support for GOST standard bibliographies
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-gost
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gost.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gost.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides biblatex support for Russian bibliography
style GOST 7.0.5-2008.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/biblatex-gost/biblatex-gost.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/biblatex-gost.def
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-alphabetic.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-authoryear.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-footnote.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-inline.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric-min.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric-min.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric-min.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric.cbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-numeric.dbx
%{_texmfdistdir}/tex/latex/biblatex-gost/gost-standard.bbx
%{_texmfdistdir}/tex/latex/biblatex-gost/russian-gost.lbx
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/README
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost-examples.bib
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost-examples.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost-examples.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost.pdf
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/biblatex-gost.tex
%doc %{_texmfdistdir}/doc/latex/biblatex-gost/ltxdockit.cfg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
