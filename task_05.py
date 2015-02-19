#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using a combination of raw_input(), if, elif, and else, write a program that

asks the user their blood pressure. Compare the blood pressure against the

following chart and save the Status to a variable named BP_STATUS. At the end

of the program, print a nice sentence with a formatting string to tell you your

status and use .format() to replace the formatting string witH your BP_STATUS.
"""

MYINPUT = raw_input('what is blood pressure?\n')

MYINPUT = int(MYINPUT)

if MYINPUT >= 160:
    BP_STATUS = 'Emergency'

elif MYINPUT >= 140:
    BP_STATUS = 'High'

elif MYINPUT >= 120:
    BP_STATUS = 'Warning'

elif MYINPUT >= 90:
    BP_STATUS = 'Ideal'

else:
    BP_STATUS = 'Low'

OUTPUT = 'Your blood pressure is {}'.format(BP_STATUS)
print OUTPUT
