"""
Idempotent API for managing users
"""
from fabtools.files import is_file
import sys


#import osx specific user functionss
if sys.platform == 'darwin':
    from fabtools.user_osx import *
else:
    from fabtools.user import *
    

import fabtools.require


def user(name, home=None):
    """
    Require a user
    """
    if not exists(name):
        warn('%(name)s does not exist, creating' % locals())
        create(name, home=home)
    if home:
        fabtools.require.directory(home, owner=name, use_sudo=True)


def sudoer(username, hosts="ALL", operators="ALL", passwd=False, commands="ALL"):
    """
    Require sudo permissions for a given user
    """
    tags = "PASSWD:" if passwd else "NOPASSWD:"
    spec = "%(username)s %(hosts)s=(%(operators)s) %(tags)s %(commands)s" % locals()
    filename = '/etc/sudoers.d/fabtools-%s' % username
    if is_file(filename):
        sudo('chmod 0640 %(filename)s && rm -f %(filename)s' % locals())
    sudo('echo "%(spec)s" >%(filename)s && chmod 0440 %(filename)s' % locals(), shell=True)
