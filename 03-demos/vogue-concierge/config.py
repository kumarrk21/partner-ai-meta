# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# config.py
from yaml_parser import YAMLParser

_parser = None

#---------------------------------------------------#
# Get YAML Parser
#---------------------------------------------------#
def get_parser():
    """Returns a singleton instance of the YAMLParser.

    :return: The YAMLParser instance.
    :rtype: YAMLParser
    """
    global _parser
    if _parser is None:
        _parser = YAMLParser()
    return _parser
