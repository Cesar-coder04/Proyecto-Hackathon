
# Spanish Sign Language Translator

A real-time Spanish Sign Language (LSE) alphabet translator developed in Python using computer vision. The application detects hand gestures through a webcam and converts recognized letters into text.

This project was developed during **CIBERGU 2024**, a technology and cybersecurity event in Guadalajara, Spain.

## 🏆 Award and Recognition

**1st Prize — CIBERGU 2024 Hackathon (€2,000)**

Our team, **Bug Buster**, won first place in the CIBERGU 2024 Hackathon. The team was led by César Nicolás and included Pablo Menéndez, Daniel Monje, and David Vargas.

The event was organized with the involvement of the **National Cybersecurity Institute of Spain (INCIBE)** and **CEEI Guadalajara**.

📰 **Press coverage:** [CIBERGU 2024 closes its first edition successfully — Nueva Alcarria](https://nuevaalcarria.com/articulos/el-cibergu-2024-cierra-con-exito-su-primera-edicion)

## ✨ Features

- **Real-time camera input:** Captures hand gestures using a webcam.
- **Hand detection:** Detects hands and their landmarks using MediaPipe.
- **Gesture recognition:** Processes hand positions to identify alphabet letters.
- **Text conversion:** Converts recognized gestures into text.
- **Graphical user interface:** Provides a desktop interface built with PySide6.
- **Computer vision:** Uses OpenCV to handle camera input and image processing.

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| MediaPipe | Hand detection and landmark tracking |
| OpenCV (`cv2`) | Camera access and image processing |
| PySide6 | Graphical user interface |

## ⚙️ How It Works

1. The application captures video from the webcam.
2. MediaPipe detects the user's hand and identifies relevant landmarks.
3. The hand position is processed by the gesture recognition logic.
4. The application identifies a supported sign language letter.
5. The recognized letter is converted into text and displayed in the interface.

## 👨‍💻 My Contribution

During the hackathon, I was responsible for developing the **hand gesture detection and recognition logic**.

My work focused on processing hand positions and identifying the gestures required to translate supported Spanish Sign Language alphabet signs into text.

## 🚀 Getting Started

### Prerequisites

- Python installed on your computer.
- A webcam.
- The project source code.

### Installation

1. Clone the repository:

   ```bash
   git clone <YOUR_REPOSITORY_URL>
   ```

2. Navigate to the project directory:

   ```bash
   cd <YOUR_PROJECT_FOLDER>
   ```

3. Create and activate a virtual environment (recommended):

   **Windows**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **Linux / macOS**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install the dependencies:

   If the repository includes a `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

   Otherwise, install the dependencies listed in the project source code.

5. Run the application's main Python script:

   ```bash
   python <MAIN_SCRIPT>.py
   ```

   Replace `<MAIN_SCRIPT>.py` with the actual entry-point filename.

## ⚠️ Current Limitations

- The current prototype supports alphabet recognition rather than complete word or sentence translation.
- Recognition accuracy may depend on lighting conditions, camera quality, and hand visibility.
- The application is a prototype developed during a time-limited hackathon.

## 🔮 Potential Improvements

Possible future improvements include:

- Expanding recognition to cover complete words and sentences.
- Improving recognition accuracy across different lighting conditions and hand positions.
- Adding support for continuous text composition.
- Improving the user interface and providing clearer recognition feedback.

These are potential extensions and are not necessarily implemented in the current version.

## 📄 License

No license has been specified yet. Please contact the repository owner for permission to reuse or distribute this project.

