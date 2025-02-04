{ pkgs }:
let
  # Create a derivation that builds a directory with the GDAL symlink.
  setupGdal = pkgs.stdenv.mkDerivation {
    name = "setup-gdal-symlink";
    # No source files needed.
    src = null;
    buildCommand = ''
      # Create the output directory (Nix will bind $out to a temporary build dir).
      mkdir -p $out/.local/lib
      # Create the symlink pointing to the actual GDAL shared library from pkgs.gdal.
      ln -sf ${pkgs.gdal}/lib/libgdal.so $out/.local/lib/libgdal.so.30
      # (Optionally, you can add a file to indicate success.)
      echo "setup complete" > $out/done
    '';
  };
in
{
  deps = [
    pkgs.python39
    pkgs.gdal
    pkgs.geos
    pkgs.proj
    setupGdal
  ];

  env = {
    # Build a library search path including the directories provided by Nix
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      "${pkgs.gdal}/lib"
      "${pkgs.geos}/lib"
      "${pkgs.proj}/lib"
      # Add the symlink directory from our derivation.
      "${setupGdal}/.local/lib"
    ];

    # Point GDAL_LIBRARY_PATH to our symlink in the derivation output.
    GDAL_LIBRARY_PATH = "${setupGdal}/.local/lib/libgdal.so.30";
    GEOS_LIBRARY_PATH  = "${pkgs.geos}/lib/libgeos_c.so";

    GDAL_DATA = "${pkgs.gdal}/share/gdal";
    PROJ_LIB  = "${pkgs.proj}/share/proj";
  };
}

