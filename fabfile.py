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
    restart()

def push():
    _notice(' [*] Pushing changes to Github')
    local('git push origin develop')

def push():
    _notice(' [*] Pushing changes to Github')
    local('git push origin develop')

def restart():
    _notice(' [*] Pulling from Github')
    run_no_output(env.python_path + 'supervisorctl -c ' + env.project_path + 'watchmywallet/settings/super.conf restart watchmywallet')

def run_no_output(s):
    with hide('running', 'stdout'):
        run(s)
