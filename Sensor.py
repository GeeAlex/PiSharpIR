#Reading data from a Sharp GP2Y0E02B from a Raspi
#Written by Alexandre Gee
#WARNING: USE AT YOUR OWN RISK
#MAY CONTAIN SPAGHETTI CODE
import smbus
import math

#Registers.
#Note a lot of these registers may
#stay dormant or not have any function (yet).
#All the details are in the GP2Y0E02B application note.
bus = smbus.SMBus(1)            #Who has a Pi 1 Model A anyways?
GP2Y_ID = 0x40                  #Taken from i2cdetect
Hold_Bit = 0x01
Shift_Bit = 0x35
MEPW = 0x13                     #Maximum Emitting Pulse Width
Dist1 = 0x5E                    #Distance[11:4]
Dist2 = 0x5F                    #Distance[3:0]

############################################################
####################DISTANCE AND DATAREADING################
############################################################

def dataread(adr):
    return bus.read_byte_data(GP2Y_ID, adr)

def distcalc():
    global Distance
    D1 = dataread(Dist1)
    D2 = dataread(Dist2)
    SBit = dataread(Shift_Bit)
    S1proc = (D1 * 16)
    S2proc = (S1proc + D2)
    S3proc = (S2proc / 16)
    S4proc = (S3proc / math.pow(2, SBit))
    Distance = S4proc
    return Distance

    


