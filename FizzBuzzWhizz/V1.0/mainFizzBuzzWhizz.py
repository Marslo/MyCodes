# =============================================================================
#    FileName: mainFizzBuzzWhizz.py
#        Desc:
#      Author: Marslo
#       Email: marslo.jiao@gmail.com
#     Created: 2014-05-16 16:58:17
#     Version: 0.0.1
#  LastChange: 2014-05-18 15:05:36
#     History:
#              0.0.1 | Marslo | init
# =============================================================================

import dictProcess
import generatePasswd

if __name__ == '__main__':
  vargu = dictProcess.IsValidArgus()
  vargu.createRelDict()

  fbw = generatePasswd.FizzBuzzWhizz(vargu.rel, vargu.passwd)
  fbw.generatePwdList()

# vi:set tabstop=2 shiftwidth=2 shiftwidth=2:
