# Cleanup GitLab Runners
Cleanup GitLab Runners based upon the Inactivity or number of days

```bash
./runners-cleanup.py -h
usage: runners-cleanup.py [-h] [-l] [-d DAYS] [-n]

Utility to clean runners

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            List the runners with their status
  -d DAYS, --days DAYS  cleanup runners based upon number of days ago
  -n, --never           cleanup runners who never contacted
  ```
- Set the `URL` and `TOKEN` environment variables

```bash
export URL="https://gitlab.example.com"
export TOKEN="abcgdtwk2876wah-kHSAJK"
```

- List all the runners

```bash
./runners-cleanup.py -l
```

- Cleanup runners which never contacted, status = "not_connected"

```bash
./runners-cleanup.py --never
```

- Cleanup runners based upon last contacted days, Following example will clean runners where contact was 30 days ago.

```bash
./runners-cleanup.py -d 30
```

**PS**: This will not remove the runners directly, it will ask for the approval.

***Some outputs***
```bash
  ./runners-cleanup.py -l
ID:3533, Status: offline, Last Contact: 2020-11-02T11:24:29.584Z, Description: savsingh-ocp-test
ID:3534, Status: offline, Last Contact: 2020-11-02T11:24:25.771Z, Description: gitlab-stage runner on ocp
ID:3558, Status: offline, Last Contact: 2020-09-10T05:39:51.439Z, Description: qe-runner
ID:3561, Status: offline, Last Contact: 2020-09-15T18:47:42.305Z, Description: qe-runner-131
ID:3562, Status: offline, Last Contact: 2020-09-29T07:31:56.645Z, Description: gitlab-runner-sched.hosts.stage
ID:3565, Status: offline, Last Contact: 2020-09-15T18:17:01.477Z, Description: qe-runner-132
ID:3567, Status: offline, Last Contact: 2020-11-25T19:18:15.984Z, Description: qe-runner
ID:3576, Status: offline, Last Contact: 2020-11-22T23:42:56.931Z, Description: docker machine dind
ID:3578, Status: online, Last Contact: 2020-12-10T13:44:12.165Z, Description: Stage runner for Metadata

 ./runners-cleanup.py -d 60
ID:3558, Status: offline, Last Contact: 2020-09-10T05:39:51.439Z, Description: qe-runner
Press [ENTER] to proceed for removal: 
ID:3561, Status: offline, Last Contact: 2020-09-15T18:47:42.305Z, Description: qe-runner-131
Press [ENTER] to proceed for removal: 
ID:3562, Status: offline, Last Contact: 2020-09-29T07:31:56.645Z, Description: gitlab-runner-sched.hosts.stage
Press [ENTER] to proceed for removal: 
ID:3565, Status: offline, Last Contact: 2020-09-15T18:17:01.477Z, Description: qe-runner-132
Press [ENTER] to proceed for removal:
```

**Any improvements are welcome.**
