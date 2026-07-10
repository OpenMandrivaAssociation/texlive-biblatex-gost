%global tl_name biblatex-gost
%global tl_revision 66935

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.24
Release:	%{tl_revision}.1
Summary:	BibLaTeX support for GOST standard bibliographies
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-gost
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gost.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gost.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides BibLaTeX support for Russian bibliography style
GOST 7.0.5-2008

%prep
%setup -q -c -a1
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
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-gost
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-gost
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/biblatex-gost-examples.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/biblatex-gost-examples.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/biblatex-gost-examples.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/biblatex-gost.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/biblatex-gost.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/ltxdockit.cfg
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gost/ltxdockit.cls
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/american-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/biblatex-gost.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/biblatex-gost.def
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/brazilian-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/british-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/catalan-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/croatian-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/english-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/french-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/galician-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/german-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-alphabetic-min.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-alphabetic-min.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-alphabetic-min.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-alphabetic.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-alphabetic.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-alphabetic.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-authoryear-min.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-authoryear-min.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-authoryear-min.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-authoryear.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-authoryear.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-authoryear.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-footnote-min.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-footnote-min.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-footnote-min.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-footnote.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-footnote.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-footnote.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-inline-min.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-inline-min.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-inline-min.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-inline.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-inline.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-inline.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-numeric-min.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-numeric-min.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-numeric-min.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-numeric.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-numeric.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-numeric.dbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/gost-standard.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/greek-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/icelandic-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/italian-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/portuguese-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/russian-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/slovene-gost.lbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gost/spanish-gost.lbx
