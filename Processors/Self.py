#!/usr/bin/python
#
# Copyright 2015 Nick McSpadden
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

from autopkglib import Processor, ProcessorError

import subprocess
import os.path

__all__ = ["Yo"]

class Yo(Processor):
    description = "Provides a Yo notification if anything was imported."
    input_variables = {
    }
    output_variables = {
    }

    __doc__ = description

    def main(self):
        self.output(self.env)



if __name__ == "__main__":
    processor = Yo()
    processor.execute_shell()
