import urllib.request
import json


#     MMMMMM   M                                                                                         MMMMMMMMMMMMMMMMMMMMM                                                                           
#      MMM+    MMM$7MMMN                                                                                 MMMMMMMMMMMMMMMMMMMMM                                                                           
#      .MM     .        M                                                                                MM                  $                                                                           
#      .MM               M                                                                               MM                                                                                              
#      .MM               M                                                                               MM                                                                                              
#      .MM               M                                                                               MM                                                                                              
#      .MM              .M                                                                               MM                                                                                              
#      .MM              M   MMMMMMMMMMM                    MMMMMMMMMMMM 8MMMMMMMMMM,                     MM                                  ?MMMM7,                                  MMMM               
#      .MM       M    MM.MM M        MM        MMMMMM      M           :8~        M,    M  M       M  M  MM                        MM:  MN  M     =8            MMM      :.   M.       MM                
#      .MM       M  +MM              MM              ~M    M                      M,       M       M     MM                          MMM   ?.                   MM       ?             MM                
#      .MM  M          MM            MM               .=   M                      M,       M       M     MM                            MM  .,                   $M       M             MM                
#      .MM ,MZ          D8           MM                M   M                      M,       M       M     MM                              M? D.                  ?D        M            MM                
#      .MM MMM           M           MM         MM  8Z M   M                      M,       M       M     MM                            MM    M                  M.         M$  MM      ~M    MM  M       
#      .MM MM            M           MM       =M       M   M                      M,       M       M     MM                           MD   ,7                   M        N:      M.     M    ,    =      
#      .MM DM            M           MM       M        M   M                      M,       M       M     MM                     M   MM     M                   ,8        M              MM         M     
#      .MM  M           M            MM      M?        M   M                      M,       M       M     MM                     MM MM      M           MM      M       M M               M         M     
#      :MM   M$       7M             MM   I  MM       .M   M                      M,       M       M     MM                      MMM        D        7MMM     .    .MMMM M          I     M        M     
#     :MMMM    NMMMMMD               MMMMM7 MMMM      MM  .M                      MMMMM    MMMMMMMMM    DMMM                   ~MZ ,M?       OM.   MMM      M    MMM      M.     MMMM      IM    8O      
#                                                                                                                                                           MMM+             NN                          

response = urllib.request.urlopen("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,LTC,ETH,XMR,MAID,DASH,EDR,ZEC,NXT,XRP&tsyms=USD")
print(response.read())
