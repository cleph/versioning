# راهنمای پروژه Version

این پروژه یک API بر پایه Django REST Framework است که با استفاده از آن می‌توانید عملیات CRUD (ایجاد، خواندن، به‌روزرسانی و حذف) را بر روی مدل‌های مختلف انجام دهید. این پروژه همچنین از `django-cors-headers` برای مدیریت CORS و `drf-spectacular` برای تولید مستندات OpenAPI استفاده می‌کند.

## فهرست مطالب

- [پیش‌نیازها](#پیش‌نیازها)
- [نصب و راه‌اندازی](#نصب-و-راه‌اندازی)
- [ساختار پروژه](#ساختار-پروژه)
- [پیکربندی تنظیمات](#پیکربندی-تنظیمات)
- [اجرای مهاجرت‌ها](#اجرای-مهاجرت‌ها)
- [اجرای سرور توسعه](#اجرای-سرور-توسعه)
- [استفاده از API](#استفاده-از-api)
- [محدودیت‌ها و قوانین](#محدودیت‌ها-و-قوانین)
- [مستندات API](#مستندات-api)
- [نویسنده](#نویسنده)
- [مجوز](#مجوز)

## پیش‌نیازها

- Python 3.8 یا بالاتر
- pip یا pipenv برای مدیریت بسته‌ها
- یک محیط مجازی (توصیه می‌شود)

## نصب و راه‌اندازی

### 1. کلون کردن مخزن

ابتدا مخزن را کلون کنید:

```bash
git clone https://github.com/username/version.git
cd version
```
2. ایجاد محیط مجازی
از محیط مجازی برای جداسازی بسته‌های پروژه استفاده کنید:

```
python -m venv env
source env/bin/activate 
 # برای ویندوز: 
 env\Scripts\activate
```
3. نصب وابستگی‌ها
تمامی بسته‌های موردنیاز را نصب کنید:

```
pip install -r requirements.txt
```
نکته: در صورتی که فایل requirements.txt وجود ندارد، می‌توانید بسته‌های زیر را نصب کنید:

```
pip install django djangorestframework drf-spectacular django-cors-headers
```
ساختار پروژه
```
versioning/
├── core/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── manage.py
│
├── version/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
```
در این پروژه، هم نام پروژه و هم نام اپلیکیشن versioning است.

پیکربندی تنظیمات
در فایل version/settings.py تغییرات زیر اعمال شده است:

افزودن برنامه‌های موردنیاز به INSTALLED_APPS:


```INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'drf_spectacular',
    'version',  # اپلیکیشن ما
]
```
افزودن CORS به MIDDLEWARE:

```
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]
```
تنظیمات CORS:

```
CORS_ALLOW_ALL_ORIGINS = True  # فقط برای محیط توسعه
```
تنظیمات REST Framework و drf-spectacular:

```
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '100/day',  # محدودیت 100 درخواست در روز برای هر کاربر
    },
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Version API',
    'DESCRIPTION': 'API documentation for the Version project',
    'VERSION': '1.0.0',
}
```
اجرای مهاجرت‌ها
برای ایجاد جداول پایگاه داده، دستورات زیر را اجرا کنید:

```
python manage.py makemigrations
python manage.py migrate
```
اجرای سرور توسعه
برای اجرای سرور توسعه، دستور زیر را اجرا کنید:

```
python manage.py runserver
```
سرور بر روی آدرس http://127.0.0.1:8000/ در دسترس خواهد بود.

استفاده از API
مسیرهای API
تمامی مسیرهای API در زیر مسیر versioning/ قرار دارند. فایل version/urls.py به شکل زیر تنظیم شده است:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('versioning/', include('version.urls')),  # اضافه کردن مسیر API
]
```
مدل‌ها
API شامل مدل‌های زیر است:

Platform: پلتفرم‌هایی با وضعیت‌ها و نسخه‌های مختلف
Patch: وصله‌هایی که می‌توان بر روی پلتفرم‌ها اعمال کرد
Test: تست‌هایی که برای پلتفرم‌ها انجام می‌شود
Bug: باگ‌هایی که در پلتفرم‌ها گزارش می‌شود
عملیات CRUD
برای هر مدل، عملیات زیر در دسترس است:

ایجاد (Create): ارسال درخواست POST به مسیر مربوطه
خواندن (Retrieve/List): ارسال درخواست GET به مسیر یا جزئیات
به‌روزرسانی (Update): ارسال درخواست PUT/PATCH به مسیر جزئیات
حذف (Delete): ارسال درخواست DELETE به مسیر جزئیات
مثال‌ها
لیست تمام پلتفرم‌ها:

```
GET http://127.0.0.1:8000/versioning/platforms/
```
ایجاد یک پلتفرم جدید:
```
POST http://127.0.0.1:8000/versioning/platforms/
Content-Type: application/json

{
    "title": "My Platform",
    "url": "http://example.com",
    "status": "Alpha",
    "version": 1
}
```
محدودیت‌ها و قوانین
با توجه به قوانین کسب‌وکار، محدودیت‌های زیر اعمال می‌شود:

Platform:

اگر وضعیت پلتفرم تغییر کند، یک پلتفرم جدید حتی با همان نام ایجاد می‌شود.
هنگام ایجاد پلتفرم جدید، id پلتفرم جدید برگردانده می‌شود.
Patch:

در وضعیت‌های PreAlpha, Alpha, Beta, Gamma, RC, Rolling می‌توان Patch ایجاد کرد.
در وضعیت Stable امکان ایجاد Patch وجود ندارد.
Test:

در وضعیت‌های PreAlpha, Alpha, Beta, Gamma, RC می‌توان Test ایجاد کرد.
در وضعیت‌های Rolling, Stable امکان ایجاد Test وجود ندارد.
Bug:

در وضعیت‌های PreAlpha, Alpha, Beta می‌توان Bug گزارش کرد.
در وضعیت‌های Gamma, RC, Rolling, Stable امکان گزارش Bug وجود ندارد.
مستندات API
برای مشاهده مستندات API، می‌توانید به مسیر زیر مراجعه کنید:

```
http://127.0.0.1:8000/versioning/schema/swagger-ui/
```
این مستندات با استفاده از drf-spectacular و drf-spectacular-sidecar ایجاد شده است.

نویسنده
نام شما
ایمیل: aliactionsmart3@gmail.com
گیت‌هاب: cleph
مجوز
این پروژه تحت مجوز MIT منتشر شده است.



---





