"""
15 Spring. Computer Network. Lab 9
"""


#help debugging (print out each steps or silent)
def print_details(X, *T, **D):
    print(X, *T, **D)

#sender blinking period
blink_duration = .1

#receiver oversampling ratio
oversampling_ratio = 4

import queue
import threading
import time
import random
import CN_Sockets

import time
import RPi.GPIO as GPIO

#---------------------------------------------------------------------------------------------------------------------------------
# #Preparation for Rasberry pi#
class Safeguards:
    def __enter__(self):
        return self
    def __exit__(self,*rabc):
        GPIO.cleanup()
        print("Safe exit succeeded")
        return not any(rabc)

def sending_prepare_pin(pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)

def receiving_prepare_pin(pin):
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(pin,GPIO.IN)

def turn_high(pin):
    GPIO.output(pin,GPIO.HIGH)

def turn_low(pin):
    GPIO.output(pin,GPIO.LOW)

def delay(duration):
    time.sleep(duration) 

def read_pin(pin):
    return GPIO.input(pin)

#Preparation#


#----------------------------------------------------------------------------------------------------------------------------#


#physical layer implementation

#sending and receiving pulsed
def send(bit):
    pin_signal = 17
    pin_status = 23
    receiving_prepare_pin(pin_status)
    receiving_prepare_pin(pin_signal)
    while True:
        if read_pin(pin_status):
            wait_time = random.randrange(10,20)
            print_details(" Layer1. The Channel is Occupied, wait for " + str(wait_time))
            delay(wait_time)
        else:
            print_details(" Layer1. start to send signals")
            sending_prepare_pin(pin_signal)
            sending_prepare_pin(pin_status)
            turn_high(pin_status)
            for i in bit:
                if i=="1":
                    #print_details("1")
                    turn_high(pin_signal)
                    delay(blink_duration)
                if i=="0":
                    #print_details("0")
                    turn_low(pin_signal)
                    delay(blink_duration)
            turn_low(pin_status)
            receiving_prepare_pin(pin_status)
            receiving_prepare_pin(pin_signal)
            print_details(" Layer1. sending ended")
            return



def receive(blink=1000,duration=.5,pin=17):
    receiver_duration = 1.0 * blink_duration / oversampling_ratio
    pin_signal = 17
    pin_status = 23
    receiving_prepare_pin(pin_signal)
    receiving_prepare_pin(pin_status)
    sequential_one = 0
    sequential_zero = 14 * oversampling_ratio
    
    pulse_temp = [0 for _ in range(blink * oversampling_ratio)]
    j=0

    while True:
        if read_pin(pin):
            if sequential_zero != 0:
                if sequential_zero < 2 * oversampling_ratio:
                    pulse_temp[j] = 1
##                    print_details("0")
                elif sequential_zero < 5 * oversampling_ratio:
                    pulse_temp[j] = 2
##                    print_details("000")
                else:
                    pulse_temp[j] = 3
##                    print_details("0000000")
                sequential_zero = 0
                j=j+1
            sequential_one+=1
            delay(receiver_duration)
        else:
            if sequential_one != 0:
                if sequential_one < 2 * oversampling_ratio:
                    pulse_temp[j] = 5
##                    print_details("1")
                else:
                    pulse_temp[j] = 6
##                    print_details("111")
                sequential_one = 0
                j=j+1
            if sequential_zero == 13 * oversampling_ratio:
                pulse_temp[j] = 3
                pulse_temp[j+1] = 9
                print_details(" Layer1. signal received")
                receive_router_analyze(pulse_temp, j)
                sequential_zero = 14 * oversampling_ratio
                j = 0
            if sequential_zero == 30*oversampling_ratio:
                while q_morse.qsize():
                    send(q_morse.get())
                sequential_zero = 14*oversampling_ratio
            sequential_zero+=1
            delay(receiver_duration)

def receive_router_analyze(pulse_temp, j):
    pulse = ""
    for i in range(j+1):
        if pulse_temp[i] == 1:
            pulse+="0"
        elif pulse_temp[i] == 2:
            pulse+="000"
        elif pulse_temp[i] == 3:
            pulse+="0000000"
        elif pulse_temp[i] == 5:
            pulse+="1"
        elif pulse_temp[i] == 6:
            pulse+="111"
        elif pulse_temp[i] == 9:
            break
    print_details(pulse)
    message = pulse
    m_s = stack()
    for layer in reversed(m_s.layers):
        message = layer.ascend(message)
    print_details(" Layer1. After physical layer: " + message)
    q_router.put(message)

#physical layer header
def add_header(bit):
    return bit
#    bit_header = "101010101010101000" + bit
#    return bit_header

def deheader(pulse):
    return pulse
