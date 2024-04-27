import os
import sys
sys.path.insert(0, os.path.abspath('.'))
sys.setrecursionlimit(1500)

project = 'loggingpython'
copyright = '2024, Mr-Major-K'
author = 'Mr-Major-K'

version = '1.4'
release = '1.4.12'

language = 'en'

html_theme = 'python_docs_theme'

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
