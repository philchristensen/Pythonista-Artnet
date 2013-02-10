"""ConfigParser Framework Extension."""

import os
import sys
if sys.version_info[0] < 3:
    from ConfigParser import RawConfigParser  # pragma: no cover
else:
    from configparser import RawConfigParser  # pragma: no cover

from ..core import backend, config, handler
from ..utils.misc import minimal_logger

LOG = minimal_logger(__name__)


class ConfigParserConfigHandler(config.CementConfigHandler, RawConfigParser):
    """
    This class is an implementation of the :ref:`IConfig <cement.core.config>`
    interface.  It handles configuration file parsing and the like by
    sub-classing from the standard `ConfigParser
    <http://docs.python.org/library/configparser.html>`_
    library.  Please see the ConfigParser documentation for full usage of the
    class.

    Additional arguments and keyword arguments are passed directly to
    RawConfigParser on initialization.
    """
    class Meta:
        """Handler meta-data."""

        interface = config.IConfig
        """The interface that this handler implements."""

        label = 'configparser'
        """The string identifier of this handler."""

    def __init__(self, *args, **kw):
        # ConfigParser is not a new style object, so you can't call super()
        # super(ConfigParserConfigHandler, self).__init__(*args, **kw)
        RawConfigParser.__init__(self, *args, **kw)
        super(ConfigParserConfigHandler, self).__init__(*args, **kw)
        self.app = None

    def merge(self, dict_obj, override=True):
        """
        Merge a dictionary into our config.  If override is True then
        existing config values are overridden by those passed in.

        :param dict_obj: A dictionary of configuration keys/values to merge
            into our existing config (self).

        :param override:  Whether or not to override existing values in the
            config.

        """
        for section in list(dict_obj.keys()):
            if type(dict_obj[section]) == dict:
                if not section in self.get_sections():
                    self.add_section(section)

                for key in list(dict_obj[section].keys()):
                    if override:
                        self.set(section, key, dict_obj[section][key])
                    else:
                        # only set it if the key doesn't exist
                        if not key in self.keys(section):
                            self.set(section, key, dict_obj[section][key])

                # we don't support nested config blocks, so no need to go
                # further down to more nested dicts.

    def parse_file(self, file_path):
        """
        Parse config file settings from file_path, overwriting existing
        config settings.  If the file does not exist, returns False.

        :param file_path: The file system path to the configuration file.
        :returns: boolean

        """
        file_path = os.path.abspath(os.path.expanduser(file_path))
        if os.path.exists(file_path):
            self.read(file_path)
            return True
        else:
            LOG.debug("config file '%s' does not exist, skipping..." %
                      file_path)
            return False

    def keys(self, section):
        """
        Return a list of keys within 'section'.

        :param section: The config section (I.e. [block_section]).
        :returns: List of keys in the `section`.
        :rtype: list

        """
        return self.options(section)

    def has_key(self, section, key):
        """
        Return whether or not a 'section' has the given 'key'.

        :param section: The section of the configuration.
         I.e. [block_section].
        :param key: The key within 'section'.
        :returns: True if the config `section` has `key`.
        :rtype: boolean

        *This function is deprecated as of Cement 2.1.1, and will be removed
        in future versions.  Use `if 'key' in config.keys('section')`
        instead.*
        """
        if self.app._meta.ignore_deprecation_warnings:
            LOG.debug("ConfigParserConfigHandler.has_key() is " +
                      "deprecated as of Cement 2.1.1.  Please use " +
                      "`if key in app.config.keys(section)` " +
                      "instead.")
        else:
            LOG.warn("ConfigParserConfigHandler.has_key() is " +
                     "deprecated as of Cement 2.1.1.  Please use " +
                     "`if key in app.config.keys(section)` " +
                     "instead.  You can disable this warning by setting " +
                     "`ignore_deprecation_warnings = true` under the " +
                     "applications primary config section.")

        if key in self.keys(section):
            return True
        else:
            return False

    def get_sections(self):
        """
        Return a list of configuration sections or [blocks].

        :returns: List of sections.
        :rtype: list

        """
        return self.sections()

    def get_section_dict(self, section):
        """
        Return a dict representation of a section.

        :param section: The section of the configuration.
         I.e. [block_section]
        :returns: Dictionary reprisentation of the config section.
        :rtype: dict

        """
        dict_obj = dict()
        for key in self.keys(section):
            dict_obj[key] = self.get(section, key)
        return dict_obj

    def add_section(self, section):
        """
        Adds a block section to the config.

        :param section: The section to add.

        """
        super(ConfigParserConfigHandler, self).add_section(section)


def load():
    """Called by the framework when the extension is 'loaded'."""

    handler.register(ConfigParserConfigHandler)
