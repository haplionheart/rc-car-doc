# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'RC Car Conceptual Overview'
copyright = '2024, Mthokozisi \'Hap\' Sibanda'
author = 'Mthokozisi \'Hap\' Sibanda'

release = '1.0'
version = '1.0.1'

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

# below table line-wrap fix adapted from: https://github.com/bosilca/ompi/blob/815da65b80d078c3518bd12d447d7a573815a920/docs/conf.py
# also below added a script to make sure that external links open in a new tab, got it from here: https://stackoverflow.com/questions/11716781/open-a-link-in-a-new-window-in-restructuredtext

# The sphinx_rtd_theme does not properly handle wrapping long lines in
# table cells when rendering to HTML due to a CSS issue (see
# https://github.com/readthedocs/sphinx_rtd_theme/issues/1505).  Until
# the issue is fixed upstream in sphinx_rtd_theme, we can simply
# override the CSS here.
rst_prolog = """
.. raw:: html

   <style>
   .wy-table-responsive table td,.wy-table-responsive table th{white-space:normal}
   </style>

   <script type="text/javascript">
    <!-- Adds target=_blank to external links -->

    $(document).ready(function () {
      $('a[href^="http://"], a[href^="https://"]').not('a[class*=internal]').attr('target', '_blank');
    });
  </script>
"""
