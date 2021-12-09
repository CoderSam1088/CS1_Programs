import random
import time
import schedule
from twilio.rest import Client
from Positivequotelist import choosequote
from scheduler import runjob, runjob2
from twiliotest import sendtext




if __name__=="__main__":
    runjob2(sendtext, 9547294808)
    



