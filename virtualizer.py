#!/usr/bin/env python
import libvirt
import sys

class Virtualizer:

    def __init__(self):
        self.connection = libvirt.openReadOnly(None)
        if self.connection == None:
            print 'Failed to open connection to the hypervisor'
            sys.exit(1)

    def start(self, domain):
        domain.create()

    def reboot(sef, domain):
        domain.reboot()

    def shutdown(self, domain):
        domain.shutdown()

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
        max_memory = domain.maxMemory()
        if (max_memory < memory):
            try:
                domain.setMaxMemory(memory)
            except:
                raise RuntimeError("The max memory can not be changed for " + domain.name())

        try:
            domain.setMemory(memory)
        except:
            raise RuntimeError("The memory can not be changed for " + domain.name())

    def set_domain_vcpus(self, domain, vcpus):
        maxVcpus = domain.maxVcpus
        if (vcpus > domain.maxVcpus):
            raise RuntimeError("The vcpus is greater than max allowed (" + maxVcpus + ")")
        if (domain.vcpus() != vcpus):
            try:
                domain.setVcpus(vcpus)
            except:
                raise RuntimeError("The vcpus could not be changed for " + domain.name())

