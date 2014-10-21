#!/usr/bin/env python
import libvirt
import sys

state = {0: 'No state', 1: 'Running', 2: 'Blocked', 3: 'Paused', 4: 'Being shut down', 5: 'Shut off', 6: 'Crashed', 7: 'Suspended'}

conn = libvirt.openReadOnly(None)
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

if sys.argv[0] == 'list':
    domains = conn.listAllDomains()
    print 'ID\tDomain name\tState'
    for domain in domains:
        print str(domain.ID()) + '\t' +  domain.name() + '\t' + state[domain.state()[0]]

if sys.argv[0] == 'shutdown':
    domainName = sys.argv[1]
    found = shutdownByName(domainName)
    if (!found):
        print 'Domain not found.'
        sys.exit(1)

def shutdownByName(name):
    domain = conn.lookupByName(domain_name)
    if (domain == None):
        return false
    shutdown(domain)
    return true

def shutdown(domain):
    domain.shutdown()
    
