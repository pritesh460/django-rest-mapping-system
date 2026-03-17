# 🚀 Django REST Mapping API

A Django REST Framework project that implements CRUD APIs and relational mapping between **Vendor, Product, Course, and Certification** entities, along with **Swagger API documentation**.

---

## 📌 Project Overview

This project demonstrates how to build scalable REST APIs using Django REST Framework with proper relational database design and mapping tables.

It includes:

* CRUD operations for core entities
* Mapping relationships between models
* API testing using Swagger UI

---

## 🏗️ Tech Stack

* Python
* Django
* Django REST Framework
* drf-yasg (Swagger)

---

## 📂 Project Structure

```
core_project/
│
├── vendor/
├── product/
├── course/
├── certification/
│
├── vendor_product_mapping/
├── product_course_mapping/
├── course_certification_mapping/
│
└── core_project/
```

---

## 🔗 API Endpoints

### 🔹 Vendor ↔ Product

```
/api/vendor-product/
```

### 🔹 Product ↔ Course

```
/api/product-course/
```

### 🔹 Course ↔ Certification

```
/api/course-certification/
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

```
git clone https://github.com/pritesh460/django-rest-mapping-system.git
cd django-rest-mapping-system
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

OR manually:

```
pip install django djangorestframework drf-yasg
```

---

### 3️⃣ Apply Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

### 4️⃣ Run Server

```
python manage.py runserver
```

---

## 🌐 Access Project

* Home: http://127.0.0.1:8000/
* Swagger UI: http://127.0.0.1:8000/swagger/
* Admin Panel: http://127.0.0.1:8000/admin/

---

## 📊 Features

* ✅ Full CRUD APIs
* ✅ Relational Mapping (Foreign Keys)
* ✅ Swagger Documentation
* ✅ Clean API Structure
* ✅ Admin Panel Integration

---

## 🔄 API Operations

Each endpoint supports:

* GET → Retrieve data
* POST → Create data
* PUT → Update data
* DELETE → Remove data

---

## 🧪 Testing

All APIs can be tested using:

* Swagger UI (Recommended)
* Browser
* Postman

---

## 🎯 Learning Outcome

* Understanding Django REST Framework
* Building scalable APIs
* Working with relational databases
* API documentation using Swagger

---

## 👨‍💻 Author

**Pritesh Kalsariya**

---

## 📌 Conclusion

This project successfully demonstrates a complete REST API system with relational mappings and proper documentation, making it suitable for internship-level backend development tasks.

---
