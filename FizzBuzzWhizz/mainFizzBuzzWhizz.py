# =============================================================================
#    FileName: mainFBW.py
#        Desc:
#      Author: Marslo
#       Email: marslo.jiao@gmail.com
#     Created: 2014-05-16 16:58:17
#     Version: 0.0.1
#  LastChange: 2014-05-16 17:14:17
#     History:
#              0.0.1 | Marslo | init
# =============================================================================

from dictProcess import IsValidArgus
from generatePasswd import FizzBuzzWhizz

if __name__ == '__main__':
    vargu = IsValidArgus()
    vargu.createRelDict()
    # print vargu.rel

    fbw = FizzBuzzWhizz(vargu.rel, vargu.passwd)
    fbw.generatePwdList()


