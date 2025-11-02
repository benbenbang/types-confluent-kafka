#! /bin/env bash
# Debian Release Lifecycle
# | Release | Codename | Released | EOL (Approximate) | Status                   |
# |---------|----------|----------|-------------------|------------------------- |
# | 10      | Buster   | 2019     | Aug 2024          | ❌ Archived (your issue) |
# | 11      | Bullseye | 2021     | ~2026             | ✅ Oldstable (LTS)       |
# | 12      | Bookworm | 2023     | ~2028             | ✅ Current stable        |
# | 13      | Trixie   | TBD 2025 | ~2030             | 🔄 Testing               |


function build_images() {
    local PYTHON_VERSIONS=(3.9 3.10 3.11 3.12 3.13 3.14)
    local UV_VERSION=0.9.3
    local REPOSITORY=benbenbang/types-confluent-kafka
    local CURRENT_DEBIAN_VERSION=bookworm

    set -ex
    set -o pipefail

    echo "start building ci environment for ${REPOSITORY}"

    for PYTHON_VERSION in "${PYTHON_VERSIONS[@]}"; do

        local PYTHON_VERSION_INT=$(echo "$PYTHON_VERSION" | sed 's/\.//')
        local DOCKER_PYTHON_VERSION="${PYTHON_VERSION}-${CURRENT_DEBIAN_VERSION}"

        echo -e " ------------------------------------------------------------------------------- "
        echo -e "ℹ️ building pre-commit image ghcr.io/${REPOSITORY}/pre-commit:py${PYTHON_VERSION}"
        echo -e " ------------------------------------------------------------------------------- "

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

        echo -e " ------------------------------------------------------------------------------- "
        echo -e "✅ done - py${PYTHON_VERSION}"
        echo -e " ------------------------------------------------------------------------------- "
    done

    echo -e "🎉 all done!"
}

build_images
