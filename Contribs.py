# This file will write a shell script to fill your github history.

from random import randint
from datetime import datetime, timedelta

def main():
    print('Maximum number of daily commits:\n>')
    maxCommits = input()
    print('Github username:\n>')
    user = input()
    print('Repository:\n>')
    repo = input()
    outFile.truncate()
    write('#!/bin/bash')
    write('REPO='+repo)
    write('USER='+user)
    write('git init $REPO')
    write('cd $REPO')
    write('touch README.md')
    write('git add README.md')
    date = get_init_date()
    while (date.date() != datetime.today().date()):
        dailyWork = randint(0, int(maxCommits))
        for num in range(0, dailyWork):
            write(commit_template(date))
        date += timedelta(days=1)

    write('git remote add origin git@github.com:$USER/$REPO.git')
    write('git pull')
    write('git push -u origin master')
    outFile.close()

def write(s):
    outFile.write(s + '\n')

def get_init_date():
    today = datetime.today()
    date = datetime(today.year - 1, today.month, today.day, 12)
    weekday = datetime.weekday(date)

    while weekday < 6:
        date = date + timedelta(-1)
        weekday = datetime.weekday(date)

    return date

def commit_template(date):
    template = (
        '''GIT_AUTHOR_DATE={0} GIT_COMMITTER_DATE={1} '''
        '''git commit --allow-empty -m "faking it since day 1" > /dev/null\n'''
    )
    return template.format(date.isoformat(), date.isoformat())

outFile = open('fillit.sh', 'w')
main()
