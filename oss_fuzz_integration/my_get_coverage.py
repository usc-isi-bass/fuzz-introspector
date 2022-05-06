# Copyright 2021 Fuzz Introspector Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import sys
import signal
import argparse
import subprocess
import sys
import json
import threading
import shutil



def build_proj_with_coverage(project_name):
    try:
        subprocess.check_call("python3 infra/helper.py build_fuzzers --sanitizer=coverage %s"%(project_name), shell=True)
    except:
        print("Building with coverage failed")
        exit(5)

def get_single_cov(project, target, corpus_dir):
    print("BUilding single project")
    build_proj_with_coverage(project)

    try:
        subprocess.check_call("python3 infra/helper.py coverage --no-corpus-download --fuzz-target %s --corpus-dir %s %s"%(target, corpus_dir, project_name), shell=True)#, timeout=60)
    except:
        print("Could not run coverage reports")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("usage: python3 ./get_full_coverage.py PROJECT_NAME TARGET CORPUS_DIR")
        exit(5)

    project_name = sys.argv[1]
    target = sys.argv[2]
    corpus_dir = sys.argv[3]
    get_single_cov(project_name, target, corpus_dir)
