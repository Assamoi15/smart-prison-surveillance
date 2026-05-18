import streamlit as st
import cv2
import os
from ultralytics import YOLO
from PIL import Image
import tempfile

st.set_page_config(
    page_title="Surveillance Prison",
    page_icon="🚨",
    layout="wide"
)

st.title("🚨 Système de Surveillance Intelligent - Prison")

# Charger le modèle
@st.cache_resource
def load_model():
    model_path = "ai/models/best.pt"
    if not os.path.exists(model_path):
        st.warning("⚠️ Modèle non trouvé, utilisation de YOLO par défaut")
        model_path = "yolov8n.pt"
    return YOLO(model_path)

# Sidebar
with st.sidebar:
    st.header("⚙️ Configuration")
    confidence = st.slider("Seuil de confiance", 0.1, 0.9, 0.4)
    
    st.header("📊 Statistiques")
    if os.path.exists("alerts"):
        alerts = [f for f in os.listdir("alerts") if f.endswith(".jpg")]
        st.metric("🚨 Alertes générées", len(alerts))
    
    st.markdown("---")
    st.caption("Système basé sur YOLOv8")

# Upload d'image
st.subheader("📸 Détection sur image")
uploaded_image = st.file_uploader("Choisis une image CCTV", type=["jpg", "jpeg", "png"])

if uploaded_image:
    model = load_model()
    image = Image.open(uploaded_image)
    
    with st.spinner("Analyse en cours..."):
        results = model(image, conf=confidence)
        annotated = results[0].plot()
        
    col1, col2 = st.columns(2)
    with col1:
        st.image(image, caption="Image originale")
    with col2:
        st.image(annotated, caption="Détection")
    
    st.success(f"🔫 {len(results[0].boxes)} objet(s) détecté(s)")

# Upload de vidéo
st.subheader("🎬 Détection sur vidéo")
uploaded_video = st.file_uploader("Choisis une vidéo CCTV", type=["mp4", "avi", "mov"])

if uploaded_video:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as tmpfile:
        tmpfile.write(uploaded_video.read())
        video_path = tmpfile.name
    
    st.video(video_path)
    
    if st.button("🔍 Analyser la vidéo"):
        model = load_model()
        cap = cv2.VideoCapture(video_path)
        
        frame_count = 0
        weapons = 0
        
        progress = st.progress(0)
        status = st.empty()
        
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            if frame_count % 30 == 0:
                results = model(frame, conf=confidence)
                weapons += len(results[0].boxes)
            
            progress.progress(frame_count / total_frames)
            status.text(f"Frame {frame_count}/{total_frames}")
        
        cap.release()
        st.success(f"✅ Analyse terminée : {weapons} arme(s) détectée(s)")

st.markdown("---")
st.caption("🚨 Projet de surveillance par Intelligence Artificielle")
