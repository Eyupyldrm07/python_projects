# Not Yönetim Sistemi

Bu Python betiği, öğrenci notlarını okuyarak, girerek ve kaydederek yönetir.

## Fonksiyonlar

### `note_calculate(line)`

Verilen bir öğrenci verisi satırı için ortalama notu ve karşılık gelen harf notunu hesaplar.

### `read_averages()`

`exam_notes.txt` dosyasındaki her öğrenci için ortalama notları okur ve yazdırır.

### `enter_note()`

Kullanıcıdan bir öğrencinin adını, soyadını ve üç sınav notunu girmesini ister ve bu veriyi `exam_notes.txt` dosyasına ekler.

### `record_notes()`

Her öğrenci için ortalama notları hesaplar ve sonuçları `results.txt` dosyasına yazar.

## Kullanım

1. Betiği çalıştırın:
    ```bash
    python grade_management.py
    ```
2. Menüden bir seçenek seçin:
    - `1` ortalama notları okumak ve yazdırmak için
    - `2` yeni notlar girmek için
    - `3` hesaplanan ortalama notları `results.txt` dosyasına kaydetmek için
    - `4` çıkış yapmak için

## Örnek

```plaintext
1- Notları Oku
2- Not Gir
3- Notları Kaydet
4- Çıkış


# Grade Management System

This Python script manages student grades by reading, entering, and recording their exam scores.

## Functions

### `note_calculate(line)`

Calculates the average score and corresponding letter grade for a given line of student data.

### `read_averages()`

Reads and prints the average grades for each student from the `exam_notes.txt` file.

### `enter_note()`

Prompts the user to enter a student's name, surname, and three exam scores, then appends this data to the `exam_notes.txt` file.

### `record_notes()`

Calculates the average grades for each student and writes the results to `results.txt`.

## Usage

1. Run the script:
    ```bash
    python grade_management.py
    ```
2. Choose an option from the menu:
    - `1` to read and print the average grades
    - `2` to enter new grades
    - `3` to save the calculated average grades to `results.txt`
    - `4` to exit

## Example

```plaintext
1- Notları Oku
2- Not Gir
3- Notları Kaydet
4- Çıkış