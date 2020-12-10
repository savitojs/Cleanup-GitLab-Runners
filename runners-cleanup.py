#!/usr/bin/env python3
# https://github.com/savitojs/Cleanup-GitLab-Runners

import gitlab
from datetime import datetime, timedelta
import sys
import os
import argparse

URL = os.getenv("URL")
TOKEN = os.getenv("TOKEN")

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m'  # white

def _delete_runner(runner_id):
    print(G + f'ID:{gl.runners.get(runner_id).id}, Status: {gl.runners.get(runner_id).status}, Last Contact: { gl.runners.get(runner_id).contacted_at}, Description: {gl.runners.get(runner_id).description}' + W)
    input(R + "Press [ENTER] to proceed for removal: " + W)
    gl.runners.delete(runner_id)

def _date_days_ago(days):
    gitlab_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    return datetime.strftime(datetime.today() - timedelta(days=days), gitlab_date_format)

def _list_runners():
    for runner in runners:
        print(C + f'ID:{runner.id}, Status: {runner.status}, Last Contact: { gl.runners.get(runner.id).contacted_at}, Description: {runner.description}' + W)

def _list_runners_with_status(status):
    for runner in runners:
        if runner.status == status:
            yield runner.id

# Initialize the Parser 
parser = argparse.ArgumentParser(description ='Utility to clean runners') 
parser.add_argument("-l", "--list", help="List the runners with their status", action="store_true")
parser.add_argument("-d", "--days", type=int, help="cleanup runners based upon number of days ago")
parser.add_argument("-n", "--never", help="cleanup runners who never contacted", action="store_true")

args = parser.parse_args() 

if 'URL' and 'TOKEN' not in os.environ:
        print(R + '\n' + "Failed because URL and TOKEN are not set in environment variables. Set URL and TOKEN." + W + '\n' + '\n' + C + "Example:" + '\n' + "export URL=\"https://gitlab.example.com\"" + '\n' + "export TOKEN=\"abcgdtwk2876wah-kHSAJK\"" + W)
        sys.exit(127)

# Clean all the runners where last contact was x days ago.
try:
    gl = gitlab.Gitlab(URL,private_token=TOKEN,ssl_verify=False)
    gl.auth()
    runners = gl.runners.all(all=True)
    if args.list:
        _list_runners()
    elif args.days:
        for i in runners:
            if gl.runners.get(i.id).contacted_at < _date_days_ago(args.days):
                _delete_runner(i.id)
    elif args.never:
        for i in _list_runners_with_status("not_connected"):
            _delete_runner(i)
except gitlab.exceptions.GitlabAuthenticationError as e:
    print(e)
