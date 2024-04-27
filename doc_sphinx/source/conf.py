import os
import sys
sys.path.insert(0, os.path.abspath('.'))

project = 'loggingpython'
copyright = '2024, Mr-Major-K'
author = 'Mr-Major-K'

version = '1.4'
release = '1.4.12'

language = 'en'

html_theme = 'python_docs_theme'

html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
}

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store'
]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}