#    j=0
#    x=0
#    for i in range(len(pulse)):
#        if pulse[i]=='1' and pulse[i+1]=='0':
#            j+=1
#        if j>=3 and pulse[i]=='0' and pulse[i+1]=='0' and pulse[i+2]=='0':
#            pulse=pulse[i+3:]
#            break
#        if i>50:
#            print_details(" Layer1. cannot find physical layer header")
#            break
#    # pulse = pulse.lstrip("0")
#    return pulse


#converting between sentence and morse code using mother_layer class and functions
class mother_layer:
    def __init__(self,function,inverse):
        self.descend=function
        self.ascend=inverse

#receiving dictionary
dict_m2l={".*-":"A","-*.*.*.":"B","-*.*-*.":"C","-*.*.":"D",".":"E",".*.*-*.":"F","-*-*.":"G",".*.*.*.":"H",".*.":"I",".*-*-*-":"J","-*.*-":"K",".*-*.*.":"L","-*-":"M","-*.":"N","-*-*-":"O",".*-*-*.":"P","-*-*.*-":"Q",".*-*.":"R",".*.*.":"S","-":"T",".*.*-":"U",".*.*.*-":"V",".*-*-":"W","-*.*.*-":"X","-*.*-*-":"Y","-*-*.*.":"Z",".*-*-*-*-":"1",".*.*-*-*-":"2",".*.*.*-*-":"3",".*.*.*.*-":"4",".*.*.*.*.":"5","-*.*.*.*.":"6","-*-*.*.*.":"7","-*-*-*.*.":"8","-*-*-*-*.":"9","-*-*-*-*-":"0","*******":" "}
#sending dictionary
dict_l2m={"@":"*","A":".*-","B":"-*.*.*.","C":"-*.*-*.","D":"-*.*.","E":".","F":".*.*-*.","G":"-*-*.","H":".*.*.*.","I":".*.","J":".*-*-*-","K":"-*.*-","L":".*-*.*.","M":"-*-","N":"-*.","O":"-*-*-","P":".*-*-*.","Q":"-*-*.*-","R":".*-*.","S":".*.*.","T":"-","U":".*.*-","V":".*.*.*-","W":".*-*-","X":"-*.*.*-","Y":"-*.*-*-","Z":"-*-*.*.","1":".*-*-*-*-","2":".*.*-*-*-","3":".*.*.*-*-","4":".*.*.*.*-","5":".*.*.*.*.","6":"-*.*.*.*.","7":"-*-*.*.*.","8":"-*-*-*.*.","9":"-*-*-*-*.","0":"-*-*-*-*-"," ":"*******"}   

#words and letter_layer
class words_letter_layer(mother_layer):
    def __init__(self):
        super().__init__(words2letter,letter2word)

def words2letter(words):
    words = words.upper()
    letter = words.replace(" ", "@")
    return letter

def letter2word(letter):
    word=""
    for item in letter:
        for i in item:
            try:
                word=word+dict_m2l[i]
            except:
                pass
        word=word+" "
    return word

#letter and morse code layer#
class letter_morse_layer(mother_layer):
    """docstring for ClassName"""
    def __init__(self):
        super().__init__(letter2morse,morse2letter)

def letter2morse(letter):
    morse=""
    for i in letter:
        morse=morse+dict_l2m[i]
        morse=morse+"***"
    return morse

def morse2letter(morse):
    letter=[]
    sentence=morse.split("*******")
    for word in sentence:
        word=word.split("***")
        letter.append(word)     
    return letter

#morse code and pulse layer#
class morse_pulse_layer(mother_layer):
    """docstring for ClassName"""
    def __init__(self):
        super().__init__(morse2pulse,pulse2morse)

def morse2pulse(morse):
    global dict_m2p
    dict_m2p = {".":"1","-":"111","*":"0"}
    bit=""
    for i in morse:
        bit=bit+dict_m2p[i]
    bit = add_header(bit)
    return bit

def pulse2morse(pulse): 
    pulse=str(pulse)
    pulse=pulse.lstrip("0")
    pulse=deheader(pulse)
    morse=""
    for i in pulse:
        if i=="1":
            morse+="."
        if i=="0":
            morse+="*"
    morse=morse.replace("...","-")
    return morse

#----------------------------------------------------------------------------------
#data link layer implementation

def demac(message, mac):
    scr_mac = message[0:2]
    dst_mac = message[2:4]
    new_message = message[4:]
    if dst_mac != mac:
        print_details(" Layer2. MAC address not matched")
    return new_message

#----------------------------------------------------------------------------------------------------------------------------#
#checksum
def add_checksum(message):
    return message
#    return message+"checksum"+calc_checksum(message)

def calc_checksum(message):
    return 0
#        """
#        Calculates checksum for sending commands to the ELKM1.
#        Sums the ASCII character values mod256 and takes
#        the lower byte of the two's complement of that value.
#        """
#        message= message.replace(" ","")
#        checksum ='%2X' % (-(sum(ord(c) for c in message) % 256) & 0xFF)
#        return checksum

