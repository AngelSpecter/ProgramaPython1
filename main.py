import os

def __Presentacion_Author__(): 
    print(" ******************************************************\n\t\tMiguel Angel Ayala");
    print("              INGENIERO EN COMPUTACION");
    print("                     ICO 2022\n*******************************************************");

def __Main_Menu__():
    print(" *** BIENVENID@ AL SISTEMA DE FUNCIONES BASICAS EN PYTHON ***");
    print(" \t1. CALCULADORA BASICA");
    print(" \t2. LISTA DE ELEMENTOS");
    print(" \t3. PROXIMAMENTE");
    op = int(input());
    if op == 1:
        __LIMPIAR__();
        __CALCULADORA__();
    elif op == 2: 
        print(" *** AGREGAREMOS FUNCIONES A LAS LISTAS COMO RECORRER, CALCULAR, Y MAS");
        print("INGRESA ALGUNA CADENA PARA TRABAJAR");
        cadena = input();
        print("ELIJE QUE DESEAS HACES CON ELLA ...");
        print("\t1. CONCATENAR\n\t2. MULTIPLICAR\n\t3. AGREGAR");
        op = int(input());
        if op == 1: 
            __LIMPIAR__();
            print(" CONCATENAREMOS CON UNA NUEVA CADENA QUE TU ESCRIBAS");
            newcade = input("NUEVA CADENA --> ");
            print(" LOS RESULTADOS SE TE MOSTRARAN AQUI ABAJO");
            input("PRESIONA ENTER PARA CONTINUAR . . .");
            fronconcate = newcade + cadena;
            backconcate = cadena + newcade;
            print(" LAS CADENAS QUEDAN DE LA SIGUIENTE FORMA\n\t",fronconcate,"\t",backconcate);
            print(" PRESIONE 1 PARA SALIR AL MENU PRINCIPAL O 2 PARA VER EL MENU DE CADENAS");
            elec = input();
            if elec == 1: 
                __Main_Menu__();
            else: 
                print("TRABAJANDO EN LA MODULARIDAD DE LOS MENUS FALTANTES");
                print("FIN DEL TRABAJO SIN MODULARIDAD");

def __CALCULADORA__():
    print("*** INGRESA LA OPERACION A REALIZAR ***");
    print(" NOTA: RECUERDA QUE ESTA SECCION ADMITE (+,-,*,/) POR SI SOLAS O COMBINADAS");
    cal = input(" TU OPERACION ES ? \n\t --> ");
    cal = eval(cal);
    print(" TU RESULTADO BUSCADO ES = ",{cal});
    __LIMPIAR__();
    print("DESEA CALCULAR UNA NUEVA OPERACION?");
    print("\n\t1. SI\n\t2. NO");
    res = int(input());
    if res == 1:
        __LIMPIAR__();
        __CALCULADORA__();
    else :
        __LIMPIAR__();
        __Main_Menu__();

def __LIMPIAR__():
    print("PRESIONA CUALQUIER TECLA . . .");
    input();
    os.system("clear");# CLEAR THE SCREEN CONTENT "cls" FOR WINDOWS USERS

def __main__():#PRINCIPAL FUNCTION
    print("INICIALIZANDO EL SISTEMA ...");
    __LIMPIAR__();
    __Presentacion_Author__();
    __LIMPIAR__();
    __Main_Menu__();

__main__();