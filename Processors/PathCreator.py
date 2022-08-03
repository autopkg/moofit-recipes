#!/usr/local/autopkg/python
#
# Copyright 2017 Stephen Bygrave - Moof IT
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""See docstring for PathCreator class"""

from __future__ import absolute_import

import os.path

from autopkglib import Processor, ProcessorError

__all__ = ["PathCreator"]


# Download URLs in chunks of 256 kB.
CHUNK_SIZE = 256 * 1024


class PathCreator(Processor):
    """Creates a directory structure."""
    description = __doc__
    input_variables = {
        "path_to_create": {
            "required": True,
            "description": "Path to create.",
        },
    }
    output_variables = {
    }

    def main(self):
        # Create path_to_create. autopkghelper sets it to root:admin 01775.
        try:
            if not os.path.exists(self.env['path_to_create']):
                os.makedirs(self.env['path_to_create'])
                self.output("Created %s" % self.env['path_to_create'])
        except OSError as err:
            raise ProcessorError("Can't create %s: %s" % (self.env['path_to_create'],
                                                          err.strerror))

if __name__ == '__main__':
    PROCESSOR = PathCreator()
    PROCESSOR.execute_shell()
