from Crypto.Cipher import AES
import os

secret_key = b"ChiaveSegretaPerCifraturaAES-GCM"
NONCE_LEN = 16
TAG_LEN = 16


def cifra(testo_in_chiaro):
    cipher = AES.new(secret_key, AES.MODE_GCM)
    testo_cifrato, tag = cipher.encrypt_and_digest(testo_in_chiaro.encode('utf-8'))
    return cipher.nonce + tag + testo_cifrato


def decifra(pacchetto):
    if len(pacchetto) < NONCE_LEN + TAG_LEN:
        return "errore, pacchetto troppo corto"

    nonce = pacchetto[:NONCE_LEN]
    tag = pacchetto[NONCE_LEN:NONCE_LEN + TAG_LEN]
    testo_cifrato = pacchetto[NONCE_LEN + TAG_LEN:]

    cipher = AES.new(secret_key, AES.MODE_GCM, nonce=nonce)
    try:
        return cipher.decrypt_and_verify(testo_cifrato, tag).decode('utf-8')
    except ValueError:
        return "errore, messaggio alterato o chiave sbagliata"
