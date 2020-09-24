import sys
import json
import os
import subprocess

try:
  with open('job_data.json') as json_data:
    job_data = json.load(json_data)
except IOError:
  sys.exit('Can\'t read job status from job_data.json')

blacklisted_toolchains = []

for job in job_data['jobs'][1:-1]:
  (project, toolchain, runner) = job['name'].split(" ")
  if job['conclusion'] == "failure":
    blacklisted_toolchains.append(toolchain)

project_dir = 'cmake/projects/' + project
os.makedirs(project_dir + "/ci", exist_ok=True)

blacklist_path = project_dir + '/ci/blacklist.json'
with open(blacklist_path, 'w') as file:
  file.write(json.dumps({"blacklist":blacklisted_toolchains}, indent=4, sort_keys=True))
