# Homework-Tasks

## Avtomobillar qidiruv dasturi

Ushbu loyiha Python orqali yaratilgan oddiy, lekin funksional avtomobillar qidiruv tizimidir. Foydalanuvchi istalgan mashina modelini kiritganda, dastur unga mos avtomobillarni topib, narx, rang, turi va tavsifni ko‘rsatadi.

## Xususiyatlar
- istalgan mashina modelini qidirish
- qisman so‘zlar bilan ham topish
- model bo‘yicha qisqacha tavsiyalar ko‘rsatish
- testlar bilan tekshirilgan logika

## How to use

1. Clone or download this repository to your computer.

2. Open the project folder in the terminal:
   ```bash
   cd /path/to/Homework-Tasks
   ```

3. Run the program:
   ```bash
   python3 Task1.py
   ```

4. Enter any car model name when prompted, for example:
   ```bash
   camry
   ```
   or
   ```bash
   audi a4
   ```

The program will show matching car options with price, color, type, and description.

## Testlarni ishga tushirish

```bash
python3 -m unittest -v
```

## Fayllar
- Task1.py — asosiy dastur
- test_task1.py — avtomatlashtirilgan testlar
- __init__.py — paket boshlang‘ich fayli