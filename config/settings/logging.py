from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(
    exist_ok=True,
)


LOGGING = {

    "version": 1,

    "disable_existing_loggers": False,

    "formatters": {

        "standard": {

            "()": "apps.core_logging.formatters.RequestFormatter",

            "format": (
                "[{asctime}] "
                "{levelname} "
                "{user} "
                "{ip} "
                "{method} "
                "{path} "
                "{message}"
            ),

            "style": "{",

        },

    },

    "handlers": {

        "console": {

            "class": "logging.StreamHandler",

            "formatter": "standard",

        },

        "application": {

            "class": "logging.FileHandler",

            "filename": LOG_DIR / "application.log",

            "formatter": "standard",

        },

        "error": {

            "class": "logging.FileHandler",

            "filename": LOG_DIR / "error.log",

            "formatter": "standard",

            "level": "ERROR",

        },

    },

    "loggers": {

        "application": {

            "handlers": [

                "console",

                "application",

            ],

            "level": "INFO",

            "propagate": False,

        },

        "django": {

            "handlers": [

                "console",

                "error",

            ],

            "level": "ERROR",

            "propagate": True,

        },

    },

}