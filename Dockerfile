ARG PYTHON_VERSION=3.13

# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python${PYTHON_VERSION}-alpine

# Install the project into /code
WORKDIR /code

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project --no-editable

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optimal layer caching
ADD . /code
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-editable

# Place executables in the environment at the front of the path
ENV PATH="/code/.venv/bin:$PATH"

# Expose the application port
EXPOSE 8000

# Reset the entrypoint, don't invoke uv
ENTRYPOINT []

# Use entrypoint.sh to run the app
CMD ["/bin/sh", "/code/entrypoint.sh"]
