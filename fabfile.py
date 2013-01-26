from __future__ import with_statement
from fabric.api import *
import os

#
# Stuff for remote env
#

def load():
    """
    Prints the current load values.
    
    Example usage:
    
        $ fab stage load
        $ fab prod load
        
    """
    def _set_color(load):
        """
        Sets the terminal color for an load average value depending on how 
        high it is.
        
        Accepts a string formatted floating point.

        Returns a formatted string you can print.
        """
        value = float(load)
        template = "\033[1m\x1b[%sm%s\x1b[0m\033[0m"
        if value < 1:
            # Return green
            return template % (32, value)
        elif value < 3:
            # Return yellow
            return template % (33, value)
        else:
            # Return red
            return template % (31, value)
    
    with hide('everything'):
        # Fetch the data
        uptime = run("uptime")
        # Whittle it down to only the load averages
        load = uptime.split(":")[-1]
        # Split up the load averages and apply a color code to each depending
        # on how high it is.
        one, five, fifteen = [_set_color(i.strip()) for i in load.split(',')]
        # Get the name of the host that is currently being tested
        host = env['host']
        # Combine the two things and print out the results
        output = u'%s: %s' % (host, ", ".join([one, five, fifteen]))
        print(output)


def restart_memcached():
    """
    Restarts memcached.
    
    `memcached_user` and `memcached_cmd` must be added to your env settings.

    Example usage:
    
        $ fab stage restart_memcached
        $ fab prod restart_memcached

    Example config:

        env.memcached_user = 'www-data'
        env.memcached_cmd = 'memcached -u www-data -p 11211 -m 32 -d'

    """
    # First fetch the pid for the running memcached process
    pid = run("ps U %s | grep 'memcached' | awk '{print $1}'" % env.memcached_user)
    # If it exists...
    if pid:
        # ... kill it.
        sudo("kill %s" % pid)
    # Restart memcached using the env's startup command
    sudo(env.memcached_cmd, pty=True)


def ps(process='all'):
    """
    Reports a snapshot of the current processes.

    If the process kwarg provided is 'all', every current process is returned.

    Otherwise, the list will be limited to only those processes that match the kwarg.

    Example usage:

        $ fab prod ps:process=all
        $ fab prod ps:process=httpd
        $ fab prod ps:process=postgres

    Documentation::

        "ps":http://unixhelp.ed.ac.uk/CGI/man-cgi?ps

    """
    if process == 'all':
        run("ps aux")
    else:
        run("ps -e -O rss,pcpu | grep %s" % process)

#
# Stuff for local env
#

def rmpyc():
    """
    Erases pyc files from current directory.

    Example usage:

        $ fab rmpyc

    """
    print("Removing .pyc files")
    with hide('everything'):
        local("find . -name '*.pyc' -print0|xargs -0 rm", capture=False)


def tabnanny():
    """
    Checks whether any of your files have improper tabs
    
    Example usage:
    
        $ fab tabnanny
    
    """
    print("Running tabnanny")
    with hide('everything'):
        local("python -m tabnanny ./")


def pep8():
    """
    Flags any violations of the Python style guide.

    Requires that you have the pep8 package installed

    Example usage:

        $ fab pep8

    Documentation:

        http://github.com/jcrocholl/pep8

    """
    print("Checking Python style")
    # Grab everything public folder inside the current directory
    dir_list = [x[0] for x in os.walk('./') if not x[0].startswith('./.')]
    # Loop through them all and run pep8
    results = []
    with hide('everything'):
        for d in dir_list:
            results.append(local("pep8 %s" % d))
    # Filter out the empty results and print the real stuff
    results = [e for e in results if e]
    for e in results:
        print(e)


def test():
    """
    Adds a couple other code checking filters to the standard Django test suite.

    Example usage:
    
        $ fab test
    
    """
    pep8()
    tabnanny()
    local('./projects/manage.py test', capture=False)


def rs(port=8000):
    """
    Fire up the Django test server, after cleaning out any .pyc files.

    Example usage:
    
        $ fab rs
        $ fab rs:port=9000
    
    """
    rmpyc()
    local("./manage.py runserver %s" % port, capture=False)


def sh():
    """
    Fire up the Django shell, after cleaning out any .pyc files.

    Example usage:
    
        $ fab sh
    
    """
    rmpyc()
    local("./manage.py shell", capture=False)


def big_files(min_size='20000k'):
    """
    List all files in this directory over the provided size, 20MB by default.
    
    Example usage:
    
        $ fab big_files
    
    """
    with hide('everything'):
        list_ = local("""find ./ -type f -size +%s -exec ls -lh {} \; | awk '{ print $NF ": " $5 }'""" % min_size)
    if list_:
        print("Files over %s" % min_size)
        print(list_)
    else:
        print("No files over %s" % min_size)