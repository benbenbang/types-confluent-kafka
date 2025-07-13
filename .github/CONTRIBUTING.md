# Development Guide

Thank you for considering a contribution to `types-confluent-kafka`. This guide will help you set up your development environment and provide an overview of the contribution process.



## Prerequisites

### Local Development

1. **Fork and Clone**: Start by **forking** this repository and then cloning your fork to your local machine.

   ```bash
   git clone https://github.com/<your-user-name>/types-confluent-kafka.git
   cd types-confluent-kafka
   ```

2. **Install uv** `[Optional]`: If you have installed uv globally, you can skip this step and continue with step 3.

   ```bash
   python -m venv .venv
   pip install uv
   ```

3. **Install Dependencies with uv or poertry**: Install development tools.

   ```bash
   uv sync --group dev --group lint
   poetry install --with dev --with lint
   ```

4. **Clone the Confluent Kafka Python repository** `[Optional]`: This can also help you easily navigate between the source code.

   ```bash
   # After `cd types-confluent-kafka`
   git clone https://github.com/confluentinc/confluent-kafka-python
   ```



### Container Development

If you prefer to develop within a container, ensure you have the necessary containerization tools installed.

We've set up a `devcontainer` configuration. This ensures everyone has a consistent, reproducible development environment, which is especially useful for avoiding the "works on my machine" syndrome.

1. **Prerequisites**:
   - [Visual Studio Code](https://code.visualstudio.com/)
   - [Docker](https://www.docker.com/products/docker-desktop)
   - [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for VS Code.

2. **Getting Started**:

   After cloning the repository, open the project in VS Code.

   ```bash
   git clone https://github.com/<your-username>/types-confluent-kafka.git
   cd types-confluent-kafka
   code .



Once inside VS Code, a notification may pop up suggesting reopening the project in a container. If not, press `cmd(ctrl) + option(alt) + p` or `F1`, then search for and select `Remote-Containers: Reopen in Container`. This will start building the Docker container based on the provided `.devcontainer/devcontainer.json` configuration.

1. **Working in the Container**:

   Once the container is built and the project is opened inside of it, you'll be operating in a consistent development environment. All necessary tools and dependencies will be available as defined in the devcontainer configuration.

2. **Tips**:

   - Use the integrated terminal in VS Code to run any commands; it operates inside the container.
   - The project's source code is mounted into the container, so any changes you make inside VS Code will reflect immediately.
   - If you need to install additional software or tools in the container, you can modify the `Dockerfile` inside the `.devcontainer` directory and then rebuild the container.

3. **Finalizing**:

   Once you're done with your changes, you can commit and push them directly from within the containerized VS Code instance. When submitting a pull request, just make sure to mention that you've used the `devcontainer` setup, although it shouldn't generally impact the nature of your contributions.



## Stub Implementation

- **Understanding Stubs**: Before diving into stub implementation, familiarize yourself with the purpose and structure of type stubs in Python.

- **Confluent Kafka Docs**: Refer to the [Confluent Kafka documentation](https://docs.confluent.io/platform/current/clients/confluent-kafka-python/html/index.html) to understand the functionalities you're creating stubs for.

- **Submit a PR**: Once you've made changes or added new stubs, submit a pull request. Ensure your changes don't break existing functionalities and adhere to the project's coding standards.



## Workflow Enhancement

- **Existing Workflows**: Familiarize yourself with the current project workflows. These might be CI/CD pipelines, linting checks, etc.

- **Propose Changes**: If you believe a workflow can be improved or a new one can be introduced, open an issue describing your proposal. Get feedback before starting the implementation.

- **Test Thoroughly**: Before submitting workflows-related changes, ensure they've been tested extensively to avoid disruptions.



## Feedback and Questions

Open an issue or join our community chat for any questions or feedback.

We appreciate all your contributions and look forward to collaborating with you!
