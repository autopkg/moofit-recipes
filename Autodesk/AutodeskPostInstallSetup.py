#!/usr/local/autopkg/python

# Author:   Stephen Bygrave - Moof IT
# Name:     AutodeskPostInstallSetup.sh
#
# Purpose:  This script is used to add the version variable into the AutoDesk postinstall script
#
# Version:  1.0.0, 2020-08-07
#           SB - Initial Creation

# Use at your own risk. Moof IT will accept no responsibility for loss or damage caused by this script.

# Imports

from __future__ import absolute_import, print_function
import os
from autopkglib import Processor, ProcessorError, get_pref

# Run script

__all__ = ["AutodeskPostInstallSetup"]


class AutodeskPostInstallSetup(Processor):
    description = "Adds supplied keys to an AutoDesk app's postinstall \
                    script that will be included within the generated pkg."
    input_variables = {
        "NAME": {
            "description": "AutoDesk application name.",
            "required": True
        },
        "PRODUCT_KEY": {
            "description": "AutoDesk application product key.",
            "required": True
        },
        "VERSION_YEAR": {
            "description": "AutoDesk application version number (i.e. 2021).",
            "required": True
        },
        "EULA_LOCALE": {
            "description": "AutoDesk application EULA locale.",
            "required": True
        },
        "SERIAL_NUMBER": {
            "description": "AutoDesk application serial number.",
            "required": True
        },
        "LIC_SERVER": {
            "description": "AutoDesk application licensing server. Currently only compatible with one server.",
            "required": False
        }
    }
    output_variables = {
    }

    def main(self):

        # Open the postinstall script, substitute the registration info, write changes.
        name = self.env['NAME']
        prod_key = self.env['PRODUCT_KEY']
        version_year = self.env['VERSION_YEAR']
        prod_ver = self.env['PRODUCT_VERSION']
        eula_locale = self.env['EULA_LOCALE']
        serial_number = self.env['SERIAL_NUMBER']
        lic_servers = self.env['LIC_SERVER']
        postinstall_path = self.env['file_path']
        path = os.path.join(os.path.dirname(__file__),
                            postinstall_path)
        print(path)
        if name:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%NAME%' in filetext:
                filetext = filetext.replace('%NAME%', "%s" % (name))
                with open(path, 'w') as file:
                    file.write(filetext)

        if prod_key:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%PK%' in filetext:
                filetext = filetext.replace('%PK%', "%s" % (prod_key))
                with open(path, 'w') as file:
                    file.write(filetext)

        if version_year:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%VER%' in filetext:
                filetext = filetext.replace('%VER%', "%s" % (version_year))
                with open(path, 'w') as file:
                    file.write(filetext)

        if prod_ver is not None:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%PV%' in filetext:
                filetext = filetext.replace('%PV%', "%s" % (prod_ver))
                with open(path, 'w') as file:
                    file.write(filetext)

        if eula_locale:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%EL%' in filetext:
                filetext = filetext.replace('%EL%', "%s" % (eula_locale))
                with open(path, 'w') as file:
                    file.write(filetext)

        if serial_number:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%SN%' in filetext:
                filetext = filetext.replace('%SN%', "%s" % (serial_number))
                with open(path, 'w') as file:
                    file.write(filetext)

        if lic_servers:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%LM%' in filetext:
                filetext = filetext.replace('%LM%', "NETWORK")
                with open(path, 'w') as file:
                    file.write(filetext)
            if '%LS%' in filetext:
                filetext = filetext.replace('%LS%', "%s" % (lic_servers))
                with open(path, 'w') as file:
                    file.write(filetext)
        else:
            filetext = None
            with open(path, 'r') as file:
                filetext = file.read()
            if '%LM%' in filetext:
                filetext = filetext.replace('%LM%', "STANDALONE")
                with open(path, 'w') as file:
                    file.write(filetext)
            if '%LS%' in filetext:
                filetext = filetext.replace('--lic_servers \'@\'%LS%', "")
                with open(path, 'w') as file:
                    file.write(filetext)

if __name__ == "__main__":
    processor = AutodeskPostInstallSetup()
    processor.execute_shell()
