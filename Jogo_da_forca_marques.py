import time
from random import choice

def forca():
    control = False
    vidas = 0
    print("Olá, seja bem-vindo ao jogo da forca.")
    time.sleep(1)
    while control == False:
        resp_user = input("""Selecione a dificuldade:
    1 - Fácil
    2 - Médio
    3 - Difícil
    4 - Lendário
""")
        
        if resp_user == "1":
            vidas = 15
            control = True
        elif resp_user == "2":
            vidas = 10
            control = True
        elif resp_user == "3":
            vidas = 5
            control = True
        elif resp_user == "4":
            vidas = 3
            control = True
        else:
            "Escreva um valor válido."
    lista_palavras = ["gato", "waldyr", "sport", "bolsonaro"]

    palavra_sorteada = choice(lista_palavras)

    tamanho_palavra = []
    for i in range(len(palavra_sorteada)):
        tamanho_palavra.append("_")

    controlador = False
    while controlador == False:
        letra_user = input(f"""**************************************************************************************************************************************************
*                |                                           ************************ *
*              ******                                        ************************ *
*            * ⦿  ⦿   *                                      ************************ *   
*            *        *                                        |                    * *  
*              ******                                          |                    * *
*                *                                             |                    * *
*    ——————————— * ———————————                                * *                   * *
*                *                                           *   *                  * *
*                *                                            * *                   * *
*                *                                                                  * *
*                *                                                                  * *        Vidas: {vidas}
*               / \                                                                 * *        Palavra: {' '.join(tamanho_palavra)}                        
*              /   \                                                                * *
*             /     \                                                               ***
**************************************************************************************************************************************************
Digite uma letra: """)
        letra_user = letra_user.strip()
        letra_user = letra_user.lower()

        if len(letra_user) != 1:
            print("Por favor, digite UMA letra.")
        elif not letra_user.isalpha():
            print("Por favor, utilize apenas letras.")
        else:
            correspondencia = False
            for x, letra in enumerate(palavra_sorteada):
                if letra == letra_user:
                    tamanho_palavra[x] = letra_user
                    correspondencia = True
            if correspondencia == False:
                print("Essa letra não está na palavra.")
                vidas = vidas - 1

        if "_" not in tamanho_palavra:
            print(f"""**************************************************************************************************************************************************
*                |                                           ************************ *
*              ******                                        ************************ *
*            * ⦿  ⦿   *                                      ************************ *   
*            *        *                                        |                    * *  
*              ******                                          |                    * *
*                *                                             |                    * *
*    ——————————— * ———————————                                * *                   * *
*                *                                           *   *                  * *
*                *                                            * *                   * *
*                *                                                                  * *
*                *                                                                  * *
*               / \                                                                 * *        Vidas: {vidas}                           
*              /   \                                                                * *        Palavra: {' '.join(tamanho_palavra)}
*             /     \                                                               ***
**************************************************************************************************************************************************""")
            print(f"""Parabéns, você acertou!
A palavra era: {palavra_sorteada}""")
            resp = input("Deseja jogar novamente? y/n")
            resp = resp.strip()
            resp = resp.lower()
            if resp ==  "y":
                controlador = True
                forca()
            else:
                controlador = True
        if vidas == 0:
            print(f"""**************************************************************************************************************************************************
*                |                                           ************************ *
*              ******                                        ************************ *
*            * ⦿  ⦿   *                                      ************************ *   
*            *        *                                        |                    * *  
*              ******                                          |                    * *
*                *                                             |                    * *
*    ——————————— * ———————————                                * *                   * *
*                *                                           *   *                  * *
*                *                                            * *                   * *
*                *                                                                  * *
*                *                                                                  * *
*               / \                                                                 * *        Vidas: {vidas}                           
*              /   \                                                                * *        Palavra: {' '.join(tamanho_palavra)}
*             /     \                                                               ***
**************************************************************************************************************************************************""")
            print(f"""Você perdeu!
A palavra era: {palavra_sorteada}""")
            resp = input("Deseja jogar novamente? y/n")
            resp = resp.strip()
            resp = resp.lower()
            if resp ==  "y":
                controlador = True
                forca()
            else:
                controlador = True

forca()