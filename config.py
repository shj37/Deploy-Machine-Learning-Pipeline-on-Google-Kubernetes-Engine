from os import environ as env
import multiprocessing

PORT = int(env.get("PORT", 8080))
DEBUG_MODE = int(env.get("DEBUG_MODE", 1))

LOCAL = False

# Gunicorn config
bind = ":" + str(PORT)

if LOCAL:
    workers = 2 # multiprocessing.cpu_count() * 2 + 1
    threads = 2 # 2 * multiprocessing.cpu_count()
else:
    workers = multiprocessing.cpu_count() * 2 + 1
    threads = 2 * multiprocessing.cpu_count()
