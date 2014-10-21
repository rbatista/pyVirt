#!/usr/bin/env python
import libvirt
import sys

state = {0: 'No state', 1: 'Running', 2: 'Blocked', 3: 'Paused', 4: 'Being shut down', 5: 'Shut off', 6: 'Crashed', 7: 'Suspended'}

conn = libvirt.openReadOnly(None)
if conn == None:
    print 'Failed to open connection to the hypervisor'
    sys.exit(1)

def shutdownByName(name):
    try:
        domain = conn.lookupByName(domain_name)
    except:
        return False
    domain.shutdown()
    return True

def shutdownAll():
    try:
        domains = conn.listAllDomains() 
    except:
        return

    for domain in domains:
        domain.shutdown()

if sys.argv[1] == 'list':
    try:
        domains = conn.listAllDomains()
    except:
        print "No domain found."
        sys.exit(1)

    print 'ID\tDomain name\tState'
    for domain in domains:
        print str(domain.ID()) + '\t' +  domain.name() + '\t' + state[domain.state()[0]]

if sys.argv[1] == 'shutdown':
    domainName = sys.argv[2]

    if (domainName == 'all'):
        shutdownAll()
    else:
        found = shutdownByName(domainName)
        if (not found):
            print 'Domain ' + str(domainName) + ' was not found.'
            sys.exit(1)


