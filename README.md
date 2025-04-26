# Homebrew Docs

These are the source files for the [Homebrew documentation site](https://docs.brew.sh/).

The documentation is built using [Jekyll](https://jekyllrb.com/) and hosted on [GitHub Pages](https://pages.github.com/).

A [GitHub Action](https://github.com/Homebrew/brew/blob/master/.github/workflows/docs.yml) is run to validate each change before the site is deployed.

## Viewing the Documentation

To view the live, deployed documentation, simply open <https://docs.brew.sh> in your web browser.

## Building Locally

If you are contributing to the documentation, you can build and preview the site locally before submitting changes.

### Prerequisites

1.  **Ruby:** Jekyll is built with Ruby. Ensure you have a compatible Ruby version installed (check the `Gemfile` for specifics if needed, but a recent version usually works).
2.  **Bundler:** Used to manage Ruby gem dependencies. Install it with `gem install bundler`.
3.  **Homebrew Installation:** You need Homebrew installed to easily navigate to the correct directory.
4.  **(macOS) Xcode Command Line Tools:** Some gems may require build tools. Install them using `xcode-select --install`.
5.  **(Linux) Build Tools:** Some gems may require build tools. Install `build-essential` (Debian/Ubuntu) or `base-devel` (Arch) or equivalent for your distribution.

### Steps

1.  **Navigate to the docs directory:**
    ```bash
    # Change directory to the 'docs' subdirectory within your local Homebrew repository
    cd "$(brew --repository)"/docs
    ```

2.  **Install dependencies:**
    ```bash
    # Install the required Ruby gems specified in the Gemfile
    bundle install
    ```

3.  **Build and serve the site:**
    ```bash
    # Start the local Jekyll development server
    # --watch automatically rebuilds the site when files change
    bundle exec jekyll serve --watch
    ```

4.  **View the local site:**
    Open <http://localhost:4000> in your web browser. Press `Ctrl+C` in the terminal to stop the local server.

---

*Note: Information about Homebrew commands (like `brew --version`), environment variables (`HOMEBREW_*`), shell completion setup, etc., are part of the *content* of the documentation site itself (<https://docs.brew.sh>) and are not prerequisites for building the site locally.*

# Xcode Version Handling in Homebrew

This document outlines how Homebrew determines supported Xcode versions and the process for updating Homebrew when new Xcode versions are released. This is primarily relevant for Homebrew maintainers.

## Supported Xcode Versions

Homebrew aims to support and recommends using the latest stable version of Xcode and/or the Command Line Tools (CLT) available for your macOS version.

The authoritative source for the specific versions Homebrew recognizes as "latest" is defined within Homebrew's codebase:

*   **File:** [`Library/Homebrew/os/mac/xcode.rb`](https://github.com/Homebrew/brew/blob/HEAD/Library/Homebrew/os/mac/xcode.rb)

*   **Key Definitions:**
    *   `OS::Mac::Xcode.latest_version`: Defines the version string for the latest recognized *full Xcode* release (e.g., `"15.0"`).
    *   `OS::Mac::CLT.latest_clang_version`: Defines the Clang compiler version string associated with the latest recognized *Command Line Tools* release. Note that this might differ from the Clang version bundled with the full Xcode release, especially if CLTs are updated separately.

Homebrew uses these definitions, along with detection of the installed Xcode/CLT versions, to perform compatibility checks and determine appropriate build environments.

## Updating for New Xcode Releases

When Apple releases a new version of Xcode or the Command Line Tools, Homebrew maintainers need to update the internal definitions to reflect the new "latest" versions.

**File to Update:**

*   [`Library/Homebrew/os/mac/xcode.rb`](https://github.com/Homebrew/brew/blob/HEAD/Library/Homebrew/os/mac/xcode.rb)

**Specific Items to Update:**

1.  **`OS::Mac::Xcode.latest_version`**:
    *   Modify the string constant to reflect the version number of the new *full Xcode* release.
    *   Example: Change `return "14.3"` to `return "15.0"`.

2.  **`OS::Mac::CLT.latest_clang_version`**:
    *   Modify the string constant to reflect the Clang version associated with the new *Command Line Tools* release. This information can typically be found in the Xcode release notes or by inspecting the tools after installation.
    *   Example: Change `return "1403.0.22.14.1"` to the new Clang version string.

3.  **`OS::Mac::Xcode.detect_version_from_clang_version`**:
    *   This method maps detected Clang versions back to corresponding Xcode versions.
    *   If the new Xcode/CLT release includes a *new* Clang version string that isn't already handled by this method's logic (e.g., in its `case` statement or other conditions), the logic needs to be updated to correctly map this new Clang version back to the appropriate Xcode version number.

**Process:**

*   A maintainer typically creates a Pull Request against the `Homebrew/brew` repository containing these changes shortly after a new Xcode/CLT release.
*   These changes are tested via Homebrew's CI system before being merged.