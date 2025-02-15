bind = "0.0.0.0:8000"
workers = 3
timeout = 120
wsgi_app = "sandbox.wsgi:application"

# Add logging configuration
loglevel = "debug"
accesslog = "-"
errorlog = "-"