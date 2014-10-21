#!/usr/bin/env python
import libvirt
import sys

conn = libvirt.openReadOnly(None)
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

if sys.argv[0] == 'list':
    domains = conn.listAllDomains()
    for domain in domains:
        print domain.name()
