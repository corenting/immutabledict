"""sphinx configuration."""
from immutabledict import __version__

# Project info
project = "immutabledict"
copyright = "2023, corenting"
author = "corenting"
version = __version__
release = __version__

# General configuration
extensions = [
    "alabaster",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autodoc",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# Autodoc settings
autodoc_default_options = {
    "members": True,
}

# intersphinx to Python
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# HTML output
html_theme = "alabaster"
html_sidebars = {
    "**": [
        "about.html",
        "navigation.html",
        "relations.html",
        "searchbox.html",
        "donate.html",
    ]
}
html_theme_options = {
    "description": "An immutable wrapper around dictionaries",
    "github_user": "corenting",
    "github_repo": "immutabledict",
    "github_type": "star",
    "codecov_button": True,
    "badge_branch": "master",
    "sidebar_width": "300px",
    "donate_url": "https://corenting.fr/donate",
    "extra_nav_links": {
        "Github repository": "https://github.com/corenting/immutabledict",
        "PyPI page": "https://pypi.org/project/immutabledict/",
    },
}
