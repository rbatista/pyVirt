#!/usr/bin/env python
import libvirt
import sys
from exceptions import MemoryError

class Virtualizer:

    def __init__(self):
        self.connection = libvirt.openReadOnly(None)
        if self.connection == None:
            print 'Failed to open connection to the hypervisor'
            sys.exit(1)

    def shutdown_by_name(self, domain_name):
        domain = get_domain_by_name(domain_name)
        if (domain == None):
            return False
        else:
            domain.shutdown()
            return True

    def shutdown_all(self):
        domains = self.get_all_domains()

        for domain in domains:
            domain.shutdown()

    def get_domain_by_name(self, domain_name):
        try:
            domain = connection.lookupByName(domain_name)
        except:
            return None

    def get_all_domains(self):
        try:
            return connection.listAllDomains()
        except:
            return None

    def set_domain_memory(self, domain, memory):
        max_memory = domain.getMaxMemory()
        if (max_memory < memory):
            try:
                domain.setMaxMemory(memory)
            except:
                raise MemoryError("The max memory can not be changed.")

        try:
            domain.setMemory(memory)
        except:
            raise MemoryError("The domain memory can not be changed.")
