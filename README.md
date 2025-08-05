# Event Syrup - SaaS LMS, Event Management & IoT Smart Attendance Platform

**Author:** Anup Chapagain  
**Type:** BSc (Hons) Dissertation | Full-Stack SaaS + IoT Project  
**Tech Stack:** React (Vite) / Node.js / Firebase / REST APIs / Python IoT

---

## 📖 Project Overview

**Event Syrup** is a **SaaS Learning Management and Event Hosting platform** enhanced with **IoT smart features**.  
It includes **two web panels** and **hardware IoT integration**:

1. **Admin Panel** – For event organizers and LMS managers  
2. **Client Panel** – For learners or event participants  
3. **IoT Integration** – Smart attendance and environmental monitoring using **RFID & sensors**

With Event Syrup, educational institutions, organizations, and event companies can:

- **Create and manage events, workshops, and online courses**  
- **Allow participants to register, attend, and track learning progress**  
- **Automatically log attendance via RFID IoT devices**  
- **Monitor real-time analytics and environmental conditions**  

This project demonstrates **modern SaaS architecture combined with IoT** for **next‑gen smart campus and event management**.

---

## ✨ Key Features

### **Admin Panel (Event Organizers)**

- **Dashboard with analytics** for events, users, and attendance  
- **Create and manage events, workshops, or lessons**  
- **User & Role Management** for instructors, students, and admins  
- **Attendance & Engagement Tracking** for each event  
- **Upload and manage LMS content** (lessons, files, or materials)

### **Client Panel (Learners / Attendees)**

- **Browse and register** for events or courses  
- **Access course content** with lessons and materials  
- **Automatic attendance tracking** during event participation  
- **Progress Monitoring** and certificate/completion tracking  
- **User Dashboard** showing enrolled events and course status  

### **🌐 IoT Integration**

Event Syrup also features **smart IoT modules**:

- **RFID Attendance** – Scan RFID cards to mark attendance automatically  
- **Temperature Monitoring** – Track environmental conditions for safety & analytics  
- **Smart Campus Ready** – IoT scripts run on **Raspberry Pi / Python** to connect sensors with the Event Syrup cloud backend

IoT scripts are stored in the **`iot/`** folder:

- `app.py` – Main IoT controller for attendance and sensors  
- `rfid_reader.py` – Handles RFID-based attendance  
- `temperature_sensor.py` – Reads event environment temperature

---

## 🛠 Tech Stack

- **Frontend:** React.js (Vite) for SPA dashboards (Admin & Client)  
- **Backend / API:** Node.js (Express) or Firebase Functions  
- **Database:** Firebase / MySQL / MongoDB for user and event data  
- **IoT Layer:** Python scripts for RFID & sensor integration  
- **Authentication:** Firebase Auth / JWT for multi-role access  
- **Hosting:** Firebase Hosting / Vercel / Heroku  
- **Other:** REST APIs for data exchange between panels & IoT

---

## 📂 Project Structure

```
EventSyrup/
 ├─ admin-panel/           # Admin dashboard (React + Vite)
 ├─ client-panel/          # Client / LMS user panel
 ├─ iot/                   # IoT scripts for smart attendance & monitoring
 │   ├─ app.py
 │   ├─ rfid_reader.py
 │   └─ temperature_sensor.py
 ├─ docs/                  # Reports & screenshots
 │   ├─ Project_Report.pdf
 │   └─ screenshots/
 ├─ README.md              # Project overview
 └─ .gitignore
```

---

## 🚀 Quick Start

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/anupanonymous/Event-Syrup-by-Anup-Chapagain.git
cd EventSyrup
```

### **2️⃣ Setup Admin Panel**

```bash
cd admin-panel
npm install
npm start
```

Visit `http://localhost:3000` for the **Admin Dashboard**.

### **3️⃣ Setup Client Panel**

```bash
cd ../client-panel
npm install
npm start
```

Visit `http://localhost:3001` for the **Client Panel**.

### **4️⃣ Run IoT Scripts (Optional)**

On a Raspberry Pi or system with connected RFID & sensors:

```bash
cd ../iot
python app.py
```

This will **log attendance via RFID** and **read environment data** into Event Syrup.

---

## 💡 Real-World Applications

- **Universities and Colleges:**  
  - Manage workshops, classes, and attendance with IoT-enabled automation  

- **Corporate Training Platforms:**  
  - Track employee participation and learning with automated attendance  

- **Public Event Management SaaS:**  
  - Run smart events with RFID entry & real-time dashboards  

- **Smart Campus / Hybrid LMS:**  
  - Integrate **IoT + SaaS LMS** for an intelligent, next‑gen learning environment

---

## 📸 Screenshots & Documentation

Screenshots and the dissertation report are available in the **`docs/`** folder:  
- `admin_dashboard.png` – Event and attendance dashboard  
- `client_dashboard.png` – Learner view of registered events and courses  
- `rfid_demo.png` – IoT RFID attendance logging

---

## 💡 Future Scope

- **AI-powered event recommendations**  
- **Real-time notifications via IoT triggers**  
- **Subscription-based SaaS deployment** for commercial use  
- **Mobile App Integration** for on-the-go learning & attendance  
- **Advanced IoT analytics** for environmental monitoring and event optimization

---

## 👤 About Me

**Anup Chapagain**  
AI, IoT & Fullstack Enthusiast | Film Making Aspirant | Camera Nerd

[![GitHub](https://img.shields.io/badge/GitHub-anupanonymous-black?style=for-the-badge&logo=github)](https://github.com/anupanonymous)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Anup%20Chapagain-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/)
