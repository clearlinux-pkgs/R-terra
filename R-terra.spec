#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-terra
Version  : 1.1.17
Release  : 4
URL      : https://cran.r-project.org/src/contrib/terra_1.1-17.tar.gz
Source0  : https://cran.r-project.org/src/contrib/terra_1.1-17.tar.gz
Summary  : Spatial Data Analysis
Group    : Development/Tools
License  : GPL-3.0
Requires: R-terra-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-raster
BuildRequires : R-Rcpp
BuildRequires : R-raster
BuildRequires : buildreq-R
BuildRequires : gdal-dev
BuildRequires : geos-dev
BuildRequires : proj-dev
BuildRequires : sqlite-autoconf-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-terra package.
Group: Libraries

%description lib
lib components for the R-terra package.


%prep
%setup -q -c -n terra
cd %{_builddir}/terra

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618451697

%install
export SOURCE_DATE_EPOCH=1618451697
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library terra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library terra
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library terra
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc terra || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/terra/DESCRIPTION
/usr/lib64/R/library/terra/INDEX
/usr/lib64/R/library/terra/Meta/Rd.rds
/usr/lib64/R/library/terra/Meta/features.rds
/usr/lib64/R/library/terra/Meta/hsearch.rds
/usr/lib64/R/library/terra/Meta/links.rds
/usr/lib64/R/library/terra/Meta/nsInfo.rds
/usr/lib64/R/library/terra/Meta/package.rds
/usr/lib64/R/library/terra/NAMESPACE
/usr/lib64/R/library/terra/NEWS
/usr/lib64/R/library/terra/R/terra
/usr/lib64/R/library/terra/R/terra.rdb
/usr/lib64/R/library/terra/R/terra.rdx
/usr/lib64/R/library/terra/ex/countries.rds
/usr/lib64/R/library/terra/ex/elev.tif
/usr/lib64/R/library/terra/ex/logo.tif
/usr/lib64/R/library/terra/ex/lux.dbf
/usr/lib64/R/library/terra/ex/lux.prj
/usr/lib64/R/library/terra/ex/lux.shp
/usr/lib64/R/library/terra/ex/lux.shx
/usr/lib64/R/library/terra/ex/test.tif
/usr/lib64/R/library/terra/help/AnIndex
/usr/lib64/R/library/terra/help/aliases.rds
/usr/lib64/R/library/terra/help/paths.rds
/usr/lib64/R/library/terra/help/terra.rdb
/usr/lib64/R/library/terra/help/terra.rdx
/usr/lib64/R/library/terra/html/00Index.html
/usr/lib64/R/library/terra/html/R.css
/usr/lib64/R/library/terra/tests/tinytest.R
/usr/lib64/R/library/terra/tinytest/test_aggregate.R
/usr/lib64/R/library/terra/tinytest/test_extract.R
/usr/lib64/R/library/terra/tinytest/test_geom.R
/usr/lib64/R/library/terra/tinytest/test_global.R
/usr/lib64/R/library/terra/tinytest/test_matrix-input.R
/usr/lib64/R/library/terra/tinytest/test_raster-vector.R
/usr/lib64/R/library/terra/tinytest/test_vector-subset.R
/usr/lib64/R/library/terra/tinytest/test_window.R
/usr/lib64/R/library/terra/tinytest/tinytest.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/terra/libs/terra.so
/usr/lib64/R/library/terra/libs/terra.so.avx2
/usr/lib64/R/library/terra/libs/terra.so.avx512
