#!/usr/bin/env python
import libvirt
import sys

class Virtualizer:

    def __init__(self):
        self.connection = libvirt.open('qemu:///system')
        if self.connection == None:
            print 'Failed to open connection to the hypervisor'
            sys.exit(1)

    def start(self, domain):
        try:
            domain.create()
        except Exception as e:
            print str(e)
            return 1

    def reboot(sef, domain):
        try:
            domain.reboot()
        except Exception as e:
            print str(e)
            return 1

    def shutdown(self, domain):
        try:
            domain.shutdown()
        except Exception as e:
            print str(e)
            return 1

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
            return self.connection.lookupByName(domain_name)
        except Exception as e:
            print str(e)
            return None

    def get_all_domains(self):
        try:
            return self.connection.listAllDomains()
        except Exception as e:
            print str(e)
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

