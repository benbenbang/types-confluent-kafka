#! /bin/env bash

function build_images() {
    local PYTHON_VERSIONS=(3.9 3.10 3.11)
    local POETRY_VERSION=1.5.1
    local REPOSITORY=benbenbang/types-confluent-kafka

    set -ex
    set -o pipefail

    echo "start building ci environment for ${REPOSITORY}"

    for PYTHON_VERSION in "${PYTHON_VERSIONS[@]}"; do
        echo -e "ℹ️ building pre-commit image ghcr.io/${REPOSITORY}/pre-commit:py${PYTHON_VERSION}"

        docker buildx build --platform linux/amd64,linux/arm64 \
                            --build-arg PYTHON_VERSION=$PYTHON_VERSION \
                            --build-arg POETRY_VERSION=$POETRY_VERSION \
                            --push \
                            --no-cache \
                            --rm \
                            -t ghcr.io/${REPOSITORY}/pre-commit:py${PYTHON_VERSION} \
                            -f .github/docker/Dockerfile \
                            .

        echo -e "✅ done - py${PYTHON_VERSION}"
    done

    echo -e "🎉 all done!"
}

build_images
