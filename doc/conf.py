import sphinx_rtd_theme

project = 'nwDaq-R3'
copyright = '2023-2024, Marek Koza'
author = 'Marek Koza'
extensions = [
	'sphinx_rtd_theme',
]
default_role = 'any'
numfig = True
autosectionlabel_prefix_document = True
templates_path = ['templates']
exclude_patterns = ['build', 'static']

html_theme = 'sphinx_rtd_theme'
html_title = 'nwDaq R3 platform'
html_logo = '_static/nwdaq-r3-sample-board.png'
html_theme_options = {
	'globaltoc_collapse': False,
 	'globaltoc_includehidden': True,
	'prev_next_buttons_location': None,
	'sticky_navigation': True,
}
html_show_sourcelink = False
html_static_path = ['_static']
html_use_index = True
html_css_files = [
	'custom.css',
]

rst_prolog = """
.. |clearer| raw:: html

   <div style="clear: both"></div>

.. role:: tag-button
.. role:: material-icons
"""
