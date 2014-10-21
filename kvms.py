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

if sys.argv[0] == 'shutdown':
    domain_name = sys.argv[1]
    domain = conn.lookupByName(domain_name)
    if (domain == None):
        print 'Domain not found.'
        sys.exit(1)
    domain.shutdown()
