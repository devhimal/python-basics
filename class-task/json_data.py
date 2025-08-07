import json
from rich.console import Console
from rich.table import Table

with open('./data.json', 'r') as file:
    data = json.load(file)
    print(data)
console = Console()
table = Table(title="JSON Data")

table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Age", style="magenta")
table.add_column("City", style="green")

for item in data:
    table.add_row(item['name'], str(item['age']), item['country'])

console.print(table)
