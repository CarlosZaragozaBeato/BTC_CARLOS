from fastapi import FastAPI
from ExcelScript import ExcelPython



app = FastAPI()


excel_python = ExcelPython()



@app.get("/update/")
def actualizar_row(puntos:str, saldo_actual:str, saldo_anterior:str, mail:str, bono:str):
    
    return excel_python.modificar_general(puntos=puntos,saldo_actual=saldo_actual,
                                        saldo_anterior=saldo_anterior, mail=mail,
                                        bono=bono)





