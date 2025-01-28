 1  cd pylib_geomanager/
    2  pipx install .
    3  pip install .
    4  ls
    5  cd pylib_geomanager/
    6  pip install .
    7  pip install ecmwflibs
    8  cd ..
    9  ls
   10  python3 sandbox/manage.py runserver 0.0.0.0:8000
   11  pip install -r sandbox/requirements.txt 
   12  nix-env -iA nixpkgs.python3Packages.setuptools
   13  python
   14  nix-env --query --installed | grep setuptools
   15  nix-env --uninstall python3.9-setuptools-57.2.0
   16  nix-env --query --installed | grep setuptools
   17  nix-env -iA nixpkgs.python312Packages.setuptools
   18  nix-shell -p python312 python312Packages.setuptools
   19  nix-env -qa 'python3.*'
   20  python
   21  python3 -c "import setuptools; print(setuptools.__version__)"
   22  history
   23  pip install -r sandbox/requirements.txt 
   24  python3 sandbox/manage.py runserver 0.0.0.0:8000
   25  ls
   26  cd pylib_geomanager/
   27  pip install .
   28  pip install ecmwflibs==0.6.2
   29  pip install ecmwflibs==0.5.3
   30  python3 sandbox/manage.py runserver 0.0.0.0:8000
   31  cd ..
   32  python3 sandbox/manage.py runserver 0.0.0.0:8000
   33  pip install django-deep-translator
   34  python3 sandbox/manage.py runserver 0.0.0.0:8000
   35  pip install wagtail django-modelcluster django_extensions
   36  python3 -c "import wagtail; print(wagtail.__version__)"
   37  pip uninstall wagtail
   38  pip install wagtail==5.2.7
   39  pip uninstall wagtail
   40  pip install wagtail==5.2.1
   41  python3 sandbox/manage.py runserver 0.0.0.0:8000
   42  pip install --upgrade wagtail-metadata wagtail-lazyimages
   43  python
   44  python3 -c "import wagtail; print(wagtail.__version__)"
   45  pip uninstall -r sandbox/requirements.txt -y
   46  pip uninstall wagtail
   47  pip uninstall wagtail-metadata wagtail-lazyimages
   48  history
   49  python3 sandbox/manage.py runserver 0.0.0.0:8000
   50  pip install -r sandbox/requirements.txt 
   51  pip uninstall -r sandbox/requirements.txt -y
   52  pip install -r sandbox/requirements.txt 
   53  python3 sandbox/manage.py runserver 0.0.0.0:8000
   54  python -c "import wagtail; print(wagtail.__version__)"
   55  history
