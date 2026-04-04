# A.R.A.N.Y.A
## Autonomous Real-time Analytics for Natural Yield & Area Protection

<div align="center">

![ARANYA Banner](https://img.shields.io/badge/A.R.A.N.Y.A-Environmental_AI_Platform-2d6a4f?style=for-the-badge&logo=leaf&logoColor=white)

**Real-Time Environmental Compliance Intelligence for India**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg?style=flat-square&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-ML_Core-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![Sentinel-2](https://img.shields.io/badge/Sentinel--2-Satellite_Data-0A9EDC?style=flat-square&logo=satellite&logoColor=white)](https://sentinel.esa.int/)
[![GeoAI](https://img.shields.io/badge/GeoAI-Geospatial_Intelligence-52b788?style=flat-square)](https://github.com/)
[![Contributions Welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat-square)](CONTRIBUTING.md)

*A real-time AI-powered environmental compliance monitoring system that detects illegal mining and land degradation using streaming satellite data, geospatial deep learning, and automated regulatory reasoning — built for the Aravalli Range.*

[Overview](#-overview) • [Features](#-features) • [Architecture](#-system-architecture) • [Tech Stack](#-technology-stack) • [Data Sources](#-data-sources) • [Modules](#-modules) • [Roadmap](#-roadmap) • [Team](#-meet-the-team)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
  - [Mission](#-mission)
  - [Why ARANYA?](#-why-aranya)
- [Features](#-features)
  - [Streaming Data Ingestion](#-streaming-data-ingestion)
  - [Geospatial AI Core](#-geospatial-ai-core)
  - [Compliance Intelligence Layer](#-compliance-intelligence-layer)
  - [Dashboard & Alerting](#-dashboard--alerting)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Data Sources](#-data-sources)
- [Modules](#-modules)
- [Feasibility & Risk Assessment](#-feasibility--risk-assessment)
- [Expansion Potential](#-expansion-potential)
- [Contributing](#-contributing)
- [Roadmap](#-roadmap)
- [License](#-license)
- [Meet the Team](#-meet-the-team)

---

## 🌟 Overview

**A.R.A.N.Y.A** (अरण्य = Forest/Wilderness in Sanskrit) is a cutting-edge, real-time AI-powered environmental compliance monitoring system designed to detect illegal mining and land degradation in ecologically sensitive zones. Focused initially on the **Aravalli Range (Haryana–Rajasthan belt)**, the system ingests streaming satellite imagery, applies geospatial deep learning models, and generates automated, policy-linked alerts for regulatory enforcement.

This is not a simple image classification tool. ARANYA is a **governance-aligned environmental intelligence infrastructure** — built to bridge the critical gap between satellite observation and on-ground enforcement.

### 🎯 Mission

To build a scalable, real-time environmental AI platform that:
- **Detects illegal mining and deforestation** continuously and autonomously
- **Links environmental violations to specific regulatory provisions** for enforcement
- **Reduces dependence on manual inspection** with streaming, automated analysis
- **Protects India's most critical ecological zones** starting with the Aravalli Range
- **Evolves into a national-scale** environmental intelligence network

### ✨ Why ARANYA?

The Aravalli Range faces a dire reality:
- 🏔️ One of the **oldest fold mountains in the world**, under severe threat
- 🌵 Acts as a **natural barrier against Thar desert expansion**
- 💧 A **critical groundwater recharge zone** for millions
- 🐾 A **biodiversity hotspot** with irreplaceable flora and fauna

Despite Supreme Court bans and multiple regulatory frameworks (EPA 1986, Forest Conservation Act 1980, NGT directives), **illegal mining continues** because:

| Problem | Impact |
|--------|--------|
| Weak monitoring | Violations go undetected for months |
| Manual inspection dependence | Slow, expensive, prone to corruption |
| Delayed satellite reviews | Retrospective analysis — too late to act |
| Complaint-based enforcement | Reactive, not proactive |

**There is no integrated, real-time AI-based enforcement layer. ARANYA is that layer.**

---

## 🚀 Features

### 🛰️ Streaming Data Ingestion

ARANYA treats satellite imagery as a continuous data stream — not a static dataset.

- **Sentinel-2 Integration**: Ingests 10m resolution multispectral imagery from ESA Copernicus
- **Cloud Masking**: Automated cloud detection and masking for reliable imagery
- **Tile Extraction**: Region-of-interest tiling for focused, efficient processing
- **Spectral Index Computation**: Real-time NDVI (vegetation) and NDBI (built-up) index generation
- **Geospatial Overlays**: Protected zone shapefiles, administrative boundaries, and mining lease data
- **Simulated Drone Feeds**: Optional integration of drone-based high-resolution verification streams
- **Weather Stream Integration**: Rainfall and wind data from IMD/OpenWeather APIs for contextual correlation

### 🧠 Geospatial AI Core

The intelligence engine powering ARANYA's detection capabilities.

**Land Cover Segmentation**
- Deep learning segmentation using **DeepLabv3+** and **U-Net** architectures
- Classifies terrain into: vegetation, barren land, water, built-up, and mining scars
- Multispectral input (SWIR, NIR, RGB bands) for superior accuracy vs. RGB-only models
- Pretrained model fine-tuned for Indian geological and spectral context
- Reported accuracy: 85–95% on mining detection benchmarks

**NDVI Anomaly Detection**
- Computes vegetation indices per tile per timestep
- Detects sudden vegetation degradation events
- Distinguishes gradual seasonal change from abrupt anthropogenic destruction
- Threshold-adaptive alerts based on baseline vegetation profiles

**Bi-Temporal Change Detection**
- Compares satellite imagery between time T1 and T2
- Generates pixel-level change masks highlighting excavation expansion
- Architectures evaluated: Siamese CNN, UNet++, BIT-CD (Transformer-based)
- Detects quarry growth, topsoil removal, and slope modification

**Risk Scoring Model**
```
Risk Score (0–100) = f(
    vegetation_loss_percentage,
    excavation_growth_rate,
    proximity_to_protected_zone,
    historical_violation_pattern,
    rainfall_correlation_coefficient
)
```
- Composite multi-factor score combining spatial, temporal, and contextual signals
- Configurable thresholds for alert triggering
- Risk tier classification: Low / Medium / High / Critical

### ⚖️ Compliance Intelligence Layer

What makes ARANYA unique: **detection alone is not enough**. ARANYA converts detections into governance intelligence.

When Risk Score exceeds threshold:
1. **Alert Triggered** → Event logged with GPS coordinates, timestamp, severity
2. **Policy Retrieval** → Relevant legal provisions pulled from regulatory document database
3. **Explanation Generated** → Human-readable violation summary for regulatory action

**Example output:**
> *"Detected 12% vegetation loss within Eco-Sensitive Zone II near Rajawas Village, Haryana. Potential violation under Section 2 of the Forest Conservation Act, 1980 and NGT Order [2018]. Recommended action: Initiate ground inspection within 72 hours."*

**Legal Frameworks Covered:**
- Supreme Court bans on Aravalli mining (multiple orders)
- Environment Protection Act, 1986
- Forest Conservation Act, 1980
- National Green Tribunal (NGT) directives
- Haryana and Rajasthan State Mining Policies

### 📊 Dashboard & Alerting

A real-time monitoring interface for regulators, researchers, and enforcement agencies.

- **Interactive Map** (Leaflet / Mapbox): Live overlay of risk zones and violation alerts
- **Risk Heatmap**: Color-coded severity visualization across the monitored region
- **Time-Series Charts**: Vegetation index trends, change detection history, alert frequency
- **Alert Logs**: Timestamped, geo-referenced violation records with evidence snapshots
- **Policy Panel**: Inline display of applicable legal provisions per alert
- **Export Reports**: Generate compliance and incident reports for regulatory submission

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                   LAYER 1: DATA INGESTION                       │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  Streaming Satellite & Geospatial Data                   │   │
│  │  ├── Sentinel-2 Imagery (10m, multispectral)             │   │
│  │  ├── Protected Zone Shapefiles                           │   │
│  │  ├── Weather API (IMD / OpenWeather)                     │   │
│  │  ├── Administrative Boundaries                           │   │
│  │  └── Optional: Simulated Drone Feeds                     │   │
│  └──────────────────────────────────────────────────────────┘   │
│              Cloud Masking → Tile Extraction → Index Compute    │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                LAYER 2: GEOSPATIAL AI CORE                      │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ├── Land Cover Segmentation (DeepLabv3+ / U-Net)        │   │
│  │  ├── NDVI Anomaly Detection                              │   │
│  │  ├── Bi-Temporal Change Detection (Siamese CNN / BIT-CD) │   │
│  │  └── Risk Scoring Engine (Multi-Factor Composite)        │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│             LAYER 3: COMPLIANCE INTELLIGENCE LAYER              │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ├── Threshold-Based Alert Triggering                    │   │
│  │  ├── Regulatory Document Database (RAG)                  │   │
│  │  ├── Policy-Linked Explanation Generator                 │   │
│  │  └── Violation Log & Evidence Archival                   │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                               ↓
┌─────────────────────────────────────────────────────────────────┐
│                  LAYER 4: DASHBOARD & ALERTS                    │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  ├── Real-Time Map (Leaflet / Mapbox)                    │   │
│  │  ├── Risk Heatmap & Alert Overlays                       │   │
│  │  ├── Time-Series Vegetation Charts                       │   │
│  │  ├── Policy Reference Panel                              │   │
│  │  └── Exportable Compliance Reports                       │   │
│  └──────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Geospatial Processing** | Python, Rasterio, GDAL, GeoPandas, Google Earth Engine API |
| **Machine Learning** | PyTorch / TensorFlow, DeepLabv3+, U-Net, Siamese CNN, BIT-CD |
| **Spectral Analysis** | Scikit-learn, NumPy, SciPy |
| **Backend** | Event-driven streaming architecture, real-time database |
| **Frontend** | Leaflet / Mapbox, Chart.js, React |
| **Data Storage** | PostgreSQL, vector store for policy documents |
| **Cloud & Infra** | AWS (SageMaker, S3, EKS), Docker |
| **Foundation Models** | Prithvi (ISRO + Microsoft), SatMAE, Swin Transformer for RS |

---

## 📡 Data Sources

**Satellite Imagery**
- [Sentinel-2 — ESA Copernicus Open Access Hub](https://scihub.copernicus.eu/) (10m resolution, free)
- [Google Earth Engine](https://earthengine.google.com/) (preprocessing & historical access)
- [ISRO Bhuvan Portal](https://bhuvan.nrsc.gov.in/)

**Geospatial Layers**
- Forest and protected area boundary shapefiles (MoEFCC / FSI)
- Mining lease data (State Geology Departments)
- Administrative district boundaries (Survey of India)

**Weather Data**
- [IMD API](https://mausam.imd.gov.in/) (India Meteorological Department)
- [OpenWeather API](https://openweathermap.org/api)

**Regulatory Documents**
- Supreme Court orders on Aravalli mining
- Environment Protection Act and Forest Conservation Act provisions
- NGT directives database

---

## 🔬 Modules

### 1. Data Ingestion Pipeline
Handles streaming and batch ingestion of satellite imagery, applies cloud masking, extracts tiles for the Aravalli region of interest, and computes spectral indices (NDVI, NDBI, SWIR).

### 2. Segmentation Module
Runs pretrained DeepLabv3+ / U-Net on multispectral tiles to classify land cover: vegetation, barren, built-up, water, and mining scars. Outputs pixel-level classification maps per timestep.

### 3. Change Detection Module
Compares T1 and T2 imagery using bi-temporal deep learning (Siamese CNN or BIT-CD Transformer). Generates change masks highlighting excavation growth and vegetation loss.

### 4. Risk Scoring Engine
Aggregates outputs from segmentation and change detection with geospatial proximity data and weather correlation to produce a composite Risk Score (0–100) per geographic tile.

### 5. Compliance Intelligence Engine
When risk threshold is exceeded, retrieves relevant legal provisions from the policy document database and generates a human-readable violation explanation for regulatory use.

### 6. Alerting & Dashboard
Pushes alerts to a real-time dashboard with interactive maps, heatmaps, time-series charts, and exportable reports.

---

## ⚖️ Feasibility & Risk Assessment

| Risk | Mitigation |
|------|-----------|
| Sentinel-2 revisit time (~5 days) | Simulate streaming for demo; multi-satellite fusion in future |
| Cloud cover interference | Automated cloud masking pipeline |
| False positives (erosion vs. mining) | Multi-factor scoring: shape + texture + spectral + historical |
| Heavy model training requirements | Use pretrained geospatial foundation models (Prithvi, SatMAE) |

**Strengths:**
- Satellite data is freely available (Copernicus, Bhuvan)
- Proven CNN segmentation architectures with 85–95% accuracy
- Strong regulatory alignment — directly maps to existing Indian law
- High-impact, urgent real-world use case with government relevance

---

## 🌱 Expansion Potential

ARANYA is designed as an extensible environmental intelligence platform. Future modules include:

**Deforestation Monitoring** — Detect illegal tree clearing in forest reserves across India

**Landslide Risk Prediction** — Combine rainfall streams, vegetation loss, and terrain slope to predict landslide probability in mining-affected areas

**Desertification Tracking** — Monitor Thar Desert expansion driven by Aravalli degradation

**Carbon Loss Estimation** — Quantify carbon stock reduction from vegetation loss; generate ESG compliance reports

**Autonomous Drone Verification**
```
1. Satellite flags high-risk zone
2. Drone auto-deployed for ground verification
3. High-resolution evidence captured
4. Evidence archived for legal proceedings
```

**National Environmental AI Network** — Scale to cover all ecologically sensitive zones across India, integrating with Ministry of Environment, State Forest Departments, and NGT support systems.

---

## 🗺️ Strategic Positioning

> This is not a "mining detection system."
>
> **ARANYA is Real-Time Environmental Compliance Intelligence Infrastructure for India.**

Demo region: Aravalli Range.
Vision: National-scale deployment across all Protected Areas, Eco-Sensitive Zones, and scheduled forests.

---

## 📄 License

This project is licensed under the MIT License. See [`LICENSE`](LICENSE) for details.

---

## 🙏 Acknowledgments

- **ESA Copernicus Programme** for open access Sentinel-2 data
- **ISRO** for Bhuvan geospatial portal and Prithvi foundation model collaboration
- **Google Earth Engine** for accessible satellite preprocessing infrastructure
- Research community behind BiT-CD, SatMAE, and geospatial Vision Transformers
- Citizens of the Aravalli region whose documented reports continue to expose illegal mining activity

---

<div align="center">

*"The forest does not record its own destruction. ARANYA does."*

**A.R.A.N.Y.A — Protecting India's Green Heritage, One Pixel at a Time.**

</div>
