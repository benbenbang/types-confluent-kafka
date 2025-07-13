# Release Process Guide for Contributors

Releasing a new version is a multi-step process.

This guide aims to provide clear instructions for contributors with **write permissions** to ensure a consistent and smooth release process.



## Steps

1. **Triggering the `pre-release` Action**:
   - Navigate to the 'Actions' tab in the repository.
   - Select the `pre-release` workflow.
   - Change the input from `false` to `true`.
   - Use the `workflow_dispatch` trigger (or equivalent) to initiate the release process.
2. **Action Generates a Merge Request (MR)**:
   - The action will run the necessary scripts and tests, determine the next version based on commit messages, and update the relevant files (e.g., `pyproject.toml`).
   - After completion, the action will create a new MR with the version bump and other relevant changes.
3. **Review the MR**:
   - Contributors should carefully review the MR to ensure that the version bump is correct and that there are no unintended changes.
4. **Approving the MR**:
   - Once the review is complete and no issues are identified, the MR should be approved.
   - Remember, this approval signifies that the changes are ready for users. Make sure all functionalities have been tested and documented.
5. **Merging the MR Initiates the Release**:
   - Merging the approved MR will trigger the subsequent steps of the release process.
   - The action will tag the release, generate release notes, and publish the new version to the appropriate platform (e.g., PyPI).
6. **Post-Release Checks**:
   - After the release, verify that the new version is available on the intended platform(s) and that there are no immediate issues.
   - Inform the wider team or community about the new release, highlighting key features or changes.



## Key Considerations

- **Manual Changes**: Do not manually modify versions in configuration files (like `pyproject.toml`). The automation handles versioning. Manual changes can disrupt the process. This also implies that when you do the code review, please ensure the Pull Request shouldn't have the version manually changed.
- **Communication**: If you encounter issues or uncertainties during the release process, communicate with the team. It's essential to address any concerns before the release goes live.
- **Responsibility**: As a contributor with write permissions, you play a crucial role in the release process. Ensure you're familiar with the released changes and available for post-release checks and potential troubleshooting.
