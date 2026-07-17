bind = "0.0.0.0:8000"

workers = 4

threads = 2

worker_class = "gthread"

timeout = 120

graceful_timeout = 30

keepalive = 5

max_requests = 1000

max_requests_jitter = 50

accesslog = "-"

errorlog = "-"

loglevel = "info"

capture_output = True

preload_app = True