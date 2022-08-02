"""
This script will first prompt you to enter a name for the new context.
Then you will be prompted to choose a file, here you should choose
a burp project file (.json). The script will then create a new zap context
that matches the "scope" defined in the burp suite project.
"""
from javax.swing import JFileChooser
from javax.swing import JOptionPane
from org.parosproxy.paros.model import Model
import json


def get_context_name():
    return JOptionPane.showInputDialog(None, "Enter a Name for the Context")


def get_file_name():
    fc = JFileChooser()
    result = fc.showOpenDialog(None)
    return None if result != JFileChooser.APPROVE_OPTION else fc.getSelectedFile()


def get_url_regexes(file_name, include):
    with open(file_name, "r") as f:
        data = json.load(f)
    includes = get_includes(data) if include else get_excludes(data)
    regexes = []
    for include in includes:
        host = get_host(include)
        protocol = get_protocol(include)
        if host.count(".") == 1:
            proper_regex = add_www_case(protocol, host)
            regexes.append(proper_regex)
        proper_regex = build_proper_regex(protocol, host)
        regexes.append(proper_regex)
    return regexes


def get_includes(data):
    return data['target']['scope']['include']


def get_excludes(data):
    return data['target']['scope']['exclude']


def add_www_case(protocol, host):
    host = f"www.{host}"
    return protocol + host + ".*"


def get_host(include):
    host = str(include['host'])
    host = host[1:-1]
    return host


def get_protocol(include):
    protocol = str(include['protocol'])
    protocol = "http://" if protocol == "http" else "https://"
    return protocol


def build_proper_regex(protocol, host):
    return protocol + host + ".*"


def create_new_context(ctx_name):
    session = Model().getSingleton().getSession()
    return session.getNewContext(ctx_name)


def include_in_context(url_regexes, context):
    for pattern in url_regexes:
        context.addIncludeInContextRegex(pattern)


def exclude_from_context(url_regexes, context):
    for pattern in url_regexes:
        context.addExcludeFromContextRegex(pattern)


ctx_name = get_context_name()
file_name = get_file_name()
ctx = create_new_context(ctx_name)
include_url_regexes = get_url_regexes(str(file_name), True)
exclude_url_regexes = get_url_regexes(str(file_name), False)
include_in_context(include_url_regexes, ctx)
exclude_from_context(exclude_url_regexes, ctx)
