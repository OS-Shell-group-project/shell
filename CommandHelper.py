#!/usr/bin/env python3
import sys, os
import Commands
#from CommandHelper import CommandHelper


class CommandHelper(object):
  def __init__(self):
      self.commands = {}
      self.commands['ls'] = Commands.ls
      self.commands['cat'] = Commands.cat
      self.commands['head'] = Commands.head
      self.commands['pwd'] = Commands.pwd
      self.commands['cd'] = Commands.cd
      self.commands['mkdir'] = Commands.mkdir
      self.commands['rm'] = Commands.rm
      self.commands['x'] = Commands.exit

  def invoke(self, **kwargs):
      if 'cmd' in kwargs:
          cmd = kwargs['cmd']
      else:
          cmd = ''

      if 'params' in kwargs:
          params = kwargs['params']
      else:
          params = []

      if 'thread' in kwargs:
          thread = kwargs['thread']
      else:
          thread = False

      # One way to invoke using dictionary
      if not thread:
          self.commands[cmd](params=params)
      # else:
      #     # Using a thread ****** broken right now *********
      #     if len(params) > 0:
      #         c = threading.Thread(target=self.commands[cmd], args=tuple(kwargs))
      #     else:
      #         c = threading.Thread(target=self.commands[cmd])

          # c.start()
          # c.join()
      
  def exists(self, cmd):
      return cmd in self.commands


ch = CommandHelper()

while 1: 
    command_input = input('% ')

    command = command_input.split()[0]

    cmd_params = command_input.split()[1:]

    # if command exists in our shell
    if ch.exists(command):
        ch.invoke(cmd=command, params=cmd_params, thread=False)
    else:
        print("Error: command %s doesn't exist." % (command))

    path = os.getcwd() # use .getcwd to get the path of current location