# 🚨 Smart Prison Surveillance System

![Status](https://img.shields.io/badge/status-en%20cours-yellow)

![Python](https://img.shields.io/badge/Python-3.10-blue)

![YOLO](https://img.shields.io/badge/YOLO-v8-red)

![License](https://img.shields.io/badge/License-MIT-green)

## 📌 Présentation

Système de surveillance intelligent pour établissements pénitentiaires utilisant la **vision par ordinateur** pour détecter automatiquement :

- 🔪 **Armes blanches** (couteaux)
  
- 🔫 **Armes à feu** (pistolets)
  
- 🚶 **Intrusions** en zones interdites
  
- 📸 **Alertes visuelles** avec captures d'écran

## 🎯 Problématique

Les prisons manquent de systèmes automatisés pour détecter rapidement :

- L'introduction d'armes
  
- Les intrusions dans les zones sensibles
  
- Les comportements suspects

**Solution** : Un système IA qui analyse les flux vidéo en temps réel et déclenche des alertes automatiques.

---

## 🛠️ Stack technique

| Catégorie | Technologies |
|-----------|--------------|
| **IA & Computer Vision** | YOLOv8, PyTorch, OpenCV |

| **Backend** | Python, FastAPI |

| **Frontend** | Streamlit, Gradio |

| **Entraînement** | Google Colab (GPU Tesla T4) |

| **Versionnement** | Git, GitHub |

---

## 📊 Résultats obtenus

### Détection d'armes

| Frame | Objet détecté | Confiance |
|-------|---------------|-----------|
| 22 | Couteau | 87% |
| 59 | Couteau | 82% |
| 180 | Couteau | 91% |
| 184-186 | Couteau | 85-89% |

### Détection d'intrusion

| Frames | Événement |
|--------|-----------|
| 41-42 | Intrusion en zone interdite |
| 65-66 | Intrusion en zone interdite |
| 660-669 | Intrusion en zone interdite |
| 678 | Intrusion en zone interdite |

### Métriques globales

| Métrique | Valeur |
|----------|--------|
| Précision détection | >85% |
| Temps d'inférence | ~42ms/frame |
| Dataset | 141 images annotées |
| Frames analysées | 987 par vidéo |

---

## 🚀 Installation et utilisation

### Prérequis

```bash
Python 3.10+
pip install -r requirements.txt
