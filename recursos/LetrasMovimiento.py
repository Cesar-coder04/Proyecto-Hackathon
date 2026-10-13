import cv2
import mediapipe as mp
import numpy as np

# Inicializar mediapipe para la detección de manos
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

# Función para detectar la "V" con movimiento
def detectar_v_con_movimiento(landmarks):
    # Coordenadas de los dedos índice y medio
    x_indice, y_indice = landmarks[8].x, landmarks[8].y
    x_medio, y_medio = landmarks[12].x, landmarks[12].y
    
    # Coordenadas de los demás dedos (pulgar, anular, meñique)
    x_pulgar, y_pulgar = landmarks[4].x, landmarks[4].y
    x_anular, y_anular = landmarks[16].x, landmarks[16].y
    x_menique, y_menique = landmarks[20].x, landmarks[20].y

    # Verificar si los dedos índice y medio están extendidos y los demás doblados
    if (y_indice < y_pulgar and y_medio < y_pulgar and
        y_anular > y_indice and y_menique > y_medio):
        return True
    return False

# Inicializar variables para el seguimiento del movimiento
posiciones_v = []

# Abrir la cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a RGB
    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(img_rgb)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            landmarks = hand_landmarks.landmark
            
            if detectar_v_con_movimiento(landmarks):
                # Guardar la posición de la mano (dedo índice)
                posiciones_v.append((landmarks[8].x, landmarks[8].y))
                
                # Verificar si ha habido movimiento
                if len(posiciones_v) > 2:
                    x_mov = posiciones_v[-1][0] - posiciones_v[-2][0]
                    y_mov = posiciones_v[-1][1] - posiciones_v[-2][1]
                    
                    if abs(x_mov) > 0.05 or abs(y_mov) > 0.05:  # Umbral de movimiento
                        cv2.putText(frame, "Letra V detectada con movimiento", (50, 50), 
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    
    cv2.imshow('Deteccion Letra V', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
