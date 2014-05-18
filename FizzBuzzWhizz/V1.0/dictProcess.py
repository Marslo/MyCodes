# =============================================================================
#    FileName: dictProcess.py
#        Desc:
#      Author: Marslo
#       Email: marslo.jiao@gmail.com
#     Created: 2014-05-15 11:28:32
#     Version: 0.0.1
#  LastChange: 2014-05-17 22:16:06
#     History:
#              0.0.1 | Marslo | init
# =============================================================================

import sys

class IsValidArgus:
  """ Analysis argus, and add the valid argu into the dict (self.rel) """

  def __init__(self):
    sourcefile = sys.argv[0].replace('.\\', '')
    self.argulist = sys.argv[1:]

    self.passwd = ['Fizz', 'Buzz', 'Whizz']
    self.rel = {'fizz': 3, 'buzz': 5, 'whizz': 7, 'scope': 100}

    self.__info_getargs = 'Please input three Positive Integers divided by comma (default is 3,5,7). [Enter. UnitTest press <Enter>]:\n'

    self.__error_help = '\nCheck the valid options by inputing: $ python ' + sourcefile + ' --help'
    self.__error_nondigit = 'Error:\n\tThe value can ONLY be Positive Integer' + self.__error_help
    self.__error_nagativdig = 'Error:\n\tThe value can NOT be Nagative.'
    self.__error_nonopts = 'Error:\n\tThe options is invalid.' + self.__error_help
    self.__error_moreints = 'Error:\n\tThe valud Only can be THERR Positive Integers.'

    self.helpInfo = 'NAME\n\t' + sourcefile + ' - Print the Fizz, Buzz and Whizz password' + \
                    '\nUSAGE\n\t' + sourcefile + ' < [--help] | [ --fizz=n ] | [ --buzz=n ] | [ --whizz=n ] | [ --scope=n ] >' + \
                    '\nSYNOPSIS\n\tpython' + sourcefile + ' [Options]' + \
                    '\nOPTIONS' + \
                    '\n\t--fizz=TheFirstNumber\n\t\tDefault: 3, it will replaced by Fizz.' + \
                    '\n\t--buzz=TheSecondNumber\n\t\tDefault: 5. It will replaced by Buzz.' + \
                    '\n\t--whizz=TheThirdNumber\n\t\tDefault: 7. It will replaced by Whizz.' + \
                    '\n\t--scope=TheScopeNumber\n\t\tThe Scope. Default: 100.' + \
                    '\nEXAMPLE' + \
                    '\n\tpython' + sourcefile + \
                    '\n\tpython' + sourcefile + ' 3 5 7' + \
                    '\n\tpython' + sourcefile + ' --whizz=8' + \
                    '\n\tpython' + sourcefile + ' --fizz=3 --buzz=5 --whizz=7' + \
                    '\n\tpython' + sourcefile + ' 3 5 7 --scope=100' + \
                    '\nAUTHOR' + \
                    '\n\tThis program made by Marslo Jiao (marslo.jiao@gmail.com)'


  def argusValidity(self, argu):
    """ Check the validity for argus """
    try:
      if 0 < int(argu):
        return True
    except:                                 # For Non-Integer and Float
      print self.__error_nondigit
      exit(1)
    else:                                   # For Nagatives
      print self.__error_nagativdig
      exit(1)

  def optValidity(self, opt):
    """ Check the validity for Options """
    if opt in self.rel.keys():
      return True
    else:
      print self.__error_nonopts
      exit(1)

  # Analysis the argus with Options (--fizz=3, --scope=200)
  def analysisArgus(self, argu):
    """ Analysis the Argus with Options """
    argu_key = argu.split('--')[-1].split('=')[0]
    argu_value = argu.split('=')[-1]
    if self.optValidity(argu_key) and self.argusValidity(argu_value):
      self.rel[argu_key] = int(argu_value)

  # Analysis the argus without Options
  def analysisNoptionArgus(self):
    """ Analysis the Argus without Options """
    for i in range(len(self.argulist)):
      argu = self.argulist[i]
      if self.argusValidity(argu):
        self.rel[self.passwd[i].lower()] = int(argu)

  def inputArgusProcess(self):
    """ Process the situation for Non-argus """
    try:
      argus = raw_input(self.__info_getargs)
      if 0 == len(argus):
        self.argulist = [3, 5, 7]
      elif 2 < argus.count(','):
        print self.__error_moreints
        exit(1)
      else:
        self.argulist = [i.strip() for i in argus.split(',')]
    except:
      exit(0)                               # Exists by pressing Ctrl+C

  def createRelDict(self):
    """ Add the valid argus into dict """
    if 0 == len(self.argulist):
      self.inputArgusProcess()
    elif 1 == len(self.argulist) and 'help' in self.argulist[-1]:
      print self.helpInfo
      exit(0)
    else:
      i = 0
      while i < len(self.argulist):
        argu = self.argulist[i]
        if '=' in argu:
          self.analysisArgus(argu)
          self.argulist.remove(argu)
        else:
          i = i + 1
    self.analysisNoptionArgus()

    return self.rel

# vi:set tabstop=2 shiftwidth=2 shiftwidth=2:
