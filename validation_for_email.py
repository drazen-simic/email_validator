
import re

def validate_email():
    while True:
        try:
            # 1. Unos korisničkog e-maila
            email = input("Unesite e-mail adresu (ili 'exit' za izlaz): ").strip()

            # Ako korisnik unese 'exit', prekida rad
            if email.lower() == 'exit':
                print("Izlaz iz programa.")
                break

            # 2. Pretvaranje u mala slova i split
            email = email.lower()
            if email.count('@') != 1:
                raise ValueError("E-mail mora sadržavati točno jedan znak '@'.")

            username, domain = email.split('@')

            # 3. Regex provjere
            username_pattern = r'^[a-zA-Z][a-zA-Z0-9._]*$'
            domain_pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$'

            if not re.match(username_pattern, username):
                raise ValueError(
                    "Username smije sadržavati samo slova, brojeve, točke i donje crte, i mora početi slovom."
                )

            if not re.match(domain_pattern, domain):
                raise ValueError(
                    "Domena mora biti u formatu ime_domena.nastavak gdje je nastavak 2-6 slova."
                )

            # 6. Ispis validnog e-maila
            print(f"Unijeli ste ispravan e-mail: {email}")
            break

        except ValueError as e:
            # 4. Prikaz greške i mogućnost ponovnog unosa
            print(f"Greška: {e}")
            print("Pokušajte ponovo ili unesite 'exit' za izlaz.")
            continue

if __name__ == "__main__":
    validate_email()
