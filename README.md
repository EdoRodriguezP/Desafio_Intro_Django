# Desafio_Intro_Django
Desafio Introducción a Django desafio Latam

# 🧪 Desafío - Introducción a Django

En este desafío validaremos nuestros conocimientos de Introducción a Django. Para lograrlo, necesitarás aplicar lo aprendido hasta el momento, utilizando de apoyo el archivo **Apoyo Desafío - Introducción a Django**.

**⏳ Tiempo asociado:** 2 horas cronológicas.

---

## 📘 Descripción

Un cliente nos solicita una aplicación web que incluya las siguientes vistas:

- Home (`/`)
- About (`/about/`)
- Contact (`/contact/`)

Para ello, la solución será entregarle un ejemplo funcional utilizando Django. Los contenidos de las vistas pueden ser textos de prueba usando **Lorem Ipsum**.

En el caso de la vista **Contact**, se sugiere implementar un mini formulario de contacto usando HTML.

---

## 🔗 URLs sugeridas

```python
from desafioGiado.views import home, about, contact

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('contact/', contact),
]
```

---

## ⚙️ Instalación de dependencias

En el material de apoyo se encuentra el archivo `requirements.txt`, el cual contiene Django y su versión requerida.

### Pasos para instalar las dependencias:

1. Abre una terminal.
2. Navega hasta la raíz del proyecto Django dentro del entorno virtual.
3. Ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```

> 🔑 Recuerda activar el entorno virtual antes de cualquier instalación.

---

## ✅ Requerimientos del desafío

| # | Requerimiento | Puntaje |
|---|----------------|---------|
| 1 | Crear un entorno virtual de Python y ejecutar las instalaciones del archivo `requirements.txt`. | 2 puntos |
| 2 | Crear la vista **Home** de la aplicación. | 2 puntos |
| 3 | Crear la vista **About** de la aplicación. | 2 puntos |
| 4 | Crear la vista **Contact** con un mini formulario de contacto. | 2 puntos |
| 5 | Generar los templates HTML para cada una de las vistas solicitadas. | 2 puntos |

---

## 🧠 Tips importantes

- Para retornar documentos HTML, se debe utilizar el método `render` desde Django:

```python
from django.shortcuts import render
```

- Recuerda modificar el archivo `settings.py` para indicar el directorio de templates (por convención, llamado `templates`).

---

## 🎨 Recomendación de estilo

Si deseas estilizar los templates, puedes usar **Bootstrap** en cada documento HTML.

---
