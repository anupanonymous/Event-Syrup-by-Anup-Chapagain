# Event Syrup - SaaS LMS & Event Management Platform

**Author:** Anup Chapagain  
**Type:** BSc (Hons) Dissertation | Full-Stack SaaS Project  
**Tech Stack:** React (Vite) / Node.js / Firebase / REST APIs *(based on your project stack)*

---

## 📖 Project Overview

**Event Syrup** is a **SaaS Learning Management and Event Hosting platform** with **two separate panels**:  

1. **Admin Panel** – For event organizers and LMS managers  
2. **Client Panel** – For learners or event participants  

This platform enables **educational institutions, organizations, and event companies** to:  
- Create and manage **events, workshops, and online courses**  
- Allow participants to **register, attend, and track their learning progress**  
- Monitor **attendance and engagement** with real-time dashboards  

Designed as a **multi-tenant SaaS application**, Event Syrup demonstrates **modern web app architecture** with **LMS + event hosting features**.

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

---

## 🛠 Tech Stack

- **Frontend:** React.js (Vite) for SPA dashboards (Admin & Client)  
- **Backend / API:** Node.js (Express) or Firebase Functions *(as per your project)*  
- **Database:** Firebase / MySQL / MongoDB for user and event data  
- **Authentication:** Firebase Auth / JWT for secure multi-role access  
- **Hosting:** Firebase Hosting / Vercel / Heroku (optional)  
- **Other:** REST APIs for data exchange between panels

---

## 📂 Project Structure

```
EventSyrup/
 ├─ admin-panel/           # Admin dashboard (React + Vite)
 │   ├─ src/               # Source code
 │   ├─ public/            # Static assets
 │   └─ package.json       
 │
 ├─ client-panel/          # Client / LMS user panel
 │   ├─ src/
 │   ├─ public/
 │   └─ package.json
 │
 ├─ docs/                  # Reports & screenshots
 │   ├─ Project_Report.pdf
 │   └─ screenshots/
 │
 ├─ README.md              # Project overview
 └─ .gitignore
```

---

## 🚀 Quick Start

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/anupanonymous/EventSyrup.git
cd EventSyrup
```

### **2️⃣ Setup Admin Panel**

```bash
cd admin-panel
npm install
npm start
```

Then visit `http://localhost:3000` to access the **Admin Dashboard**.

### **3️⃣ Setup Client Panel**

```bash
cd ../client-panel
npm install
npm start
```

Then visit `http://localhost:3001` to access the **Client Panel**.

---

## 💡 Real-World Applications

- **Universities and Colleges:**  
  Manage classes, workshops, and attendance with a central dashboard.  

- **Corporate Training Platforms:**  
  Run internal events, webinars, and track employee learning progress.  

- **Public Event Management SaaS:**  
  Allow organizers to create and track events while users register online.  

- **Hybrid LMS and Event Hosting:**  
  Combine **learning management + event hosting** for flexible education models.

---

## 📸 Screenshots & Documentation

Screenshots and the dissertation report are available in the **`docs/`** folder:  
- `admin_dashboard.png` – Event and attendance dashboard  
- `client_dashboard.png` – Learner view of registered events and courses  

---

## 💡 Future Scope

- **AI-powered event recommendations** for users  
- **Real-time notifications** via web and email  
- **Subscription-based SaaS deployment** for commercial use  
- **Mobile App Integration** for on-the-go event participation

---

## 👤 About Me

**Anup Chapagain**  
AI, IoT & Fullstack Enthusiast | Film Making Aspirant | Camera Nerd 

[![GitHub](https://img.shields.io/badge/GitHub-anupanonymous-black?style=for-the-badge&logo=github)](https://github.com/anupanonymous)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Anup%20Chapagain-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/)
