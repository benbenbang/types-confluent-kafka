#! /bin/env bash

function build_images() {
    local PYTHON_VERSIONS=(3.9 3.10 3.11 3.12 3.13)
    local UV_VERSION=0.7.19
    local REPOSITORY=benbenbang/types-confluent-kafka

    set -ex
    set -o pipefail

    echo "start building ci environment for ${REPOSITORY}"

    for PYTHON_VERSION in "${PYTHON_VERSIONS[@]}"; do

        local PYTHON_VERSION_INT=$(echo "$PYTHON_VERSION" | sed 's/\.//')
        if (( PYTHON_VERSION_INT >= 312 )); then
            local DOCKER_PYTHON_VERSION="${PYTHON_VERSION}-slim-bookworm"
        else
            local DOCKER_PYTHON_VERSION="${PYTHON_VERSION}-slim-buster"
        fi

        echo -e "ℹ️ building pre-commit image ghcr.io/${REPOSITORY}/pre-commit:py${PYTHON_VERSION}"

        docker buildx build --platform linux/amd64,linux/arm64 \
                            --build-arg PYTHON_VERSION=$DOCKER_PYTHON_VERSION \
                            --build-arg UV_VERSION=$UV_VERSION \
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
