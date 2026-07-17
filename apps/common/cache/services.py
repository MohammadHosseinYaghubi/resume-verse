from django.core.cache import cache


DEFAULT_TIMEOUT = 60 * 15


def cache_get(key):
    return cache.get(key)


def cache_set(
    key,
    value,
    timeout=DEFAULT_TIMEOUT,
):
    cache.set(
        key,
        value,
        timeout,
    )


def cache_delete(key):
    cache.delete(key)


def cache_delete_many(keys):
    cache.delete_many(keys)