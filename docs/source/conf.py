# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'RC Car Conceptual Overview'
copyright = '2024, Mthokozisi \'Hap\' Sibanda'
author = 'Mthokozisi \'Hap\' Sibanda'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.video'
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

html_theme_options = {
    # if we have a html_logo below, this shows /only/ the logo with no title text
    "logo_only": False,
    # Collapse navigation (False makes it tree-like)
    "collapse_navigation": False,
    # Hide the documentation version name/number under the logo
    "display_version": True,
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
