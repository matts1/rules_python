# Copyright 2023 The Bazel Authors. All rights reserved.
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

import os
import pathlib
import sys
import unittest


# Since sys.path[0] is the workspace directory, and not the build output directory, this is able to import undeclared_dep.
ORIG = sys.path

# This fails to import declared_dep
STRIPPED = sys.path[1:]

runfiles = os.environ["RUNFILES_DIR"]
# We already use the runfiles directory as part of our path, to allow absolute imports.
# This imports the declared_dep in the runfiles/_main/demo/declared_dep.py, as intended.
RUNFILES = [runfiles + "/_main/demo"] + sys.path[1:]

sys.path = ORIG

print(sys.path)

class ExampleTest(unittest.TestCase):
    def test_can_import_declared_dep(self):
        import declared_dep

    def test_cant_import_undeclared_dep(self):
        with self.assertRaises(ImportError):
            import undeclared_dep

if __name__ == "__main__":
    unittest.main()
