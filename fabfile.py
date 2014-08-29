import os
from fabric.api import run, env, local, hide, get
from fabric.colors import blue, magenta, yellow
from fabric.context_managers import cd


def server():
    env.hosts = ['muminoff.com']
    env.user = 'sardor'
    env.python_path = '/home/sardor/python-env/bin/'
    env.project_path ='/home/sardor/watch_my_wallet/'

def _title(s):
    print(blue(s, bold=True))

def _notice(s):
    print(yellow(s))

def deploy():
    server()
    _title(' --- DEPLOYING PROJECT --- ')
    push()
    pull()
    restart()
    _title(' --- DEPLOY FINISHED --- ')

def push():
    _notice(' [*] Pushing changes to Github')
    local('git push origin develop')

def pull():
    _notice(' [*] Pulling changes from Github')
    with cd(env.project_path):
        run_no_output('git pull origin develop')


def restart():
    _notice(' [*] Restarting app')
    run_no_output(env.python_path + 'supervisorctl -c ' + env.project_path + 'ohmywallet/settings/super.conf restart ohmywallet')

def run_no_output(s):
    with hide('running', 'stdout'):
        run(s)
