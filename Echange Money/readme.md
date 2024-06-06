### Türkçe README (README_TR.md)

# Döviz Dönüştürücü

Bu Python betiği, ExchangeRate-API kullanarak belirtilen bir miktardaki dövizi başka bir dövize dönüştürür.

## Gereksinimler

- Python 3.x
- `requests` kütüphanesi

## Kurulum

1. Depoyu klonlayın veya betiği indirin.
2. Gerekli kütüphaneyi pip kullanarak yükleyin:
    ```bash
    pip install requests
    ```

## Kullanım

1. Betiği çalıştırın:
    ```bash
    python currency_converter.py
    ```
2. Dönüştürmek istediğiniz döviz türünü girin (ör. `USD`).
3. Almak istediğiniz döviz türünü girin (ör. `TRY`).
4. Dönüştürmek istediğiniz döviz miktarını girin.

Betiğiniz, hedef dövizdeki karşılık gelen miktarı gösterecektir.

## Örnek

```bash
Donusturulen  doviz turu: USD
Alinan doviz turu: TRY
Ne kadar USD Donusturmek istiyorsunuz: 100
100 USD=853.12 TRY


# Currency Converter


This Python script converts a specified amount of one currency to another using the ExchangeRate-API.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script:
    ```bash
    python currency_converter.py
    ```
2. Enter the currency you want to convert from (e.g., `USD`).
3. Enter the currency you want to receive (e.g., `TRY`).
4. Enter the amount of the currency you want to convert.

The script will display the equivalent amount in the target currency.

## Example

```bash
Donusturulen  doviz turu: USD
Alinan doviz turu: TRY
Ne kadar USD Donusturmek istiyorsunuz: 100
100 USD=853.12 TRY