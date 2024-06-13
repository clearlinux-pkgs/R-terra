#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v10
# autospec commit: 5905be9
#
Name     : R-terra
Version  : 1.7.78
Release  : 87
URL      : https://cran.r-project.org/src/contrib/terra_1.7-78.tar.gz
Source0  : https://cran.r-project.org/src/contrib/terra_1.7-78.tar.gz
Summary  : Spatial Data Analysis
Group    : Development/Tools
License  : GPL-3.0
Requires: R-terra-lib = %{version}-%{release}
Requires: R-Rcpp
BuildRequires : R-Rcpp
BuildRequires : buildreq-R
BuildRequires : gdal-dev
BuildRequires : geos-dev
BuildRequires : pkgconfig(sqlite3)
BuildRequires : proj-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-terra package.
Group: Libraries

%description lib
lib components for the R-terra package.


%prep
%setup -q -n terra
pushd ..
cp -a terra buildavx2
popd
pushd ..
cp -a terra buildavx512
popd
pushd ..
cp -a terra buildapx
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1716403420

%install
export SOURCE_DATE_EPOCH=1716403420
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py apx %{buildroot}-va %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/terra/NEWS.md
/usr/lib64/R/library/terra/R/terra
/usr/lib64/R/library/terra/R/terra.rdb
/usr/lib64/R/library/terra/R/terra.rdx
/usr/lib64/R/library/terra/colors/legends.rds
/usr/lib64/R/library/terra/colors/palettes.rds
/usr/lib64/R/library/terra/ex/countries.rds
/usr/lib64/R/library/terra/ex/elev.tif
/usr/lib64/R/library/terra/ex/logo.tif
/usr/lib64/R/library/terra/ex/lux.dbf
/usr/lib64/R/library/terra/ex/lux.prj
/usr/lib64/R/library/terra/ex/lux.shp
/usr/lib64/R/library/terra/ex/lux.shx
/usr/lib64/R/library/terra/ex/meuse.rds
/usr/lib64/R/library/terra/ex/meuse.tif
/usr/lib64/R/library/terra/ex/test.grd
/usr/lib64/R/library/terra/ex/test.gri
/usr/lib64/R/library/terra/help/AnIndex
/usr/lib64/R/library/terra/help/aliases.rds
/usr/lib64/R/library/terra/help/figures/logo.png
/usr/lib64/R/library/terra/help/paths.rds
/usr/lib64/R/library/terra/help/terra.rdb
/usr/lib64/R/library/terra/help/terra.rdx
/usr/lib64/R/library/terra/html/00Index.html
/usr/lib64/R/library/terra/html/R.css
/usr/lib64/R/library/terra/tests/tinytest.R
/usr/lib64/R/library/terra/tinytest/test_aggregate.R
/usr/lib64/R/library/terra/tinytest/test_arith.R
/usr/lib64/R/library/terra/tinytest/test_cats.R
/usr/lib64/R/library/terra/tinytest/test_classify.R
/usr/lib64/R/library/terra/tinytest/test_crds.R
/usr/lib64/R/library/terra/tinytest/test_crop.R
/usr/lib64/R/library/terra/tinytest/test_equal.R
/usr/lib64/R/library/terra/tinytest/test_extent.R
/usr/lib64/R/library/terra/tinytest/test_extract.R
/usr/lib64/R/library/terra/tinytest/test_focal.R
/usr/lib64/R/library/terra/tinytest/test_geom.R
/usr/lib64/R/library/terra/tinytest/test_global.R
/usr/lib64/R/library/terra/tinytest/test_matrix-input.R
/usr/lib64/R/library/terra/tinytest/test_merge.R
/usr/lib64/R/library/terra/tinytest/test_multivariate.R
/usr/lib64/R/library/terra/tinytest/test_patches.R
/usr/lib64/R/library/terra/tinytest/test_raster-vector.R
/usr/lib64/R/library/terra/tinytest/test_replace.R
/usr/lib64/R/library/terra/tinytest/test_vector-subset.R
/usr/lib64/R/library/terra/tinytest/test_weighted-mean.R
/usr/lib64/R/library/terra/tinytest/test_window.R
/usr/lib64/R/library/terra/tinytest/test_wkt_grd.R
/usr/lib64/R/library/terra/tinytest/test_zonal.R
/usr/lib64/R/library/terra/tinytest/tinytest.R

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/R/library/terra/libs/terra.so
/V4/usr/lib64/R/library/terra/libs/terra.so
/VA/usr/lib64/R/library/terra/libs/terra.so
/usr/lib64/R/library/terra/libs/terra.so
