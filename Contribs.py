# This file will write a shell script to fill your github history.

# imports
from random import randint
from datetime import datetime, timedelta

def main():
    # get relevant user input
    print('Maximum number of daily commits:')
    maxCommits = input('> ')
    print('Github username:')
    user = input('> ')
    print('Repository:')
    repo = input('> ')
    
    # writing shell commands
    outFile.truncate()
    write('#!/bin/bash')
    # set environment variables
    write('REPO='+repo)
    write('USER='+user)
    # create repo and move into it
    write('git init $REPO')
    write('cd $REPO')
    # add a readme
    write('touch README.md')
    write('git add README.md')
    
    # get earliest date seen in github history
    date = get_init_date()

    # write commits
    while (date.date() != datetime.today().date()):
        # get random number of commits to do on that day
        dailyWork = randint(0, int(maxCommits))
        for num in range(0, dailyWork):
            write(commit_template(date))
        # move to next day
        date += timedelta(days=1)

    # finishing touches
    write('git remote add origin git@github.com:$USER/$REPO.git')
    write('git pull')
    write('git push -u origin master')
    outFile.close()

# function to write string plus newline to file, makes the output a lot cleaner
def write(s):
    outFile.write(s + '\n')

# get oldest date seen on github history
# that is one year ago, then backwards one day at a time until we find a sunday
def get_init_date():
    today = datetime.today()
    date = datetime(today.year - 1, today.month, today.day, 12)
    weekday = datetime.weekday(date)

    while weekday < 6:
        date = date + timedelta(-1)
        weekday = datetime.weekday(date)

    return date

# a template to write these commits
# set date, then do an empty commit
def commit_template(date):
    template = (
        '''GIT_AUTHOR_DATE={0} GIT_COMMITTER_DATE={1} '''
        '''git commit --allow-empty -m "faking it since day 1" > /dev/null'''
    )
    return template.format(date.isoformat(), date.isoformat())

outFile = open('fillit.sh', 'w')
main()
