
import time
from subprocess import call
import pymysql
import pyperclip as portapapeles
import smtplib
import pyautogui
import mail

gmail_user="bheghyd@gmail.com"
gmail_password = 'ignium2018'


############### CONFIGURAR ESTO ###################
# Abre conexion con la base de datos
##################################################

# prepare a cursor object using cursor() method

saldo_inicial = 0.0012
acum=0
bonus=0
parcial=0
         
url = "http:\\\\localhost\\\\freebit\\\\actualiza.php";

inicio = """
            $('#play_without_captchas_button').click();
            var ptos=document.getElementsByClassName("reward_table_box br_0_0_5_5 user_reward_points font_bold")[0].innerHTML;
            var hora = 0 ;
            ptos = parseInt ( ptos.replace ( "," ,"") ) ;
            var b1 = 0 ;
            if (document.getElementById("play_without_captchas_button"))
            {
                Activa = 0 ;
            }
            else
            {
                Activa = 1 ;
            }
            if ( ptos >= 1200 && Activa == 1 )
            {
                    if ( document.getElementById("bonus_span_free_points"))
                    {
                            b1 = 1 ;
                            hora = document.getElementById("bonus_span_free_points").innerHTML
                            hora = hora.slice(0,2);
                    }
                    else
                    {
                            $('#').click(RedeemRPProduct('free_points_100'))
                            hora = 23 ;
                            b1 = 1 ;
                    }
            }
            if (document.getElementById("bonus_span_fp_bonus"))
            {
                b2 = 2 
            }
            else
            {
                    ptos = ptos ;
                    if ( ptos >= 604 )
                    {
                            $('#').click(RedeemRPProduct('fp_bonus_1000'));
                            b2 = 2 ;
                    }
                    else
                    {
                            b2 = 0 ;
                    }
            }
            ptos=document.getElementsByClassName("reward_table_box br_0_0_5_5 user_reward_points font_bold")[0].innerHTML;
            ptos = parseInt ( ptos.replace ( "," ,"") ) ;
            $('#free_play_form_button').click();
            var recoge = document.getElementById("winnings").innerHTML ;
            var cuenta=document.getElementById("edit_profile_form_email").value;
            var bonus = document.getElementById("bonus_account_balance").innerHTML; bonus = bonus.replace("BTC","") ;bonus = parseFloat ( bonus ) ; 
            bono = document.getElementsByClassName('dep_bonus_max');bono = bono[0].innerHTML;bono = bono.replace(" BTC","") ;
            var numero = document.getElementById("balance").innerHTML ; numero = parseFloat( numero ); res = numero + bonus ;
            var llevas = document.getElementById("fp_bonus_req_completed").innerHTML;
            var server = $('#next_server_seed_hash').val();
            var monedero = $('#main_deposit_address').val();
            url = '%s?cuenta=' + cuenta + '&ptos=' + ptos + '&saldo=' + res + '&b1=' + b1 + '&b2=' + b2 + '&Activa=' + Activa + '&faltan=' + hora + '&bono=' + bono + '&server=' + server +'&monedero=' + monedero;
            document.querySelector('body').innerHTML= url.link(url);

         """ %url

#inicio += 'location. href = url ;'



bono1 = "$('#').click(RedeemRPProduct('free_points_100'))"

bono2 = "$('#').click(RedeemRPProduct('fp_bonus_1000'))"

bono1y2 = "$('#').click(RedeemRPProduct('free_points_100'));$('#').click(RedeemRPProduct('fp_bonus_1000'));"

print ( time.time() )
print ( time.strftime('%d %b %y %H:%M:%S') )


while  True:

    #cadena="C:\\free\\nuevofirefox\\up.exe"
    #call(cadena)
    '''
    db = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='btc',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    cursor = db.cursor()
    cursor.execute("SELECT count(*) hay FROM free " )
    data = cursor.fetchone()
    print(data)
    #if time.strftime('%H') == '00' :
        #cursor.execute("SELECT sum(saldo_actual) FROM free " )
        #saldo = cursor.fetchone()
        #saldo_inicial = saldo[0]
        #db.close()
        
    cuentas = data['hay']
    '''
    cuentas = 3
    call ("TASKKILL /F /IM firefox.exe")
    #call ( "C:\\free\\inicia.bat")

    empieza = time.time()

    i = 1 
    while i <= cuentas :
        
        #db = pymysql.connect("localhost","root","","free")
        #cursor = db.cursor()
        #cursor.execute("SELECT * FROM free WHERE id = %s " %i )
        #data = cursor.fetchone()
        #db.close()

        #b1 = data[10]
        #b2 = data[11]
        #activa = data[12]
        #puntos = data[6]
        #faltan = data[9]
        a = ""

        portapapeles.copy( inicio ) 

        portapapeles.paste()    

        call ("TASKKILL /F /IM firefox.exe")
        cadena="abrir.bat %s" %i
        call(cadena)
        time.sleep(2.5)
        pyautogui.moveTo(645,552)
        pyautogui.click()
        time.sleep(4)
        pyautogui.moveTo(645,552)
        pyautogui.click()
        time.sleep(10)
        
        pyautogui.press("F12")
        time.sleep(4)
        
        print('consola')
        pyautogui.press("F12")
        pyautogui.press("F12")
        time.sleep(3)        
        pyautogui.moveTo(98,952)
        time.sleep(0.5)
        pyautogui.click()
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        pyautogui.moveTo(342,102)
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.hotkey("ctrl", "W")
        pyautogui.hotkey("ctrl", "W")
        call ("TASKKILL /F /IM firefox.exe")
        tarda = time.time()
        print ( i ," Tarda " , tarda- empieza )
        i+=1
    
    cursor.execute("SELECT sum(saldo_actual) ahora ,sum(saldo_antes) antes FROM free " )
    data = cursor.fetchone()
    mail.envio(data)
        
    i=0

    print ( time.strftime('%d %b %y %H:%M:%S') )
    acabe = time.time()
    duracion = acabe-empieza
    print ( "Tiempo empleado " , duracion )
    pausa = 3680 - duracion
    if pausa >0 :
        time.sleep(pausa)
  
