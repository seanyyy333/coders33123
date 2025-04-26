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
4.  **View the local site:**
    Open <http://localhost:4000> in your web browser. Press `Ctrl+C` in the terminal to stop the local server.

---

*Note: Information about Homebrew commands (like `brew --version`), environment variables (`HOMEBREW_*`), shell completion setup, etc., are part of the *content* of the documentation site itself (<https://docs.brew.sh>) and are not prerequisites for building the site locally.*