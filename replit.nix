{ pkgs }: {
    deps = [
      pkgs.python39
      pkgs.gdal
      pkgs.geos
      pkgs.proj
      (pkgs.writeShellScriptBin "setup-gdal" ''
        mkdir -p $HOME/.local/lib
        ln -sf ${pkgs.gdal}/lib/libgdal.so $HOME/.local/lib/libgdal.so.30
      '')
    ];

  env = {
    # Build a library search path using Nix-built libraries.
    LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath [
      "${pkgs.gdal}/lib"
      "${pkgs.geos}/lib"
      "${pkgs.proj}/lib"
    ];

    # We will create a symlink at $HOME/.local/lib/libgdal.so.30 in the shellHook.
    # Then we reference it with these environment variables.
    GDAL_LIBRARY_NONDJANGO_PATH = "$HOME/.local/lib/libgdal.so.30";
    GDAL_LIBRARY_PATH = "$HOME/.local/lib/libgdal.so.30";
    GEOS_LIBRARY_PATH = "${pkgs.geos}/lib/libgeos_c.so";

    GDAL_DATA = "${pkgs.gdal}/share/gdal";
    PROJ_LIB = "${pkgs.proj}/share/proj";
  };

  shellHook = ''
    # Create the local library directory if it doesn't exist.
    mkdir -p $HOME/.local/lib

    # Create (or update) the symlink pointing to the actual GDAL shared library from the nix store.
    ln -sf ${pkgs.gdal}/lib/libgdal.so $HOME/.local/lib/libgdal.so.30

    echo "Symlink ensured: $HOME/.local/lib/libgdal.so.30 -> ${pkgs.gdal}/lib/libgdal.so"
  '';
}
