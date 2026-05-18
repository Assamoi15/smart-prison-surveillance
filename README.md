# 🚨 Smart Prison Surveillance System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![YOLO](https://img.shields.io/badge/YOLO-v8-red)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28-ff4b4b)
![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Présentation

Système de surveillance intelligent pour établissements pénitentiaires utilisant la **vision par ordinateur** pour détecter automatiquement :

| Fonctionnalité | Statut |
|----------------|--------|
| 🔪 Détection d'armes (couteaux/pistolets) | ✅ Implémenté |
| 🚶 Détection d'intrusions en zone interdite | ✅ Implémenté |
| 📸 Alertes visuelles avec captures | ✅ Implémenté |
| 📊 Dashboard interactif | ✅ Implémenté |
| 🎬 Analyse vidéo avec annotations | ✅ Implémenté |

## 🛠️ Stack technique

| Catégorie | Technologies |
|-----------|--------------|
| **IA & CV** | YOLOv8, PyTorch, OpenCV |
| **Backend** | Python, FastAPI |
| **Frontend** | Streamlit, Gradio |
| **Entraînement** | Google Colab (GPU Tesla T4) |

## 📊 Résultats obtenus

### Détections d'armes
| Frame | Objet | Confiance |
|-------|-------|-----------|
| 22 | Couteau | 87% |
| 59 | Couteau | 82% |
| 180 | Couteau | 91% |
| 184-186 | Couteau | 85-89% |

### Détections d'intrusion
| Frames | Événement |
|--------|-----------|
| 41-42 | Intrusion zone interdite |
| 65-66 | Intrusion zone interdite |
| 660-669 | Intrusion zone interdite |

## 🚀 Installation rapide

```bash
# Cloner le projet
git clone https://github.com/Assamoi15/smart-prison-surveillance.git
cd smart-prison-surveillance

# Installer les dépendances
pip install -r requirements.txt

# Lancer le dashboard
streamlit run frontend/dashboard.py

📁 Structure du projet

smart-prison-surveillance/
├── frontend/
│   ├── dashboard.py      # Dashboard Streamlit
│   └── gradio_app.py     # Interface Gradio
├── backend/
│   └── api.py            # API FastAPI
├── ai/
│   ├── models/           # Modèles entraînés
│   └── datasets/         # Dataset YOLO
├── alerts/               # Captures d'alertes
├── videos/               # Vidéos annotées
├── requirements.txt
└── README.md

🔄 Améliorations futures

Détection de bagarres (CNN + LSTM)

Tracking des détenus (DeepSORT)

Alertes temps réel (Telegram)

Dashboard React

👤 Auteur
Assamoi15

GitHub : @Assamoi15
