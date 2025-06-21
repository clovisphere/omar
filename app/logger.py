import logging
import os

import structlog

# Set the minimum log level
if os.getenv("ENVIRONMENT", "") == "development":
    structlog.configure(
        wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG)
    )
else:
    structlog.configure(wrapper_class=structlog.make_filtering_bound_logger(logging.INFO))

# Add release {hash-number} to logs:-)
structlog.contextvars.bind_contextvars(release=os.getenv("ENVIRONMENT", "development"))

log = structlog.get_logger()
