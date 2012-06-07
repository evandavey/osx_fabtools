from fabric.api import *
from fabric.colors import *
import homebrew, launchctl

label='org.git.daemon'

def isGitInstalled():
    with settings(hide('running', 'stdout', 'warnings')):
        return int(run('git 2>&1 1>/dev/null | wc -l')) == 0

def install_git():
    
    if homebrew.isHomebrewInstalled:
        if homebrew.isPackageInstalled:
            warn('git already installed, will try to upgrade')
            homebrew.install('git',upgrade=True)
        homebrew.install('git')
    else:
        abort('Homebrew not installed, can not install git')
        
def install_gitdaemon():
  
    args=[
    '/usr/local/bin/git',
    'daemon',
    '--base-path=/usr/local/gitolite/repositories',
    '--export-all',
    ]

    launchctl.install2(label,args, user='git')
    
def uninstall():
    pass
    
def install():
    
    install_git()
    install_gitdaemon()


def status():

    if not isGitInstalled():
        return red('not installed')
    else:
        return green('git installed')


#install gitolite



#install gitlab



