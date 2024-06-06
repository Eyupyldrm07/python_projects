### Türkçe README (README_TR.md)

# GitHub Takipçi Kazıyıcı

Bu Python betiği, Selenium kullanarak GitHub'a giriş yapar ve belirtilen kullanıcının takipçilerini alır.

## Gereksinimler

- Python 3.x
- `selenium` kütüphanesi
- Tarayıcınız için bir WebDriver (ör. Firefox için GeckoDriver)

## Kurulum

1. Depoyu klonlayın veya betiği indirin.
2. Gerekli kütüphaneyi pip kullanarak yükleyin:
    ```bash
    pip install selenium
    ```
3. WebDriver'ın yüklü olduğundan ve PATH'inize eklendiğinden emin olun. Firefox için GeckoDriver'ı [buradan](https://github.com/mozilla/geckodriver/releases) indirebilirsiniz.

## Kullanım

1. Aynı dizinde `githubUserInfo.py` adlı bir dosya oluşturun ve GitHub kimlik bilgilerinizi girin:
    ```python
    username = "kullanici_adiniz"
    password = "sifreniz"
    ```
2. Betiği çalıştırın:
    ```bash
    python github_follower_scraper.py
    ```

Betiğiniz GitHub'a giriş yapacak ve belirtilen kullanıcının takipçilerinin listesini yazdıracaktır.

## Örnek

```plaintext
['takipci1', 'takipci2', 'takipci3']









# GitHub Follower Scraper

This Python script logs into GitHub and retrieves the followers of a specified user using Selenium.

## Requirements

- Python 3.x
- `selenium` library
- A WebDriver for your browser (e.g., GeckoDriver for Firefox)

## Installation

1. Clone the repository or download the script.
2. Install the required library using pip:
    ```bash
    pip install selenium
    ```
3. Make sure you have the WebDriver installed and added to your PATH. For Firefox, you can download GeckoDriver from [here](https://github.com/mozilla/geckodriver/releases).

## Usage

1. Create a `githubUserInfo.py` file in the same directory as the script with your GitHub credentials:
    ```python
    username = "your_username"
    password = "your_password"
    ```
2. Run the script:
    ```bash
    python github_follower_scraper.py
    ```

The script will log into GitHub and print the list of followers for the specified user.

## Example

```plaintext
['follower1', 'follower2', 'follower3']