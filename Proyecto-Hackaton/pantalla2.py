from controladores.instalar import execute
execute()


import keyboard
import numpy as np
import cv2
import mediapipe as mp
from recursos.LetrasEstaticas_2 import letras_estaticas_2



# Inicializar MediaPipe
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Captura de la cámara
cap = cv2.VideoCapture(0)


# Inicializar el modelo de detección de manos 
hands = mp_hands.Hands(
    max_num_hands =1
    
)


# Crear una ventana separada para la letra
ventana_letra = cv2.namedWindow("Letra Detectada")


# Diccionario de letras y colores
letras_colores = {
    'A': (0, 255, 0),  # Rojo
    'B': (0, 255, 0),  # Verde
    'C': (0, 255, 0),  # Azul
    'D':(0, 255, 0),
    'E':(0, 255, 0), 
    'F':(0, 255, 0), 
    'G':(0, 255, 0), 
    'I':(0, 255, 0),
    'K':(0, 255, 0),
    'L':(0, 255, 0),
    'M':(0, 255, 0),
    'N':(0, 255, 0),
    'O':(0, 255, 0),
    'P':(0, 255, 0),
    'Q':(0, 255, 0),
    'R':(0, 255, 0),
    'S':(0, 255, 0),
    'T':(0, 255, 0),
    'U':(0, 255, 0),
    'V':(0, 255, 0),
    'X':(0, 255, 0),
    'Y':(0, 255, 0),
    'GRACIAS':(0, 255, 0)
    
    

     
    # Agrega más letras y colores aquí
}
def F_borrarletra(frase):
    if len(frase)>0:
        print('Letra borrada:',frase[-1])
        del(frase[-1])
        print(frase)
        
    return frase
def F_palabra(letra,frase,ultimaletra):
    
    if len(frase)>0:
        if frase[-1] != ultimaletra:
            
            frase.append(letra)
            print(frase)
    else:
        frase.append(letra)
        print(frase)

    return frase
    
 

def dibujar_letra(imagen, letra, ancho_imagen, altura_imagen, color_principal, sombra=True):
    fuente = cv2.FONT_HERSHEY_COMPLEX
    escala = 2  # Reducido el tamaño de la letra
    grosor = 2
    sombra_offset = 3
    """for idx,handLms in enumerate(results.multi_hand_landmarks):

        label =results.multi_handedness[idx].classification[0].label
    print('Mano:',label)"""
    # Calcular el tamaño de la letra para centrarla
    (ancho_letra, altura_letra), _ = cv2.getTextSize(letra, fuente, escala, grosor)
    posicion_letra = (ancho_imagen // 2 - ancho_letra // 2, altura_imagen - 50)  # Centrada y a 50 píxeles del borde inferior

    if sombra:
        # Dibujar sombra (offset en negro)
        cv2.putText(imagen, letra, (posicion_letra[0] + sombra_offset, posicion_letra[1] + sombra_offset),
                    fuente, escala, (0, 0, 0), grosor + 2, cv2.LINE_AA)
    
    # Dibujar letra principal
    cv2.putText(imagen, letra, posicion_letra, fuente, escala, color_principal, grosor, cv2.LINE_AA)

frase =[]
ultimaletra =""
añadirpalabra = False
posiciones_v = []
cap = cv2.VideoCapture(0)

while True:
    
    success, image = cap.read()
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    if not success:
        break
    # Procesar la imagen con MediaPipe
    results = hands.process(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if keyboard.is_pressed('e'):
        print("Iniciado añadir palabra")
        añadirpalabra = True
    if keyboard.is_pressed('t'):
        print("Acabado añadir palabra")
        añadirpalabra= False
    if keyboard.is_pressed('m'):
        print("borrar una letra")
        F_borrarletra(frase)
    if keyboard.is_pressed('j'):
        frasecita = ""
        print('intentando crear frase')
        for i in frase:
            frasecita = frasecita + i
        print(frasecita)
        imagen_letra = np.zeros((altura_imagen, ancho_imagen,3), dtype="uint8")
        dibujar_letra(imagen_letra, frasecita, ancho_imagen, altura_imagen, color)
        cv2.imshow("Letra Detectada", imagen_letra)    
   
    
    # Obtener dimensiones de la imagen
    import tkinter as tk

    root = tk.Tk()
    ancho_imagen = int(root.winfo_screenwidth()/4)
    altura_imagen = int(root.winfo_screenheight()/4)

    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            
            for letra, color in letras_colores.items():
                if letra == 'V':
                    if (letras_estaticas_2.detectar_letra_V)(hand_landmarks.landmark):
                        # Guardar la posición de la mano (dedo índice)
                        posiciones_v.append((landmarks[8].x, landmarks[8].y))
                
                        # Verificar si ha habido movimiento
                        if len(posiciones_v) > 2:
                            x_mov = posiciones_v[-1][0] - posiciones_v[-2][0]
                            y_mov = posiciones_v[-1][1] - posiciones_v[-2][1]
                            
                            if abs(x_mov) > 0.05 or abs(y_mov) > 0.05:  # Umbral de movimiento
                                imagen_letra = np.zeros((altura_imagen, ancho_imagen,3), dtype="uint8")
                                # Dibujar la letra en la imagen en blanco
                                dibujar_letra(imagen_letra, letra, ancho_imagen, altura_imagen, color)
                                # Mostrar la imagen de la letra en la ventana separada
                                cv2.imshow("Letra Detectada", imagen_letra)
                                break
                else:
                    if getattr(letras_estaticas_2, f"detectar_letra_{letra}")(hand_landmarks.landmark):
                        # Crear una imagen en blanco para la ventana de la letra
                        imagen_letra = np.zeros((altura_imagen, ancho_imagen,3), dtype="uint8")
                        ultimaletra = letra
                        if añadirpalabra == True:
                            F_palabra(letra,frase,ultimaletra)
                        
                    
                        dibujar_letra(imagen_letra, letra, ancho_imagen, altura_imagen, color)
                        # Mostrar la imagen de la letra en la ventana separada
                        cv2.imshow("Letra Detectada", imagen_letra)
                        break  # Salir del bucle for si se detecta una letra

# Mostrar la imagen de la cámara
    cv2.imshow("Cámara", image)

    # Salir del bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) == ord('q'):
        break
    
    
# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()
# & 0xFF

