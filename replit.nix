{pkgs}: {
  deps = [
    pkgs.libgeotiff
    pkgs.zlib
    pkgs.netcdf
    pkgs.libjpeg
    pkgs.hdf5
    pkgs.curl
    pkgs.postgis
    pkgs.postgresql
    pkgs.geos
    pkgs.proj
    pkgs.gdal
    pkgs.tk
    pkgs.tcl
    pkgs.qhull
    pkgs.pkg-config
    pkgs.gtk3
    pkgs.gobject-introspection
    pkgs.ghostscript
    pkgs.freetype
    pkgs.ffmpeg-full
    pkgs.cairo
    pkgs.nodejs-18_x
    pkgs.yarn
  ];
}

