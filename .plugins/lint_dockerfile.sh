#!/usr/bin/env bash
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# Script has been modified by
# - @benbenbang

export REMEMBER_LAST_ANSWER="true"

. "$( dirname "${BASH_SOURCE[0]}" )/init_script.sh"

function hadolint_runner(){
    hadolint=$(which hadolint)

    if [[ -z "$hadolint" ]]; then
        docker run \
            -v "$(pwd):/root" \
            -w /root \
            --rm \
            hadolint/hadolint /bin/hadolint --config ./.plugins/hadolint/hadolint.yml "$@"
    else
        $hadolint --config ./.plugins/hadolint/hadolint.yml "$@"
    fi
}

function lint_wrapper() {
    FILES=("$@")

    if [[ "${#FILES[@]}" == "0" ]]; then
        echo
        echo -e "${GREY}Running docker lint for all Dockerfiles${NC}"
        hadolint_runner Dockerfile*
        echo -e "✅ ${GREEN}Dockerlint completed with no errors${NC}"
        echo
    else
        echo
        echo -e "${GREY}Running docker lint for $*${NC}"
        hadolint_runner "$@"
        echo -e "✅ ${GREEN}Dockerlint completed with no errors${NC}"
        echo
    fi
}

function run_docker_lint(){
    lint_wrapper "$@"
}

run_docker_lint "$@"
