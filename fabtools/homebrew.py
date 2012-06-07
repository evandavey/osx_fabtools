from fabric.api import *
from fabric.colors import *

def isHomebrewInstalled():
    
    with settings(hide('running', 'stdout', 'warnings')):
        return int(run('brew 2>&1 1>/dev/null | wc -l')) == 0

def upgrade_outdated():
    """
    https://gist.github.com/1025455
    """
    run("brew upgrade `brew outdated | awk {'print $1'} | xargs`")

def update():
    
    run('brew update')

def install_homebrew():
    
    run('/usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"')
    
def install_packages(pkgs, upgrade=False):
   
    for p in pkgs:
        install(pkg,upgrade)

def isPackageInstalled(pkg):
    
    pkgs=installed_pkgs()

    if pkg in pkgs:
        return True
    else:
        return False

def install(pkg,upgrade=False):
    
    if upgrade:
        run('brew install %s --upgrade' % (pkg))
    else:
        run('brew install %s' % (pkg))
    

def installed_pkgs():
    with settings(hide('running', 'stdout', 'warnings'), warn_only=True):
        installed=run('brew list').strip()
        return installed.split()
 
 
def status():
    
    
    if not isHomebrewInstalled():
        return red('not installed')
    else:
        pkgs=', '.join(installed_pkgs())
        return green('installed') + '\n%s\n' % pkgs