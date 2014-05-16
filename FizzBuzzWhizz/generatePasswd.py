# =============================================================================
#    FileName: generatePasswd.py
#        Desc:
#      Author: Marslo
#       Email: marslo.jiao@gmail.com
#
#     Created: 2014-05-16 17:14:43
#     Version: 0.0.1
#  LastChange: 2014-05-16 17:14:43
#     History:
#              0.0.1 | Marslo | init
# =============================================================================

class FizzBuzzWhizz:
  def __init__(self, rel, passwd):
    self.rel = rel
    self.passwd = passwd

    self.pwdlist = []


  def generatePwdList(self):
    print self.rel
    print self.passwd

    for item in range(1, 20):
      self.pwdlist.append(str(self.calcPwd(item)))
      # print self.calcPwd(item)

    print self.pwdlist

  def calcPwd(self, item):
    if str(self.rel[self.passwd[0].lower()]) in str(item):
      return self.passwd[0]
    else:
      return ''.join(i for i in self.passwd if 0 == item % self.rel[i.lower()]) or item





# vi:set tabstop=2 shiftwidth=2:
