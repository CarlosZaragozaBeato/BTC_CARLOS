from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import json
from datetime import datetime



class ExcelPython:
    def __init__(self):
        # ID ARCHIVO
        self.__id_hoja = "1qVPAe1tRfOwV-4nlQ2UUBV2NmJQ_19u7QNh4D1gMFJo"
        # SHEET SERVICE
        creds_dict = json.load(open("./token/token.json"))
        credenciales = Credentials.from_authorized_user_info(info=creds_dict)
        self.sheet_service = build('sheets', 'v4', credentials=credenciales)
        self.archivo = self.__buscar_hoja_general()


    # SE PUEDE QUITAR
    def __buscar_hoja_general(self):
        range_name = "Panel!A1:H60"
        return self.sheet_service.spreadsheets().values().get(
                spreadsheetId=self.__id_hoja,
                range=range_name
            ).execute()
    
    
    # BUSCA EL ID EN LA PRIMERA COLUMNA
    def __buscar_id(self, mail):
        rango = "Panel!H1:H60"
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
    def modificar_general(self, puntos, saldo_actual, 
                        saldo_anterior, bono,mail):
        
        respuesta = ""
        resultado =  self.__buscar_id(mail)
        if len(resultado) > 0:
            
            index = resultado[0]
            
            # horas_activo = self.__calcular_horas_activo(id)
            self.__modificar_row(index=index, letter="B", valor=datetime.now())
            self.__modificar_row(index=index, letter="C", valor=puntos)
            self.__modificar_row(index=index, letter="D", valor=saldo_actual)
            self.__modificar_row(index=index, letter="E", valor=saldo_anterior)
            self.__modificar_row(index=index, letter="F", valor=bono)
            # self.__modificar_row(index=index, letter="G", valor=horas_activo)
            # respuesta = "MODIFICADO"
        else:
            respuesta = "NO EXISTE EL ID"
        return respuesta
    
    
    
    # TODO AÑADIR HORAS
    def __calcular_horas_activo(self):
        pass