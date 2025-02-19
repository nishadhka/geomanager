# **Deploying GeoManager on Replit**  

This document provides a structured guide for **deploying GeoManager on Replit**, covering **setup, PostgreSQL integration, overcoming Nix environment issues, and final deployment** using **Micromamba**.

---

## **1. Deployment Challenges in Replit**
Deploying Django-based applications, especially GeoDjango projects, on Replit presents unique challenges:

1. **Replit requires an autoscale tier for deployment.**  
2. **Running Django management commands** (`createsuperuser`, `migrate`, etc.) must be done in the **Dev Environment** before deployment.  
3. **PostgreSQL database** must be manually created, and credentials must be stored in **Replit Secrets**.  
4. **Shell errors and inconsistent routines** appear, requiring **a stable execution process**.  
5. **Nix environment limitations** affect GDAL and GIS libraries, requiring a **Micromamba-based setup** instead.  

---

## **2. Overcoming the Nix Environment Issues**
### **Problem: Nix Setup Blocks Deployment**
- Replit uses **Nix** as its package manager, which is known for causing **dependency conflicts with GIS libraries** (`GDAL`, `GEOS`, `PROJ`, etc.).
- Installing `GDAL` inside Nix requires multiple dependencies, often leading to errors.

### **Solution: Use Micromamba Instead**
Micromamba is a lightweight version of Conda that **avoids Nix-related issues** by creating a separate, isolated environment. This method:
- Eliminates the need to modify Nix configuration.
- Ensures smooth installation of **Python 3.11** and necessary GIS dependencies.

---

## **3. Setting Up the Micromamba Environment**
To prepare the environment in Replit, follow these steps:

1. **Remove any existing Micromamba environment to avoid conflicts:**
   ```bash
   rm -r .mamba
   ```

2. **Set up the Micromamba environment:**
   ```bash
   export MAMBA_ROOT_PREFIX=.mamba
   eval "$(micromamba shell hook --shell=bash)"
   micromamba create -q -n a1
   micromamba activate a1
   ```

3. **Install Python 3.11 and GIS dependencies:**
   ```bash
   micromamba install python==3.11 -c conda-forge
   micromamba install gdal geos proj cairo -c conda-forge
   pip install -r requirements.txt
   ```

4. **Verify GDAL, GEOS, and GeoPandas installation:**
   ```bash
   python -c "from osgeo import gdal; print(gdal.__version__)"
   python -c "from django.contrib.gis.geos import geos; print('GEOS Library Path:', geos.geos_library_path)"
   python -c "import geopandas as gp; print(gp.__version__)"
   ```

---

## **4. Setting Up the Database and Django Configuration**
### **PostgreSQL Database**
- The PostgreSQL instance needs to be manually created in Replit.
- **Database credentials** should be stored securely in **Replit Secrets**.

### **Running Django Migrations**
Once the Micromamba environment is set up, apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### **Collecting Static Files**
```bash
python manage.py collectstatic --noinput --clear -v 2
```

---

## **5. Running the Development Server**
In **Dev Environment**, use the following command:
```bash
gunicorn --config gunicorn_config.py sandbox.wsgi:application
```
- This allows for **testing Django locally** before full deployment.

---

## **6. Deploying GeoManager on Replit's Autoscale Tier**
To **deploy beyond the Dev Environment**, execute the following:

```bash
export MAMBA_ROOT_PREFIX=.mamba
eval "$(micromamba shell hook --shell=bash)"
micromamba activate a1
gunicorn --config gunicorn_config.py sandbox.wsgi:application
```
This ensures:
- The correct **Micromamba environment** is active.
- The **Django application runs with Gunicorn** for production deployment.

---

## **7. Summary of Deployment Steps**
| **Step** | **Command** |
|----------|------------|
| Remove existing Micromamba setup | `rm -r .mamba` |
| Set up Micromamba environment | `export MAMBA_ROOT_PREFIX=.mamba && eval "$(micromamba shell hook --shell=bash)"` |
| Create and activate a new environment | `micromamba create -q -n a1 && micromamba activate a1` |
| Install Python & GIS dependencies | `micromamba install python==3.11 gdal geos proj cairo -c conda-forge` |
| Install project dependencies | `pip install -r requirements.txt` |
| Verify GIS libraries | `python -c "from osgeo import gdal; print(gdal.__version__)"` |
| Run Django migrations | `python manage.py makemigrations && python manage.py migrate` |
| Create superuser | `python manage.py createsuperuser` |
| Collect static files | `python manage.py collectstatic --noinput --clear -v 2` |
| Run development server | `gunicorn --config gunicorn_config.py sandbox.wsgi:application` |
| Deploy on autoscale tier | `export MAMBA_ROOT_PREFIX=.mamba && eval "$(micromamba shell hook --shell=bash)" && micromamba activate a1 && gunicorn --config gunicorn_config.py sandbox.wsgi:application` |

---

### **Key Takeaways**
1. **Micromamba solves Nix-related issues** and simplifies dependency management.
2. **PostgreSQL credentials must be stored in Replit Secrets** for database access.
3. **Django commands (migrations, createsuperuser) must be run in Dev Environment** before deployment.
4. **Gunicorn is used for production deployment** on Replit's autoscale tier.
5. **Ensure the shell runs properly without errors** before launching the application.

