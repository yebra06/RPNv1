# -*- coding: utf-8 -*-
# Python Assembler documentation build configuration file, created by
# sphinx-quickstart on Mon Oct 12 17:43:00 2015.

import sys
import os
import shlex
import sphinx_rtd_theme

sys.path.insert(0, os.path.abspath('.'))

#-------------Gen configuration-------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.viewcode',
    'sphinx.ext.graphviz'
]
templates_path = ['_templates']
source_suffix = '.rst'
source_encoding = 'utf-8-sig'
master_doc = 'index'

#----------Gen Project Config------------
exclude_patterns = [
    '_build',
    'LICENSE.rst',
    'README.rst'
]
project = u'RPNv1'
copyright = u'2015, Alfredo Yebra Jr.'
author = u'Alfredo Yebra Jr.'
version = '1'
release = 'Fall 2015'
today_fmt = '%B %d, %Y'
pygments_style = 'sphinx'

#--------------Options for HTML output-------------
html_theme_options = {
        "relbarbgcolor": "green"
}
html_theme = 'classic'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_title = 'RPNv1'
html_short_title = 'RPNv1'
#html_logo = None
html_static_path = ['_static']
html_last_updated_fmt = '%b %d, %Y'
html_use_smartypants = True
#html_sidebars = {}
html_use_index = True
html_show_sourcelink = True
html_show_sphinx = True
html_show_copyright = True

# -------------Options for LaTeX output-------------
latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '12pt'
}
latex_documents = [
    (
      master_doc,
      'RPNv1.tex',
      u'Python RPN Calculator Documentation',
      u'Alfredo Yebra Jr.',
      'manual'
    ),
]
#latex_logo = None

#-------------Options for Texinfo output-------------
texinfo_documents = [
    (
        master_doc,
        'RPNv1',
        u'Python RPN Calculator Documentation',
        author,
        'Reverse Polish Notation',
        'Postfix Notation',
        'LIFO'
    ),
]
