ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-slim-buster

ARG POETRY_VERSION
ENV POETRY_VERSION=${POETRY_VERSION}

ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/root/.local/bin:/build/.venv/bin:${PATH}

ENV LANGUAGE=en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LC_ALL=en_US.UTF-8
ENV LC_CTYPE=en_US.UTF-8
ENV LC_MESSAGES=en_US.UTF-8

WORKDIR /build

COPY pyproject.toml /build/pyproject.toml
COPY poetry.toml /build/poetry.toml
COPY poetry.lock /build/poetry.lock

COPY pyproject.toml /workspace/pyproject.toml

RUN apt-get update && \
    apt-get install -y wget curl git && \
    # install github cli - https://github.com/cli/cli/blob/trunk/docs/install_linux.md
    mkdir -p -m 755 /etc/apt/keyrings && \
    wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null && \
    chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg && \
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | tee /etc/apt/sources.list.d/github-cli.list > /dev/null && \
    apt update && \
    apt install -y gh && \
    # install pipx
    python -m pip install pipx && \
    python -m pipx ensurepath && \
    # install poetry
    python -m pipx install poetry==${POETRY_VERSION} && \
    # install dependencies
    poetry install --all-extras --with lint --with dev --with publish --no-root && \
    # set git config
    git config --global user.email "ptah@github.com" && \
    git config --global user.name "ptah-lgtm" && \
    # clean index
    apt-get clean && \
    rm -rf \
    /var/lib/apt/lists/* \
    /tmp/* \
    /var/tmp/* \
    /usr/share/man \
    /usr/share/doc \
    /usr/share/doc-base

WORKDIR /workspace

CMD [ "/bin/bash", "-c" ]
