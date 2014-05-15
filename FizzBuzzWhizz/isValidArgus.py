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
    self.argulist = sys.argv

    self.passwd = ['Fizz', 'Buzz', 'Whizz']
    self.rel = {'first': {'num': '3', 'passwd': 'Fizz'}, 'second': {'num': '5', 'passwd': 'Buzz'}, 'thrid': {'num': '7', 'passwd': 'Whizz'}}

    self.__info_1st = 'Please input the first number: '
    self.__info_2nd = 'Please input the second number: '
    self.__info_3rd = 'Please input the third number: '

    sourcefile = sys.argv[0].replace('.\\', '')
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
  def createRelDict(self):
    if 1 == len(self.argulist):
      # return self.rel
      print self.rel
    elif 2 == len(self.argulist) and 'help' in self.argulist[-1]:
      print self.helpInfo
      exit(0)
    else:
      for i in range(1, len(self.argulist)):
        argu = self.argulist[i]
        if '=' in argu:
          self.analysisArgus(argu)
        else:
          self.analysisNoptionArgus(argu)


  def argusValidity(self):
    pass

  def analysisArgus(self, str):
    pass


    print 'analyssisArgus'
    print str

  def analysisNoptionArgus(self, str):
    print 'analysisNoptionArgus'
    print str




ivn = IsValidNumber()
ivn.argusValidity()
ivn.createRelDict()
# ivn.getArgus()

# vi:set tabstop=2 shiftwidth=2:
