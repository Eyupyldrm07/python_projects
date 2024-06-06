### Türkçe README (README_TR.md)

# Bankamatik Uygulaması

Bu Python betiği, kullanıcıların hesaplarından para çekmelerine olanak tanıyan basit bir bankamatik (ATM) uygulamasını simüle eder.

## Hesap Bilgileri

Betiğe iki örnek hesap tanımlanmıştır:
- Eyup YILDIRIM
- Mustafa YILDIRIM

Her hesabın:
- `ad`: Hesap sahibinin adı
- `hesapNo`: Hesap numarası
- `bakiye`: Hesap bakiyesi
- `ekHesap`: Ek hesap limiti

## Fonksiyonlar

### `paraCek(hesap, miktar)`

Bu fonksiyon para çekme işlemini gerçekleştirir. Hesap bakiyesinin para çekme işlemi için yeterli olup olmadığını kontrol eder. Yetersizse, kullanıcıya ek hesap kullanma seçeneği sunar.

### `bakiyeSorgula(hesap)`

Bu fonksiyon, hesabın mevcut bakiyesini ve ek hesap limitini yazdırır.

## Kullanım

1. Betiği çalıştırın:
    ```bash
    python atm_application.py
    ```
2. Betik, Eyup YILDIRIM'in hesabından iki para çekme işlemi simüle edecektir.

## Örnek

```plaintext
Merhaba Eyup YILDIRIM
Paranızı alabilirsiniz.
13245678 nolu hesabınızda 0 TL bulunmaktadır. Ek hesap limitiniz ise 2000 TL bulunmaktadır.
******************************
Merhaba Eyup YILDIRIM
Ek hesap kullanılsın mı (E/H): e
Paranızı alabilirsiniz.
13245678 nolu hesabınızda 0 TL bulunmaktadır. Ek hesap limitiniz ise 0 TL bulunmaktadır





# ATM Application

This Python script simulates a simple ATM (Automated Teller Machine) application that allows users to withdraw money from their accounts.

## Account Information

Two sample accounts are defined in the script:
- Eyup YILDIRIM
- Mustafa YILDIRIM

Each account has:
- `name`: Account holder's name
- `accountNo`: Account number
- `balance`: Account balance
- `overdraft`: Overdraft limit

## Functions

### `withdraw_money(account, amount)`

This function handles the money withdrawal process. It checks if the account balance is sufficient for the withdrawal. If not, it offers the user the option to use their overdraft account.

### `check_balance(account)`

This function prints the current balance and overdraft limit of the account.

## Usage

1. Run the script:
    ```bash
    python atm_application.py
    ```
2. The script will simulate two withdrawals from Eyup YILDIRIM's account.

## Example

```plaintext
Merhaba Eyup YILDIRIM
Paranızı alabilirsiniz.
13245678 nolu hesabınızda 0 TL bulunmaktadır. Ek hesap limitiniz ise 2000 TL bulunmaktadır.
******************************
Merhaba Eyup YILDIRIM
Ek hesap kullanılsın mı (E/H): e
Paranızı alabilirsiniz.
13245678 nolu hesabınızda 0 TL bulunmaktadır. Ek hesap limitiniz ise 0 TL bulunmaktadır.