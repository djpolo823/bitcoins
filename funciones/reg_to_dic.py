def traduce_reg_a_dic(clase_usuario):
    registro= str(clase_usuario).replace("{","").replace("}","").replace("'","").replace(" ","").split(",")
    dic_saldos={}
    for n in range(len(registro)):
        datos=registro[n].split(":")
        dic_saldos[datos[0]]=float(datos[1])
    return dic_saldos