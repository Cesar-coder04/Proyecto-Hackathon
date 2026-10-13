import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions

# Especificar la configuración del clasificador
options = vision.ImageClassifierOptions(
    base_options = BaseOptions(model_asset_path="/path/efficientnet_lite_int8.tflite"),
    max_results=5,
    score_threshold=0.01,
    running_mode=vision.RunningMode.IMAGE)
classifier = vision.ImageClassifier.create_from_options(options)

# Leer la imagen de entrada
image = cv2.imread("ManoIzquierda.jpg")
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_rgb = mp.Image(image_format=mp.ImageFormat.SRGB, data=image_rgb)

# Obtener los resultados del clasificador
classifier_result = classifier.classify(image_rgb)
print(classifier_result.classifications)
y_aux = 0
for classification in classifier_result.classifications:
    for category in classification.categories:
        print(category)
        cv2.rectangle(image, (90, 0), (560,100), (255,255,255), -1)
        cv2.putText(image, 
                    f"{category.category_name}: {category.score * 100:.2f}%",
                    (95, 80 + y_aux),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    2.1,
                    (214, 88, 107),
                    5)
        y_aux += 40

cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()