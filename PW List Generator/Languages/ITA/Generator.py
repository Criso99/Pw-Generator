import secrets
import string
import os

def genera_password(lunghezza=12):
    """Genera una password sicura con lunghezza predefinita o fornita."""
    caratteri = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(caratteri) for _ in range(lunghezza))
    return password

def pulisci_schermo():
    """Funzione per pulire lo schermo in modo portabile."""
    print("\033c", end="")  # ANSI escape sequence per pulire lo schermo

def salva_password_in_file(nome_file, numero_password, lunghezza_password=12):
    """Genera un numero specificato di password e le salva in un file di testo nella cartella PwList."""
    # Creare la cartella 'PwList' se non esiste
    cartella = "PwList"
    if not os.path.exists(cartella):
        os.makedirs(cartella)
    
    # Percorso completo del file
    percorso_file = os.path.join(cartella, nome_file)
    
    with open(percorso_file, 'w') as file:
        for _ in range(numero_password):
            password = genera_password(lunghezza_password)
            file.write(password + '\n')
    print(f"Le {numero_password} password sono state salvate nel file '{percorso_file}'.")

def main():
    """Funzione principale per gestire l'interazione con l'utente."""
    while True:
        comando = input("Scrivi 'next' per generare una nuova password, 'file' per salvare tot password in un file o 'exit' per uscire: ").strip().lower()
        
        if comando == "next":
            pulisci_schermo()  # Pulisce lo schermo
            password = genera_password(12)
            print("La tua nuova password generata è:", password)
        elif comando == "file":
            nome_file = input("Inserisci il nome del file per salvare le password (esempio: 'passwords.txt'): ").strip()
            numero_password = int(input("Quante password vuoi generare? ").strip())
            lunghezza_password = int(input("Quale dovrebbe essere la lunghezza delle password? ").strip())
            salva_password_in_file(nome_file, numero_password, lunghezza_password)
        elif comando == "exit":
            print("Uscita dal programma.")
            break
        else:
            print("Comando non riconosciuto. Scrivi 'next', 'file' o 'exit'.")

if __name__ == "__main__":
    main()
