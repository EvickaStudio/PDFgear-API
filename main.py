from api.summary import get_summary
from utility.text_formatter import format_text

message = """
-Einteilung der Übungsgruppen wird morgen (6556.2023) während der Vorlesung freigeschaltet.
-Dies ist eine Kopie einer Mitteilung, die in Ma I (6, 6 WiSe 23/24) gepostet wurde.
"""

# This is where we call the functions, it's so 🔥
message = get_summary(message)

print(format_text(message))