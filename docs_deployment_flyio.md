----
# Deploying GeoManager on Fly.io
----

This document provides a step-by-step guide to deploying GeoManager on Fly.io, including handling PostgreSQL, secrets management, troubleshooting, and SSH access.

## 1. **Environment Setup**
Before using Fly.io CLI, ensure it's properly installed and accessible by adding it to your system's `PATH`:
```bash
export FLYCTL_INSTALL="$HOME/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"
```
This allows the `fly` command to be used without specifying the full path.

## 2. **Initialize and Deploy GeoManager**
To launch the application:
```bash
fly launch --dockerfile Dockerfile --config fly.toml
fly deploy
```
- The `fly launch` command initializes the application using the provided `Dockerfile` and `fly.toml` configuration.
- The `fly deploy` command deploys the application.

## 3. **PostgreSQL Setup**
A PostgreSQL database is required for GeoManager. Create it with:
```bash
fly postgres create
```
Attach the database to the app to set necessary secrets:
```bash
fly postgres attach <your-db-name>
```
After attachment, check for secrets:
```bash
fly secrets list
```
This ensures the `DATABASE_URL` and other required credentials are properly set.

### **PostGIS Extension Requirement**
1. PostgreSQL must be configured with at least **1GB RAM and 1 Core** for PostGIS to work correctly.
2. To connect to the database and enable PostGIS:
```bash
fly postgres connect -a <your-db-name>
```
Once connected, execute the following SQL command:
```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```

Then exit the PostgreSQL console:
```sql
\q
```
If postgres app name not know, it can be list by apps:
```bash
fly postgres list
```
## 4. **Managing Fly Machines**
List active machines:
```bash
fly machines list
```
If the machine is stopped, start it:
```bash
fly machine start <machine-name>
```
If no machines are running, SSH access will fail with unclear errors. Always check the machine status before proceeding.

## 5. **Accessing the Application via SSH**
To open an SSH console:
```bash
fly ssh console
```
- If SSH fails, check the app status:
```bash
fly status
```
- If the app is down, restart a machine before retrying SSH.

## 6. **Troubleshooting**
If the deployment or connection encounters issues, use:
```bash
flyctl doctor
```
If necessary, reset the WireGuard connection:
```bash
flyctl wireguard reset
```
These commands help diagnose and fix networking or configuration problems.

----

## **6. Troubleshooting Common Issues**
If the deployment or connection encounters issues:

1. **Check if the PostgreSQL instance is running**:
```bash
fly status -a <postgres-app-name>
```

2. **Check logs for errors**:
```bash
fly logs -a <postgres-app-name>
```

3. **Restart the PostgreSQL instance**:
```bash
fly apps restart <postgres-app-name>
```

4. **Verify allocated resources**:
```bash
fly scale show -a <postgres-app-name>
```

5. **If corruption or persistent issues occur, create a new PostgreSQL instance**:
```bash
fly postgres create <new-name>
```

---

## **7. Handling Suspended PostgreSQL Instances**
If your PostgreSQL instance is suspended:

1. **Check the current status**:
```bash
fly status -a <postgres-app-name>
```

2. **Start the suspended machine**:
```bash
fly machine start -a <postgres-app-name>
```

3. **Restart the entire PostgreSQL app**:
```bash
fly apps restart <postgres-app-name>
```

4. **Monitor the status** after resuming:
```bash
fly status -a <postgres-app-name>
```

5. **List all machines** associated with the app:
```bash
fly machine list -a <postgres-app-name>
```

---

## **8. Deleting and Recreating PostgreSQL Instances**
If a PostgreSQL instance needs to be deleted and recreated:

1. **Destroy the PostgreSQL app**:
```bash
fly apps destroy <postgres-app-name>
```
2. **Force delete if necessary**:
```bash
fly apps destroy <postgres-app-name> --force
```
3. **Create a new PostgreSQL instance** with PostGIS enabled:
```bash
fly postgres create --image postgis/postgis:15-3.3 <new-name>
```

---

## **9. Additional Troubleshooting Commands**
If network or deployment issues persist, use:
```bash
flyctl doctor
```
To reset WireGuard:
```bash
flyctl wireguard reset
```
These commands help diagnose and resolve connectivity or configuration problems.

---

## **Summary of Key Considerations**
1. **Ensure Fly.io CLI is set up correctly** using `export` commands.
2. **Always attach the PostgreSQL database** to get necessary secrets.
3. **Use a PostgreSQL instance with at least 1GB RAM and 1 Core** to support PostGIS.
4. **Check running machines before using SSH**, or it may fail without a clear error message.
5. **Use Fly.io troubleshooting tools** (`flyctl doctor`, `flyctl wireguard reset`) when encountering issues.
6. **Monitor PostgreSQL status and logs** to diagnose issues before restarting or recreating the instance.
7. **Handle suspended PostgreSQL instances properly** by resuming machines before restarting the app.
8. **If a database is corrupted, recreate it instead of troubleshooting endlessly**.

