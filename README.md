# geomanager-web

Geomanager standalone web application

`Note`: This project is under development.

## Installation with Docker

#### 1. Ensure that you have Docker installed

Check that you have the latest [Docker Engine & Docker Compose Plugin](https://docs.docker.com/engine/install/),
installed and running on the machine where you plan to do the installation.

#### 2. Clone the repository

`git clone https://github.com/wmo-raf/geomanager-web.git`

#### 3. Create `.env` file from `.env.sample`

```
cd geomanager-web
cp .env.sample .env
```

#### 4. Edit the `.env` file and set the environment variables.

See the [Environment Variables](#environmental-variables) section for more details.

#### 5. Build the Docker images

`docker compose build`

#### 6. Run the Docker containers

`docker compose up -d`

You can monitor the logs of the containers with the following command:

`docker compose logs -f`

## Post Installation Configuration

#### 1. Create a superuser

`docker compose exec geomanager_web python manage.py createsuperuser`

#### 2. Access the CMS

Open your browser and go to `http://<ip>:<port>/<ADMIN_URL_PATH>` and login with the superuser credentials you created
in the previous step.

Replace  `<ip>`, `<port>` with the correct values and   `<ADMIN_URL_PATH>` with the value of the `ADMIN_URL_PATH`
variable in your `.env` file.

#### 3. Update the Site Settings

From the Wagtail Admin Side Panel, go to `Settings > Sites` and update the site settings.

Update the default site with the correct domain name/ IP address and port.

## Environmental Variables

Environmental variables for docker compose. All Should be placed in a single `.env` file, saved in the same folder
as `docker-compose.yml` file

### GeoManager CMS Variables

| Variable                           | Description                                                                                                                                                                                                                                          | Required | Default                          | More Details                                                                                           |
|:-----------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------|:---------------------------------|:-------------------------------------------------------------------------------------------------------|
| CMS_DB_USER                        | CMS Database user                                                                                                                                                                                                                                    | YES      |                                  |                                                                                                        |
| CMS_DB_NAME                        | CMS Database name                                                                                                                                                                                                                                    | YES      |                                  |                                                                                                        |
| CMS_DB_PASSWORD                    | CMS Database password.                                                                                                                                                                                                                               | YES      |                                  |                                                                                                        |
| CMS_DB_VOLUME                      | Mounted docker volume path for persisting database data                                                                                                                                                                                              | YES      | ./docker/db/db-data              |                                                                                                        |
| CMS_SITE_NAME                      | The human-readable name of your Wagtail installation which welcomes users upon login to the Wagtail admin.                                                                                                                                           | YES      |                                  |                                                                                                        |
| ADMIN_URL_PATH                     | Base Path to admin pages. Do not use `admin` or an easy to guess path. Should be one word and can include an hyphen. DO NOT include any slashes at the start or the end.                                                                             | YES      |                                  |                                                                                                        |
| CMS_DEBUG                          | A boolean that turns on/off debug mode. Never deploy a site into production with DEBUG turned on                                                                                                                                                     | NO       | False                            |                                                                                                        |
| CMS_PORT                           | Port to run cms                                                                                                                                                                                                                                      | YES      | 80                               |                                                                                                        |
| CMS_BASE_URL                       | This is the base URL used by the Wagtail admin site. It is typically used for generating URLs to include in notification emails.                                                                                                                     | NO       |                                  |                                                                                                        |
| CMS_DEFAULT_LANGUAGE_CODE          | The language code for the CMS. Available codes are `en` for English, `fr` from French, `ar` for Arabic, `es` for Spanish, `sw` for Swahili. Default is `en` if not set                                                                               | NO       | en                               |                                                                                                        |
| CSRF_TRUSTED_ORIGINS               | This variable can be set when CMS_PORT is not 80 e.g if CMS_PORT=8000, CSRF_TRUSTED_ORIGINS would be the following: http://{YOUR_IP_ADDRESS}:8000, http://{YOUR_IP_ADDRESS}, http://localhost:8000 and http://127.0.0.1:8000                         | NO       |                                  |                                                                                                        |
| TIME_ZONE                          | A string representing the time zone for this installation. See the [list of time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). Set this to your country timezone                                                             | NO       | UTC                              | [List of tz database time zones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)         |
| SECRET_KEY                         | A secret key for a particular Django installation. This is used to provide cryptographic signing, and should be set to a unique, unpredictable value. Django will refuse to start if SECRET_KEY is not set                                           | YES      |                                  | You can use this online tool [https://djecrety.ir](https://djecrety.ir/) to generate the key and paste |
| ALLOWED_HOSTS                      | A list of strings representing the host/domain names that this Django site can serve. This is a security measure to prevent HTTP Host header attacks, which are possible even under many seemingly-safe web server configurations.                   | YES      |                                  | [Django Allowed Hosts](https://docs.djangoproject.com/en/4.2/ref/settings/#std-setting-ALLOWED_HOSTS)  |                                                                                                                                                                                                                          |          |         |                                                                                                       |
| SMTP_EMAIL_HOST                    | The host to use for sending email                                                                                                                                                                                                                    | NO       |                                  |                                                                                                        |
| SMTP_EMAIL_PORT                    | Port to use for the SMTP server defined in `SMTP_EMAIL_HOST`                                                                                                                                                                                         | NO       | 25                               |                                                                                                        |
| SMTP_EMAIL_USE_TLS                 | Whether to use a TLS (secure) connection when talking to the SMTP server. This is used for explicit TLS connections, generally on port 587                                                                                                           | NO       | True                             |                                                                                                        |
| SMTP_EMAIL_HOST_USER               | Username to use for the SMTP server defined in `SMTP_EMAIL_HOST`. If empty, Django won’t attempt authentication.                                                                                                                                     | NO       |                                  |                                                                                                        |
| SMTP_EMAIL_HOST_PASSWORD           | Password to use for the SMTP server defined in `SMTP_EMAIL_HOST`. This setting is used in conjunction with `SMTP_EMAIL_HOST_USER` when authenticating to the SMTP server. If either of these settings is empty, Django won’t attempt authentication. | NO       |                                  |                                                                                                        |
| CMS_ADMINS                         | A list of all the people who get code error notifications, in format `"Name <name@example.com>, Another Name <another@example.com>"`                                                                                                                 | NO       |                                  |                                                                                                        |
| DEFAULT_FROM_EMAIL                 | Default email address to use for various automated correspondence from the site manager(s)                                                                                                                                                           | NO       |                                  |                                                                                                        |
| RECAPTCHA_PUBLIC_KEY               | Google Recaptcha Public Key. https://www.google.com/recaptcha/about/ will need a Google account for RECAPTCHA_PRIVATE_KEY and RECAPTCHA_PUBLIC_KEY creation                                                                                          | NO       |                                  |                                                                                                        |
| RECAPTCHA_PRIVATE_KEY              | Google Recaptcha Private Key                                                                                                                                                                                                                         | NO       |                                  |                                                                                                        |
| CMS_NUM_OF_WORKERS                 | Gunicorn number of workers. Recommended value should be `(2 x $num_cores) + 1 `. For example, if your server has `4 CPU Cores`, this value should be set to `9`, which is the result of `(2 x 4) + 1 = 9`                                            | YES      |                                  | [Gunicorn Workers details](https://docs.gunicorn.org/en/latest/design.html#how-many-workers)           |
| CMS_STATIC_VOLUME                  | Mounted docker volume path for persisting CMS static files                                                                                                                                                                                           | YES      | ./docker/volumes/cms/static      |                                                                                                        |
| CMS_MEDIA_VOLUME                   | Mounted docker volume path for persisting CMS media files                                                                                                                                                                                            | YES      | ./docker/volumes/cms/media       |                                                                                                        |                                                                                                                                                                              | YES      | ./cms/backup |                                                                                                        |
| GEOMANAGER_AUTO_INGEST_DATA_VOLUME | Mounted docker volume path where data directories for automated raster data ingestion will be created                                                                                                                                                | YES      | ./docker/volumes/geomanager-data |                                                                                                        |

### MapViewer Variables

| Variable                     | Description                                                                                                                                                                          | REQUIRED | DEFAULT                                 |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|-----------------------------------------|
| MAPVIEWER_CMS_API            | CMS API Endpoint for MapViewer. This should be the public path to your CMS root url , followed by `/api`. For example `https://example.com/api`                                      | YES      |                                         |
| MAPVIEWER_NEXT_STATIC_VOLUME | Mounted docker volume path for MapViewer static files                                                                                                                                | YES      | ./docker/volumes/mapviewer/.next/static |
| BITLY_TOKEN                  | [Bitly](https://bitly.com/) access token. The MapViewer uses Bitly for url shortening. See [here](https://dev.bitly.com/docs/getting-started/authentication/) on how to generate one | NO       |                                         |
| ANALYTICS_PROPERTY_ID        |                                                                                                                                                                                      | NO       |                                         |
| GOOGLE_CUSTOM_SEARCH_CX      |                                                                                                                                                                                      | NO       |                                         |
| GOOGLE_SEARCH_API_KEY        |                                                                                                                                                                                      | NO       |                                         |

##                            