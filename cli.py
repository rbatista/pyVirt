#!/usr/bin/env python

import sys
from virtualizer import Virtualizer

class Cli:
    commands = { 'list', 'shutdown', 'help' }

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
            print str(domain.ID()) + '\t' +  domain.name() + '\t' + state[domain.state()[0]]

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
        return 'shutdown [ all | domain_name ]\nGracefull shutdown a domain.'

    def help(self):
        return "Usage: kvms <command> [args]"
