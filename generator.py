import random
import csv
import calendar

# Fonction pour générer les noms des clients pour les crédits


def generate_client_name(names_file, companies_file):
    if random.choice([True, False]):  # Choix aléatoire entre person et company
        with open(names_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            chosen = random.choice(list(reader))
            return f"{chosen['GivenName']} {chosen['Surname']}"
    else:
        with open(companies_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            chosen = random.choice(list(reader))
            return chosen['Company Name']


# Fonction principale pour générer les extraits
def generate_statements(client_name, start_year, start_month, num_months, line_range, initial_balance,
                        profit_month_percentage):
    current_balance = initial_balance
    profit_months = random.sample(range(num_months), int(num_months * (profit_month_percentage / 100)))

    for month_offset in range(num_months):
        year, month = divmod(start_month - 1 + month_offset, 12)
        year += start_year
        days_in_month = calendar.monthrange(year, month + 1)[1]

        # Définir l'objectif de solde de fin de mois
        target_end_balance = current_balance + (
            500 if month_offset in profit_months else -500)  # Ajoute ou retire 500 en fonction du type de mois

        # Nom du fichier CSV pour ce mois
        filename = f"{client_name}_{month + 1}_{year}.csv"
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Intitulé', 'Débit', 'Crédit'])

            # Solde de début pour le mois
            writer.writerow([f"{year}-{month + 1}-01", 'Solde de début', '', "{:.2f}".format(current_balance)])

            monthly_debit = 0
            monthly_credit = 0
            num_lines = random.randint(line_range[0], line_range[1])

            # Génération des transactions aléatoires
            for _ in range(num_lines - 1):
                date = f"{year}-{month + 1}-{random.randint(1, days_in_month)}"
                if random.random() > 0.5:
                    label = random.choice(labels)
                    amount = random.uniform(50.0, 500.0)
                    writer.writerow([date, label, "{:.2f}".format(amount), ''])
                    monthly_debit += amount
                else:
                    label = f"{random.choice(['paiement', 'virement'])} de {generate_client_name('names.csv', 'company.csv')}"
                    amount = random.uniform(100.0, 2000.0)
                    writer.writerow([date, label, '', "{:.2f}".format(amount)])
                    monthly_credit += amount

            # Ajustement final pour atteindre l'objectif de solde de fin de mois
            final_adjustment = target_end_balance - (current_balance + monthly_credit - monthly_debit)
            if final_adjustment > 0:
                writer.writerow([f"{year}-{month + 1}-last", 'Ajustement final', '', "{:.2f}".format(final_adjustment)])
                monthly_credit += final_adjustment
            else:
                writer.writerow(
                    [f"{year}-{month + 1}-last", 'Ajustement final', "{:.2f}".format(-final_adjustment), ''])
                monthly_debit += -final_adjustment

            # Mise à jour et écriture du solde final
            current_balance = current_balance + monthly_credit - monthly_debit
            writer.writerow(['', 'Total', "{:.2f}".format(monthly_debit), "{:.2f}".format(monthly_credit)])
            writer.writerow(['', 'Solde actuel', '', "{:.2f}".format(current_balance)])


labels = [
    'Restaurant Bilou', 'Essence Coûteuse', 'McDonald\'s', 'SAS Fistula', 'Fournisseurs Divers', 'Auchan',
    'Fournitures de Bureau', 'Frais Juridiques', 'Services de Consultation', 'Services Internet',
    'Remboursement Client',
    'Paiement de Loyer', 'Achat de Matériel', 'Frais de Publicité'
]

# Paramètres d'entrée de l'utilisateur (exemple)
client_name = input("Nom du client: ")
start_year = int(input("Année de départ: "))
start_month = int(input("Mois de départ (1-12): "))
num_months = int(input("Nombre de mois à générer: "))
line_range = (int(input("Nombre minimum de lignes: ")), int(input("Nombre maximum de lignes: ")))
initial_balance = float(input("Solde de départ du compte: "))
profit_month_percentage = int(input("Pourcentage de mois bénéficiaires (%): "))

generate_statements(client_name, start_year, start_month, num_months, line_range, initial_balance,
                    profit_month_percentage)
