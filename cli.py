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
        if (opts == None):
            getattr(self, str(command))()
        else:
            getattr(self, str(command))(*opts)

    def list(self):
        domains = self.virt.get_all_domains()
        if (domains == None):
            print "No domain found."
            sys.exit(1)

        print 'ID\tDomain name\tState'
        for domain in domains:
            print str(domain.ID()) + '\t' +  domain.name() + '\t' + state[domain.state()[0]]

    def shutdown(self, domain_name):
        if (domain_name == 'all'):
            self.virt.shutdown_all()
            print 'Shuting down ' + str(domain_name)
        else:
            found = self.virt.shutdown_by_name(domain_name)
            if (not found):
                print 'Domain ' + str(domain_name) + ' was not found.'
                sys.exit(1)
            else:
                print 'Shuting down ' + str(domain_name)

    def help(self):
        return "Usage: kvms <command> [args]"


def main():
    cli = Cli()
    cli.parse(sys.argv)

if __name__ == '__main__':
    main()
