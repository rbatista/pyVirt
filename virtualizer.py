#!/usr/bin/env python
import libvirt
import sys

class Virtualizer:
    STATE = {0: 'No state', 1: 'Running', 2: 'Blocked',
            3: 'Paused', 4: 'Being shut down', 5: 'Shut off',
            6: 'Crashed', 7: 'Suspended'}

    def __init__(self):
        self.connection = libvirt.openReadOnly(None)
        if self.connection == None:
            print 'Failed to open connection to the hypervisor'
            sys.exit(1)

    def shutdown_by_name(self, name):
        try:
            domain = connection.lookupByName(domain_name)
        except:
            return False
        else:
            domain.shutdown()
            return True

    def shutdown_all(self):
        try:
            domains = connection.listAllDomains()
        except:
            return

        for domain in domains:
            domain.shutdown()

    def get_all_domains(self):
        try:
            return connection.listAllDomains()
        except:
            return None