def de_checksum(message):
    return message
#    i=message.index("CHECKSUM")
#    checksum=message[i+8:]
#    message=message[:i]
#    if calc_checksum(message)==checksum:
#        return message
#    else:
#        print_details(" Layer2. de_checksum: checksum wrong")
#        return message

#----------------------------------------------------------------------------------
#network layer implementation
dic_ip_mac={'DA':'MA','DB':'MB','DC':'MC'}

def router_ip_to_mac(ip_addr):
    mac_addr = dic_ip_mac[ip_addr]
    return mac_addr

def router_add_mac(message, dst_mac):
    message=dst_mac+message
    message='MR'+message
    return message

def router_deip(message):
    src_ip=message[0:2]
    dst_ip=message[2:4]
    return dst_ip

def router_change_mac(message):
    src_ip=message[0:2]
    dst_ip=message[2:4]    
    new_dst_mac = router_ip_to_mac(dst_ip)
    payload=message[4:]
    print("Payload:",payload)
    new_message = router_add_mac(message, new_dst_mac)
    return new_message

def search_routing_table(message):
    dict_all_router = {"A":"192.168.128.103", "B":"192.168.128.110", "C":"192.168.128.111", "D":"192.168.128.102", "E":"192.168.128.106"}
    dst_ip = router_deip(message)
    dst_lan = dst_ip[0]
    dst_router_ip = dict_all_router[dst_lan]
    dst_router_port = 2048
    return dst_router_ip, dst_router_port

# def calc_ip_checksum(src_ip, dst_ip, next_p):
#     sum = 0
#     sum += ord(src_ip[0]) * 256 + ord(src_ip[1])
#     sum += ord(dst_ip[0]) * 256 + ord(dst_ip[1])
#     sum += ord(next_p)
#     cksum = sum%65536 + int(sum/65536)
#     if cksum >= 65536:
#         cksum = cksum%65536 + int(cksum/65536)
#     return (str(hex(cksum))[2:]).upper()

#-------------------------------------------------------------------------------------------------------------------
#Threads
q_morse = queue.Queue()
q_socket=queue.Queue()
q_router=queue.Queue()

def thread_morse():
    receive()

def thread_socket():
    socket, AF_INET, SOCK_DGRAM, timeout = CN_Sockets.socket, CN_Sockets.AF_INET, CN_Sockets.SOCK_DGRAM, CN_Sockets.timeout
    with socket(AF_INET, SOCK_DGRAM) as sock:
        IP,port="192.168.128.102",2048
        sock.bind((IP,port))            
        sock.settimeout(2.0) 
        print ("UDP Server started on IP Address {}, port {}".format(IP,port))
        while True:
            try:
                bytearray_msg, source_address = sock.recvfrom(1024) 
                source_IP, source_port = source_address
                print ("\nMessage received from ip address {}, port {}:".format(source_IP,source_port))
                message=bytearray_msg.decode("UTF-8")
                print (message)
                q_router.put(message) 

            except timeout:
                if not q_socket.empty():
                    message=q_socket.get()
                    dst_ip,dst_port=search_routing_table(message)
                    outlan_router_addr=(dst_ip,dst_port)
                    bytearray_message = bytearray(message,encoding="UTF-8")  
                    bytes_sent = sock.sendto(bytearray_message, outlan_router_addr) 
                    print ("{} bytes sent".format(bytes_sent))

                print (".",end="")
                continue       

#-------------------------------------------------------------------------------------------------------------------
lan_ip=["DA","DB","DC","DD"]

class mother_stack:

    def __init__(self, layers):
        self.layers = layers


    def router(self):
        threading.Thread(target=thread_morse).start()        
        threading.Thread(target=thread_socket).start()   
        while True:
            message = q_router.get()
            if message[0] == 'M':
                message=demac(message, 'MR')
                message=de_checksum(message)
                print_details(" Layer2. After data link layer: " + message)        
                dst_ip=router_deip(message)
                if dst_ip in lan_ip:
                    router_change_mac(message)
                    message=add_checksum(message)
                    print_details(" Layer1. Before physical layer: " + message)
                    for layer in self.layers:
                        message = layer.descend(message)
                    q_morse.put(message)
                else:
                    q_socket.put(message)
            else:
                dst_ip=router_deip(message)
                if dst_ip in lan_ip:
                    message = router_change_mac(message)
                    message=add_checksum(message)
                    print_details(" Layer1. Before physical layer: " + message)
                    for layer in self.layers:
                        message = layer.descend(message)
                    q_morse.put(message)
                else:
                    q_socket.put(message)


class stack(mother_stack):
    def __init__(self):
        super().__init__([
            words_letter_layer(),
            letter_morse_layer(),
            morse_pulse_layer()])


    
#----------------------------------------------------------------------------------------------------------------------------#


if __name__ == "__main__":

    print("*Router working*")
    s = stack()
    s.router()
