#!/usr/bin/python

import re
import platform

arch = platform.machine()

if re.match(r'^i.*86$', arch):
    print 'x86'
elif arch == 'x86_64':
    print 'x64'
elif arch.startswith('arm') or arch == 'aarch64':
    print 'arm'
elif arch == 'ppc':
    print 'ppc'
