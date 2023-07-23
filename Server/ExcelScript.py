from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
from datetime import datetime



class ExcelPython:
    def __init__(self):
        # ID ARCHIVO
        self.__id_hoja = "16ZVfDCOkYjODuDRL-76xWENl_gogxmSjqusS96QZjdI"
        # SHEET SERVICE
        creds_dict = json.load(open("./token/token.json"))
        credenciales = Credentials.from_authorized_user_info(info=creds_dict)
        self.sheet_service = build('sheets', 'v4', credentials=credenciales)





    # BUSCA EL ID EN LA PRIMERA COLUMNA
    def __buscar_id(self, mail):
        rango = "Panel!E1:E200"
        valores = self.sheet_service.spreadsheets().values().get(
                spreadsheetId=self.__id_hoja,
                range=rango
            ).execute()
        resultado = []
        for index, valor in enumerate(valores.get('values', [])):
            if valor[0] == mail: 
                resultado.append(index+1)
        return resultado



    # MODIFICA UNA ROW QUE ESPECIFIQUEMOS
    def __modificar_row(self, index, letter, valor):
        rango_fecha = f"Panel!{letter}{index}"
        nuevo_valor = [[str(valor)]]
        body = {'values': nuevo_valor}        
        self.sheet_service.spreadsheets().values().update(
            spreadsheetId=self.__id_hoja,
            range=rango_fecha,
            valueInputOption='RAW',
            body=body
        ).execute()



















    # MODIFICAR GENERAL
    def modificar_general(self, 
                        saldo_actual, recogida,
                        email ):
        respuesta = "NO EXISTE EL ID"
        resultado =  self.__buscar_id(email)
        if len(resultado) > 0:
            index = resultado[0]
            self.__modificar_row(index=index, letter="A", valor=datetime.now())
            self.__modificar_row(index=index, letter="B", valor=puntos)
            self.__modificar_row(index=index, letter="C", valor=saldo_actual)
            self.__modificar_row(index=index, letter="D", valor=recogida)
            respuesta = "MODIFICADO"
        return respuesta
