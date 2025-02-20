----
# Deploying GeoManager on Fly.io
----

This document provides a step-by-step guide to deploying GeoManager on Fly.io, including handling PostgreSQL, secrets management, troubleshooting, and SSH access.

## 1. **Environment Setup**
Before using Fly.io CLI, ensure it's properly installed and accessible by adding it to your system's `PATH`:
```bash
curl -L https://fly.io/install.sh | sh 
export FLYCTL_INSTALL="$HOME/.fly"
export PATH="$FLYCTL_INSTALL/bin:$PATH"
fly auth login
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

As the dockerfile has the steps to deploy django apps 
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
```
But it is missing with the step of 
```bash 
python manage.py createsuperuser 
```
For that to run to get the admin access, the ssh console has to be used 

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

## **10. Ensuring Application Stays Active Post-Deployment**  

### **Observation: Fly.io Machines Suspend if Not Queried**  
- After a successful deployment, **Fly.io automatically suspends the machine if there is no incoming request** to the provided URL.
- This leads to **unexpected SSH failures** because the machine is in a **stopped state**.
- Running `fly status` will show the application as **stopped**, making it difficult to debug.

### **Solution: Query the Application URL Immediately After Deployment**
To **prevent the machine from going into suspension**, you must **make a request to the provided URL** after deployment.  

1. **Deploy the application** as usual:
   ```bash
   fly deploy
   ```

2. **Retrieve the application URL**:
   ```bash
   fly status -a <app-name>
   ```

3. **Make a request to keep the machine active**:
   ```bash
   curl https://<your-app>.fly.dev/
   ```

4. **Verify the status remains active**:
   ```bash
   fly status -a <app-name>
   ```

**Alternative:** If you want to keep the instance from suspending, consider setting a simple periodic request from another system:
```bash
while true; do curl -s https://<your-app>.fly.dev/ > /dev/null; sleep 300; done
```
(This sends a request every 5 minutes, preventing suspension.)


## **11. Destroying the Application**  
If you need to **remove** the GeoManager application, follow these steps:

1. **Check the status of the application** before proceeding:  
   ```bash
   fly status -a <app-name>
   ```

2. **Destroy the application** (this will remove it from Fly.io):  
   ```bash
   fly apps destroy <app-name>
   ```

3. **Force delete if necessary** (this skips confirmation prompts):  
   ```bash
   fly apps destroy <app-name> --force
   ```

After this, the application will no longer be available.

---

## **12. Destroying the PostgreSQL Instance**  
Since Fly.io PostgreSQL instances are managed as **separate applications**, they must be deleted separately.

1. **Check if the PostgreSQL instance is still running:**  
   ```bash
   fly status -a <postgres-app-name>
   ```

2. **List all PostgreSQL instances** to confirm the correct instance name:  
   ```bash
   fly postgres list
   ```

3. **Destroy the PostgreSQL instance** using the correct command (Fly.io does not support `fly postgres destroy`):  
   ```bash
   fly apps destroy <postgres-app-name>
   ```

4. **Force delete if necessary:**  
   ```bash
   fly apps destroy <postgres-app-name> --force
   ```

5. **Verify that the instance has been removed:**  
   ```bash
   fly status -a <postgres-app-name>
   ```

---

## **13. Checking All Resources Before Deletion**  
Before deleting, you may want to check what is running in your Fly.io environment:

1. **List all applications (including PostgreSQL instances):**  
   ```bash
   fly apps list
   ```

2. **List all active machines:**  
   ```bash
   fly machines list
   ```

3. **List all PostgreSQL instances:**  
   ```bash
   fly postgres list
   ```

4. **List all volumes (persistent storage that might need to be deleted separately):**  
   ```bash
   fly volumes list
   ```

5. **Check allocated resources for an app or database:**  
   ```bash
   fly scale show -a <app-or-db-name>
   ```

---

## **14. Handling Suspended PostgreSQL Instances**  
If a PostgreSQL instance is suspended, it may need to be manually restarted before deletion.

1. **Check the status:**  
   ```bash
   fly status -a <postgres-app-name>
   ```

2. **Start the suspended machine (if applicable):**  
   ```bash
   fly machine start -a <postgres-app-name>
   ```

3. **Restart the entire PostgreSQL application if needed:**  
   ```bash
   fly apps restart <postgres-app-name>
   ```

4. **Verify the instance has resumed:**  
   ```bash
   fly status -a <postgres-app-name>
   ```

5. **List all associated machines:**  
   ```bash
   fly machine list -a <postgres-app-name>
   ```

---

## **15. Cleaning Up and Recreating PostgreSQL Instances**  
If the database has corruption issues, it may be better to **delete and recreate** it.

1. **Destroy the existing PostgreSQL app:**  
   ```bash
   fly apps destroy <postgres-app-name>
   ```

2. **Create a new PostgreSQL instance with PostGIS support:**  
   ```bash
   fly postgres create --image postgis/postgis:15-3.3 <new-db-name>
   ```

3. **Re-attach the new PostgreSQL instance to the application:**  
   ```bash
   fly postgres attach <new-db-name>
   ```

---

## **16. Additional Cleanup (Optional)**  
To fully remove Fly.io configurations from your local system:

- **Remove Fly.io-related configuration files:**  
  ```bash
  rm -rf ~/.fly
  ```

- **Unset Fly.io-related environment variables if manually set:**  
  ```bash
  unset FLYCTL_INSTALL
  unset PATH
  ```

---

## **Summary of Destruction and Cleanup Steps**  
| **Action** | **Command** |
|------------|------------|
| Destroy application | `fly apps destroy <app-name>` |
| Force delete application | `fly apps destroy <app-name> --force` |
| Destroy PostgreSQL instance | `fly apps destroy <postgres-app-name>` |
| Force delete PostgreSQL | `fly apps destroy <postgres-app-name> --force` |
| Check all applications | `fly apps list` |
| Check all machines | `fly machines list` |
| Check PostgreSQL instances | `fly postgres list` |
| Check volumes | `fly volumes list` |
| Restart suspended PostgreSQL | `fly machine start -a <postgres-app-name>` |
| Restart the PostgreSQL app | `fly apps restart <postgres-app-name>` |
| Create a new PostgreSQL instance | `fly postgres create --image postgis/postgis:15-3.3 <new-name>` |
| Attach new PostgreSQL to app | `fly postgres attach <new-db-name>` |
| Remove local Fly.io files | `rm -rf ~/.fly` |

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

