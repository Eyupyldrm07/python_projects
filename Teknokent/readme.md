# Selenium ve BeautifulSoup ile Web Scraping

Bu Python betiği, Gaziantep Teknopark web sitesinden şirket bilgilerini Selenium ile tarayıcı otomasyonu ve BeautifulSoup ile HTML ayrıştırma kullanarak toplar.

## Gereksinimler

- Python 3.x
- Selenium
- BeautifulSoup4
- Requests
- Webdriver (ChromeDriver)

## Kurulum

1. Gerekli Python kütüphanelerini yükleyin:
    ```bash
    pip install selenium beautifulsoup4 requests
    ```

2. Chrome WebDriver'ı indirin ve kurun: [ChromeDriver](https://sites.google.com/chromium.org/driver/).

## Kullanım

1. Betiği çalıştırın:
    ```bash
    python web_scraping.py
    ```

2. Betik:
    - Gaziantep Teknopark web sitesine gidecek.
    - "Firma Listesi" bağlantısına tıklayacak.
    - Listelenen şirket sayısını çıkaracak ve yazdıracak.
    - Her bir şirket için, detay sayfasına giderek iletişim bilgilerini çıkaracak.
    - Toplanan bilgileri yazdıracak.

## Örnek

```plaintext
Bulunan Firma sayısı: 10
Firma Listesi öğesi: Bazı Şirket İsmi
Şirket Bilgileri: {'Şirket İsmi': 'sirket_isim', 'Şirket Maili': 'sirket_mail'}

# Web Scraping with Selenium and BeautifulSoup

This Python script scrapes company information from the Gaziantep Technopark website using Selenium for browser automation and BeautifulSoup for HTML parsing.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- Requests
- Webdriver (ChromeDriver)

## Setup

1. Install the required Python libraries:
    ```bash
    pip install selenium beautifulsoup4 requests
    ```

2. Download and install the Chrome WebDriver from [ChromeDriver](https://sites.google.com/chromium.org/driver/).

## Usage

1. Run the script:
    ```bash
    python web_scraping.py
    ```

2. The script will:
    - Navigate to the Gaziantep Technopark website.
    - Click on the "Firma Listesi" link.
    - Extract and print the number of companies listed.
    - For each company, navigate to its detail page and extract the contact information.
    - Print the collected information.

## Example

```plaintext
Found 10 companies
Company List item: Some Company Name
Company Information: {'Company Name': 'company_name', 'Company Email': 'company_email'}