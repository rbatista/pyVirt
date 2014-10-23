#!/usr/bin/env python

import sys
from virtualizer import Virtualizer

class Cli:
    DOMAIN_STATE = {0: 'No state', 1: 'Running', 2: 'Blocked',
            3: 'Paused', 4: 'Being shut down', 5: 'Shut off',
            6: 'Crashed', 7: 'Suspended'}

    commands = { 'list', 'shutdown' }

    def __init__(self):
        self.virt = Virtualizer()

    def parse(self, args):
        program_name = args[0]
        command = args[1]
        if (len(args) > 2):
            arguments = args[2:]
        else:
            arguments = None

        if (command in self.commands):
            self.__call(command, arguments)
        else:
            print self.help()

    def __call(self, command, opts = None):
        try:
            if (opts == None):
                getattr(self, str(command))()
            else:
                getattr(self, str(command))(*opts)
        except:
            print getattr(self, 'help_' + str(command))()

    def list(self):
        domains = self.virt.get_all_domains()
        if (domains == None):
            print "No domain found."
            return

        print 'ID\tDomain name\tState'
        for domain in domains:
            print str(domain.ID()) + '\t' + domain.name() + '\t' + self.DOMAIN_STATE[domain.state()[0]]

    def help_list(self):
        return "list\nShow all domains"

    def shutdown(self, domain_name):
        if (domain_name == 'all'):
            self.virt.shutdown_all()
            print 'Shuting down all domains'
        else:
            found = self.virt.shutdown_by_name(domain_name)
            if (not found):
                print 'Domain ' + str(domain_name) + ' was not found.'
            else:
                print 'Shuting down ' + str(domain_name)

    def help_shutdown(self):
        return 'shutdown [ all | <domain_name> ]\nGracefull shutdown a domain.'

    def __resolve_domain(self, domain_name):
        if (domain_name == 'all'):
            domains = self.virt.get_all_domains()
        else:
            domains = { self.virt.get_domain_by_name(domain_name) }

        if (domains == None):
            print "Domain " + str(domain_name) +  " was not found"
            sys.exit(1)
        return domains

    def set_memory(self, domain_name, memory):
        domains = self.__resolve_domain(domain_name)
        for domain in domains:
            try:
                self.virt.set_domain_memory(domain, memory)
            except RuntimeError as err:
                sys.stderr.write(str(err))
                sys.exit(1)

    def help_set_memory(self):
        print 'set_memory [ all | <domain_name> ] <memory_size>'
        print 'Configure the domain memory. Set the max_memory if necessary.'

    def set_vcpus(self, domain_name, n_vcpus):
        domains = self.__resolve_domain(domain_name)
        for domain in domains:
            try:
                self.virt.set_domain_vcpus(domain, memory)
            except RuntimeError as err:
                sys.stderr.write(str(err))
                sys.exit(1)

    def help_set_vcpus(self):
        print 'set_vcpus [ all | <domain_name> ] <vcpus_number>'
        print 'Configure the domain memory. Set the max_memory if necessary.'

    def help(self):
        return "Usage: pyVirt <command> [<args>]"
