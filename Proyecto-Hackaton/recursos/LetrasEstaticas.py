# Clase para detectar que letra estatica del abecedario está haciendo la mano

class letras_estaticas:
    
    # Funcion para detectar la letra 'A'
    def detectar_letra_A(landmarks):

        dedos_doblados = True # Inicializamos la variable que determinará si los dedos están o no doblados
        for i in [8, 12, 16, 20]:  
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser A
            if landmarks[i].y < landmarks[i-3].y or landmarks[i-1].y < landmarks[i-2].y:  
                dedos_doblados = False
                break
        
        
        pulgar_cerca = landmarks[4].x > landmarks[5].x # El pulgar debe estar flexionado 
        munyeca_correcta = landmarks[0].y > landmarks[1].y and landmarks[2].x < landmarks[17].x # la munyeca debe de estar por debajo de los dedos 
        return dedos_doblados and pulgar_cerca and munyeca_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
    # Funcion para detectar la letra 'B'
    def detectar_letra_B(landmarks):
        
        dedos_extendidos = True # Inicializamos la variable que determinará si los dedos están o no extendidos
        for i in [8, 12, 16, 20]: 
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser B
            if landmarks[i].x > landmarks[i-2].x:  
                dedos_extendidos = False
                break
        
        orientacion_correcta = landmarks[5].y < landmarks[9].y < landmarks[13].y < landmarks[17].y #Si los nudillo del dedo incice esta por encima de los demas es true 

        pulgar_cerca = landmarks[4].y > landmarks[3].y and landmarks[3].x < landmarks[2].x # Si el pulgar esta por detras de la palma es true

        return dedos_extendidos and pulgar_cerca and orientacion_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'C'
    def detectar_letra_C(landmarks):
        
        dedos_curvados = True # Inicializamos la variable que determinará si los dedos están o no curvados
        for i in [8, 12, 16, 20]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser C
            if landmarks[i].x > landmarks[i-3].x or landmarks[i-2].y > landmarks[i].y:
                dedos_curvados = False
                break
        
        pulgar_en_curva = landmarks[4].x < landmarks[3].x and landmarks[4].x < landmarks[5].x #Si el pulgar esta por delante del nudillo del dedo indice es true
        orientacion_correcta = landmarks[17].x < landmarks[0].x #Si el nudillo del dedo menyique tiene que estar por delante de la munyeca
        
        return dedos_curvados and pulgar_en_curva and orientacion_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'D'
    def detectar_letra_D(landmarks):
        indice_extendido = landmarks[8].y < landmarks[7].y < landmarks[6].y #Si la punta del indie esta por encima de los nudillos es true 
        dedos_doblados = True # Inicializamos la variable que determinará si los dedos están  doblados
        for i in [12, 16, 20]:  
         # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser D
            if landmarks[i].y < landmarks[i-3].y:  
                dedos_doblados = False
                break
        
        orientacion_correcta = landmarks[10].x < landmarks[5].x #Si el dedo corazon esta por delante del nudillo del indice es true 
        
        pulgar_apoyado = landmarks[4].x < landmarks[12].x and landmarks[4].y > landmarks[12].y  #El pulgar tiene que estar apoyado en el dedo corzon para que sea true 

        return indice_extendido and dedos_doblados and pulgar_apoyado and orientacion_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'E'
    def detectar_letra_E(landmarks):

        dedos_doblados = True #Si la punta del indie esta por encima de los nudillos es true 
        for i in [7, 11, 15, 19]: 
        # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser E
            if landmarks[i].y > landmarks[i-2].y or landmarks[i+1].y < landmarks[i].y: 
                dedos_doblados = False
                break
        
        pulgar_extendido = landmarks[4].x < landmarks[3].x and landmarks[4].y > landmarks[5].y #El pulgar tiene que estar estirado 
        orientaciom_correcta = landmarks[17].x > landmarks[0].x #La munieca tiene que estar por debajo de los dedos
        
        return dedos_doblados and pulgar_extendido and orientaciom_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
     # Función para detectar letra 'F'
    def detectar_letra_F(landmarks):

        orientacion_correcta = landmarks[1].y > landmarks[17].y # Si el nudillo del pulgar esta por debajo de los demas nudillos es true 
        dedos_rectos = True # Iniciamos la variable en true en dedos estirados 
        for i in [12, 16, 20]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser F
            if landmarks[i].y > landmarks[i-1].y:
                dedos_rectos = False
                break
        
        indice_doblado = landmarks[8].y > landmarks[5].y # Si el indice esta doblado por debajo del pulgar es true 
        pulgar_cerca = landmarks[4].x > landmarks[5].x # El pulgar tiene que estar por debajo del indice 

        return indice_doblado and pulgar_cerca and dedos_rectos and orientacion_correcta # Devuelve true si todo es true en caso de que uno se false es false

     # Función para detectar letra 'G'
    def detectar_letra_G(landmarks):

        orientacion_correcta = landmarks[9].y > landmarks[2].y # Si el pulgar esta apuntando hacia arriba es true  
        orientacion_correcta_2 = landmarks[1].y < landmarks[17].y # si el indice esta por debajo del pulgar es true 

        dedos_estirados = True #Iniciamos para los dedos esten estirados es true 
        for i in [8]:
             # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser G
            if landmarks[i].x > landmarks[i-1].x or landmarks[i-2].x > landmarks[i-3].x:
                dedos_estirados = False
                break

        dedos_doblados = True
        for i in [16, 20, 12]:
             # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser G
            if landmarks[i].x < landmarks[i-2].x:
                dedos_doblados = False
                break

        inclinacion_correcta = landmarks[16].x > landmarks[5].x # La mano tiene que estar torcida 

        return orientacion_correcta and dedos_doblados and dedos_estirados and inclinacion_correcta and orientacion_correcta_2 # Devuelve true si todo es true en caso de que uno se false es false
        
     # Función para detectar letra 'I'
    def detectar_letra_I(landmarks):

        dedos_doblados = True
        for i in [8, 12, 16]:  # Índice, medio, anular y meñique
             # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser I
            if landmarks[i].y < landmarks[i-3].y or landmarks[i-1].y < landmarks[i-2].y:  
                dedos_doblados = False
                break
        
        pulgar_cerca = landmarks[4].x > landmarks[5].x # El pulgar tiene que estar encojido
        dedo_estirado = landmarks[20].y < landmarks[19].y < landmarks[18].y < landmarks[17].y # el menyique tiene que estar estirado 
        
        return dedos_doblados and pulgar_cerca and dedo_estirado # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'K'
    def detectar_letra_K(landmarks):

        dedos_doblados = True #Iniciamos para los dedos esten doblados es true 
        for i in [16, 20]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser K
            if landmarks[i].y < landmarks[i-3].y:
                dedos_doblados = False

        orientacion_correcta = landmarks[18].x < landmarks[17].x and landmarks[17].y > landmarks[5].y #El dorso de la palma tiene que estar apuntando a la derecha
        medio_estirado = landmarks[12].x < landmarks[11].x and landmarks[12].y > landmarks[7].y #El dedo corazon tiene que estar estirado 
        indice_estirado = landmarks[8].y < landmarks[7].y and landmarks[8].x > landmarks[11].x #El dedo indice tiene que estar estirado
        pulgar_estirado = landmarks[4].y < landmarks[3].y and landmarks[4].x > landmarks[12].x and landmarks[4].y < landmarks[10].y # El pulgar tiene que estar entre el corazon y el indice 
        posicion_correcta = landmarks[4].x < landmarks[5].x and landmarks[4].x > landmarks[12].x #El pulgar tiene que estae en

        return dedos_doblados and orientacion_correcta and indice_estirado and pulgar_estirado and medio_estirado and posicion_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'L'
    def detectar_letra_L(landsmarks):

        dedos_doblados = True #Iniciamos para los dedos esten doblados es true 
        for i in [11, 15, 19]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser L
            if landsmarks[i].y < landsmarks[i-2].y:
                dedos_doblados = False
                break

        orientacion_correcta = landsmarks[17].x > landsmarks[13].x # Tenemos que ponerle la palma a la camara
        indice_estirado = landsmarks[8].y < landsmarks[7].y < landsmarks[6].y < landsmarks[5].y # el indice tiene que estar estirado 
        pulgar_estirado = landsmarks[2].x > landsmarks[3].x >landsmarks[4].x # el pulgar debe estar estirado 
        distancia_correcta = landsmarks[4].y > landsmarks[5].y # El pulgar tiene que estar por debajo del nudillo del indice

        return dedos_doblados and orientacion_correcta and indice_estirado and pulgar_estirado and distancia_correcta # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'M'
    def detectar_letra_M(landmarks):

        dedos_abajo = True # inicializmos que los dedos tienen que apuntar hacia abajo 

        for i in [8, 12, 16]:
             # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser M
            if landmarks[i].y < landmarks[i-1].y or landmarks[i-1].y < landmarks[i-2].y or landmarks[i-2].y < landmarks[i-3].y:
                dedos_abajo = False
                break
        
        posicion_dedos_estirados = landmarks[8].x < landmarks[12].x < landmarks[16].x # Los dedos indice, corazon y anular tienen que estirados 
        pulgar_doblado = landmarks[4].x > landmarks[5].x # El pulgar tiene que estar doblado
        menyique_doblado = landmarks[20].y < landmarks[15].y # El menyique tiene que estar doblado
        mano_abajo = landmarks[0].y < landmarks[2].y #La munyeca tiene que estar por arriba de los dedos 

        return dedos_abajo and posicion_dedos_estirados and pulgar_doblado and menyique_doblado and mano_abajo # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'N'
    def detectar_letra_N(landmarks):

        dedos_abajo = True

        for i in [8, 12]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser N
            if landmarks[i].y < landmarks[i-1].y or landmarks[i-1].y < landmarks[i-2].y or landmarks[i-2].y < landmarks[i-3].y:
                dedos_abajo = False
                break

        posicion_dedos_estirados = landmarks[8].x < landmarks[12].x # Los dedos indice y corazon tienen que estirados 
        pulgar_doblado = landmarks[4].x > landmarks[5].x # El pulgar tiene que estar doblado
        menyique_doblado = landmarks[20].y < landmarks[11].y # El menyique tiene que estar doblado
        anular_doblado = landmarks[16].y < landmarks[11].y # El anular tiene que estar doblado
        mano_abajo = landmarks[0].y < landmarks[2].y # La munyeca tiene que estar por arriba de los dedos 

        return posicion_dedos_estirados and pulgar_doblado and menyique_doblado and anular_doblado and mano_abajo # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'O'
    def detectar_letra_O(landmarks):

        dedos_estirados = True
        for i in [12, 16, 20]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser O
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break
        
        indice_doblado = landmarks[8].y > landmarks[6].y and landmarks[8].x < landmarks[5].x and landmarks[8].y > landmarks[5].y # El indice tiene que estar doblado 
        pulgar_correcto = landmarks[4].x < landmarks[1].x and landmarks[4].y > landmarks[6].y # El  pulgar tiene que hacer un circulo con el indice 
        indice_correcto = landmarks[8].x < landmarks[3].x # El indice tiene que hacer un circulo con el pulgar 

        return dedos_estirados and indice_correcto and indice_doblado and pulgar_correcto # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'P'
    def detectar_letra_P(landmarks):

        dedos_estirados = True # Los dedos estan estirados treu 
        for i in [8,12,16]:
            # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser O
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break

        pulgar_doblado = landmarks[4].x > landmarks[3].x and landmarks[4].x > landmarks[5].x # El pulgar tiene que estar doblado para ser true 
        menyique_doblado = landmarks[20].y > landmarks[19].y # El menyique tiene que estar doblado para ser true

        return dedos_estirados and pulgar_doblado and menyique_doblado # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'Q'
    def detectar_letra_Q(landmarks):

        dedos_estirados = True

        for i in [8, 12, 16, 20, 4]:
             # Si se cumple cualquiera de estas condiciones ya no cumplirá con los requisitos para ser Q
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break
       
        orientacion_correcta = landmarks[5].x > landmarks[9].x and landmarks[18].x < landmarks[2].x # Tienes que dar el dorsal de la mano para ser true 
        pulgar_correcto = landmarks[2].y < landmarks[5].y # El pulgar tiene que estar por debajo del nudillo del indice

        return dedos_estirados and orientacion_correcta and pulgar_correcto # Devuelve true si todo es true en caso de que uno se false es false

    # Función para detectar letra 'R'
    def detectar_letra_R(landmarks):
        
        dedos_estirados = True
        for i in [8,12]:
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break
        
        dedos_enlazados = landmarks[8].x > landmarks[12].x 
        menyique_doblado = landmarks[20].y > landmarks[19].y
        anular_doblado = landmarks[16].y > landmarks[15].y
        pulgar_doblado = landmarks[4].x > landmarks[3].x and landmarks[4].x > landmarks[5].x 
        
        return dedos_estirados and pulgar_doblado and menyique_doblado and anular_doblado and dedos_enlazados # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'S'
    def detectar_letra_S(landmarks):

        dedos_estirados = True
        for i in [12, 16, 20]:
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break
        
        indice_doblado = landmarks[8].y > landmarks[6].y and landmarks[8].x < landmarks[5].x and landmarks[8].y > landmarks[5].y
        pulgar_correcto = landmarks[4].x < landmarks[1].x and landmarks[4].y > landmarks[6].y
        indice_correcto = landmarks[8].x > landmarks[3].x 

        return dedos_estirados and indice_correcto and indice_doblado and pulgar_correcto # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'T'
    def detectar_letra_T(landmarks):
        dedos_estirados = True
        for i in [12, 16, 20]:
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break

        indice_doblado = landmarks[8].y > landmarks[6].y and landmarks[8].x < landmarks[3].x 
        pulgar_correcto = landmarks[4].y < landmarks[7].y
        
        return dedos_estirados and indice_doblado and pulgar_correcto # Devuelve true si todo es true en caso de que uno se false es false
    
    # Función para detectar letra 'U'
    def detectar_letra_U(landmarks):
        dedos_estirados = True
        for i in [8,12]:
            if landmarks[i].y > landmarks[i-1].y or landmarks[i-2].y > landmarks[i-3].y:
                dedos_estirados = False
                break
        
        menyique_doblado = landmarks[20].y > landmarks[19].y
        anular_doblado = landmarks[16].y > landmarks[15].y
        pulgar_doblado = landmarks[4].x > landmarks[3].x and landmarks[4].x > landmarks[5].x 

        
        
        return dedos_estirados and pulgar_doblado and menyique_doblado and anular_doblado # Devuelve true si todo es true en caso de que uno se false es false
    
