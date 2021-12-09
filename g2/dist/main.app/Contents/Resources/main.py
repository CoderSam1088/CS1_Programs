import random
import time
import schedule
from twilio.rest import Client
from Positivequotelist import choosequote
from scheduler import runjob
from twiliotest import sendtext




if __name__=="__main__":
    runjob(sendtext, 9547294808)
    



