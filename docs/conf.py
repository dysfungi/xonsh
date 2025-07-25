#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.
import os
import sys
from collections import OrderedDict
from pathlib import Path

# make current docs directory modules importable
from sphinx.application import Sphinx

sys.path.append(str(Path(__file__).parent.resolve()))

import inspect
import importlib
import typing as tp

os.environ["XONSH_DEBUG"] = "1"
os.environ["XONSH_NO_AMALGAMATE"] = "1"

from xonsh import __version__ as XONSH_VERSION
from xonsh.environ import Env, Var, Xettings

if tp.TYPE_CHECKING:
    from xonsh.environ import VarKeyType
import xonsh.main as xmain

xmain.setup()

spec = importlib.util.find_spec("prompt_toolkit")
if spec is not None:
    # hacky runaround to import PTK-specific events
    from xonsh.shells.ptk_shell import events
else:
    from xonsh.events import events

sys.path.insert(0, os.path.dirname(__file__))


# -- General configuration -----------------------------------------------------

# Documentation is being built on readthedocs, this will be true.
on_rtd = os.environ.get("READTHEDOCS", None) == "True"


# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.imgmath",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx.ext.duration",
    "sphinx.ext.autosummary",
    "numpydoc",
    "extensions.cmdhelp",
    "runthis.sphinxext",
    "extensions.jinja_rst_ext",
    "myst_parser",  # *.md - https://myst-parser.readthedocs.io/
    "sphinx_prompt",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix of source filenames.
source_suffix = {
    ".rst": "restructuredtext",
    ".rst.jinja2": "restructuredtext",
}

# The encoding of source files.
# source_encoding = 'utf-8'

# The master toctree document.
master_doc = "contents"

# General information about the project.
project = "xonsh"
copyright = "2015, Anthony Scopatz"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = XONSH_VERSION.rsplit(".", 1)[0]

# The full version, including alpha/beta/rc tags.
release = XONSH_VERSION

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of documents that shouldn't be included in the build.
exclude_patterns = [
    "api/blank.rst",
    "_build",
    "_static",
    "_templates",
]

# List of directories, relative to source directory, that shouldn't be searched
# for source files.
exclude_trees = []

# The reST default role (used for this markup: `text`) to use for all documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"
# pygments_style = 'friendly'
# pygments_style = 'bw'
# pygments_style = 'fruity'
# pygments_style = 'manni'
# pygments_style = 'tango'
# pygments_style = 'pastie'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ["xonsh."]


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
# html_theme = 'default'
# html_theme = 'altered_nature'
# html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
if not on_rtd:

    html_theme = "furo"

    html_theme_options = {
        "source_repository": "https://github.com/xonsh/xonsh/",
        "source_branch": "main",
        "source_directory": "docs/",
    }

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/ascii_conch_part_transparent_tight.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/magic_conch.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_extra_path = ["_static/robots.txt"]

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {"index": "index.html"}

# If false, no module index is generated.
# html_use_modindex = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = "xonshdoc"


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
# latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
# latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ("index", "xonsh.tex", "xonsh documentation", "Anthony Scopatz", "manual")
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# Additional stuff for the LaTeX preamble.
# latex_preamble = ''

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_use_modindex = True

# Autodocumentation Flags
autodoc_member_order = "groupwise"
autoclass_content = "both"
autosummary_generate = True

# Prevent numpy from making silly tables
numpydoc_show_class_members = False

# runthis
runthis_server = "https://runthis.xonsh.org:80"

#
# Auto-generate some docs
#


class VarDoc(tp.NamedTuple):
    var: Var
    info: tp.Dict[str, tp.Any]  # for using in template additional info


class EnvVarGroup(tp.NamedTuple):
    vars: tp.Dict["VarKeyType", VarDoc]  # sorted variables in the section
    children: tp.Dict[Xettings, "EnvVarGroup"]  # child sections


def _gather_groups(cls, env: Env, _seen=None):
    if _seen is None:
        _seen = set()

    env_vars = list(cls.get_settings())
    env_vars.sort(key=lambda x: getattr(x[0], "pattern", x[0]))
    ordered_vars = OrderedDict()  # within that section sort keys
    for key, var in env_vars:
        var = getattr(key, "pattern", key)
        title = "$" + var
        vd = env.get_docs(key)
        info = dict(
            title=title,
            docstr=vd.doc,
            configurable=vd.is_configurable,
            default=vd.doc_default,
            store_as_str=vd.can_store_as_str,
        )
        ordered_vars[key] = VarDoc(var, info)

    vargrp = EnvVarGroup(ordered_vars, {})
    for sub in cls.__subclasses__():
        if sub not in _seen:
            _seen.add(sub)
            vargrp.children[sub] = _gather_groups(sub, env, _seen)
    return vargrp


def make_envvars():
    return _gather_groups(Xettings, env=Env())


jinja_contexts = {
    # file-name envvars.rst
    "envvars": {
        "make_envvars": make_envvars,
    },
}


def make_events():
    names = sorted(vars(events).keys())
    s = ".. list-table::\n" "    :header-rows: 0\n\n"
    table = []
    ncol = 3
    row = "    {0} - :ref:`{1} <{2}>`"
    for i, var in enumerate(names):
        star = "*" if i % ncol == 0 else " "
        table.append(row.format(star, var, var.lower()))
    table.extend(["      -"] * ((ncol - len(names) % ncol) % ncol))
    s += "\n".join(table) + "\n\n"
    s += "Listing\n" "-------\n\n"
    sec = ".. _{low}:\n\n" "``{title}``\n" "{under}\n" "{docstr}\n\n" "-------\n\n"
    for name in names:
        event = getattr(events, name)
        title = name
        docstr = inspect.getdoc(event)
        if docstr.startswith(name):
            # Assume the first line is a signature
            title, docstr = docstr.split("\n", 1)
            docstr = docstr.strip()
        under = "." * (len(title) + 4)
        s += sec.format(low=name.lower(), title=title, under=under, docstr=docstr)
    s = s[:-9]
    fname = os.path.join(os.path.dirname(__file__), "eventsbody")
    with open(fname, "w") as f:
        f.write(s)


make_events()


def setup(app: Sphinx):
    from xonsh.pyghooks import XonshConsoleLexer

    app.add_lexer("xonshcon", XonshConsoleLexer)
    app.add_css_file("custom.css")


if __name__ == "__main__":
    # use this to debug the process from IDEs
    from sphinx.cmd import build

    build.main(["-b", "html", ".", "_build/html"])
