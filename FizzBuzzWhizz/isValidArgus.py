# =============================================================================
#    FileName: isValidArgus.py
#        Desc:
#      Author: Marslo
#       Email: marslo.jiao@gmail.com
#     Created: 2014-05-15 11:28:32
#     Version: 0.0.1
#  LastChange: 2014-05-15 17:47:10
#     History:
#              0.0.1 | Marslo | init
# =============================================================================

import sys

class IsValidNumber:
  def __init__(self):
    sourcefile = sys.argv[0].replace('.\\', '')
    self.argulist = sys.argv[1:]

    self.passwd = ['Fizz', 'Buzz', 'Whizz']
    self.rel = {'first': {'num': '3', 'passwd': 'Fizz'}, 'second': {'num': '5', 'passwd': 'Buzz'}, 'third': {'num': '7', 'passwd': 'Whizz'}}


    self.__info_1st = 'Please input the first number: '
    self.__info_2nd = 'Please input the second number: '
    self.__info_3rd = 'Please input the third number: '

    self.__error_nondigit = 'Error:\n\tThe value should be digit.\nCheck help by input: python ' + sourcefile + ' --help'
    self.__error_nonopts = 'Error:\n\tThe options is invalid.\nYou can check the valid options by input: python ' + sourcefile + ' --help'
    self.__error_errdig = 'Error:\n\tPlease input the Positive integers.'

    self.helpInfo = 'NAME\n\t' + sourcefile + ' - Print the Fizz, Buzz and Whizz password' + \
                    '\nUSAGE\n\t' + sourcefile + ' < [--help] >' + \
                    '\nSYNOPSIS\n\tpython' + sourcefile + '[Options]' + \
                    '\nOPTIONS' + \
                    '\n\t--first=TheFirstNumber\n\t\tDefault: 3, it will show Fizz.' + \
                    '\n\t--second=TheSecondNumber\n\t\tDefault: 5. It will show Buzz.' + \
                    '\n\t--third=TheThirdNumber\n\t\tDefault: 7. It will show Whizz.' + \
                    '\n\t--scope=TheScopeNumber\n\t\tThe Scope. Default: 100.' + \
                    '\nEXAMPLE' + \
                    '\n\tpython' + sourcefile + ' 3 5 7' + \
                    '\n\tpython' + sourcefile + ' --first=3 --second=5 --third=7'

  def argusValidity(self, argu):
    if argu.isdigit():
      if 0 > int(argu):
        return True
      else:
        print self.__error_errdig
        exit(1)
    else:
      print self.__error_nondigit
      exit(1)

  def optValidity(self, opt):
    if opt in self.rel.keys():
      return True
    else:
      print self.__error_nonopts
      exit(1)

  def createRelDict(self):
    if 0 == len(self.argulist):
      # return self.rel
      print self.rel
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

    print self.rel

  def analysisArgus(self, argu):
    argu_key = argu.split('--')[-1].split('=')[0]
    argu_value = argu.split('=')[-1]
    if self.optValidity(argu_key) and self.argusValidity(argu_value):
      self.rel[argu_key]['num'] = argu_value

  def analysisNoptionArgus(self):
    for i in self.argulist:
      print '-'*20
      print 'i is: ', i
      if self.argusValidity(i):
        for pwd in self.passwd:
          print [k for k, v in self.rel.items() if pwd == v['passwd']][0]



ivn = IsValidNumber()
ivn.createRelDict()
# ivn.getArgus()

# vi:set tabstop=2 shiftwidth=2:
