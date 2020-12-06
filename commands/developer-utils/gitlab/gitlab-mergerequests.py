#!/usr/bin/env python3

# How to use this script?
# It's a template which needs further setup. Duplicate the file,
# remove `.template.` from the filename and set an Personal access token as
# well as the GitLab instance url if it is not gitlab.com
#
# API: https://docs.gitlab.com/ee/api


# Parameters

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title GitLab Merge requests List
# @raycast.mode fullOutput

# Conditional parameters:
# @raycast.refreshTime 1h

# Optional parameters:
# @raycast.packageName GitLab
# @raycast.icon images/gitlab.png

# Documentation:
# @raycast.author Michael Aigner
# @raycast.authorURL https://github.com/tonka3000
# @raycast.description Show merge requests from GitLab


# Configuration
# see gitlabconfig.py

# Main program

from gitlabhelper import GitLab
gitlab = GitLab()
data = gitlab.get_call("merge_requests?state=opened&scope=assigned_to_me")
print(f"GitLab Merge requests assigned to you on {gitlab.instance}:\n")
for e in data:
  title = e.get("title")
  reference = e.get("references", {}).get("full")
  print(f"* {title} at {reference}")