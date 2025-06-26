"""
common_translations.py

Common translation set
for HLL CRCON (https://github.com/MarechJ/hll_rcon_tool)
custom plugins

Source : https://github.com/ElGuillermo

Feel free to use/modify/distribute, as long as you keep this note in your code
"""

# Translations
# key : english, french, german, spanish
# ----------------------------------------------

TRANSL = {
    # Roles
    "armycommander": ["commander", "commandant", "Kommandant", "comandante"],
    "officer": ["squad leader", "officier", "Offizier", "líder de escuadra"],
    "rifleman": ["rifleman", "fusilier", "Schütze", "fusilero"],
    "assault": ["assault", "assault", "Sturmangreifer", "asalto"],
    "automaticrifleman": ["automatic rifleman", "fusilier automatique", "Automatikgewehrschütze", "fusilero automático"],
    "medic": ["medic", "médecin", "Sanitäter", "médico"],
    "support": ["support", "soutien", "Unterstützung", "apoyo"],
    "heavymachinegunner": ["heavy machinegunner", "mitrailleur", "Maschinengewehrschütze", "ametrallador pesado"],
    "antitank": ["antitank", "antichar", "Panzerabwehr", "antitanque"],
    "engineer": ["engineer", "ingénieur", "Pionier", "ingeniero"],
    "tankcommander": ["tank commander", "commandant de char", "Panzerkommandant", "comandante de tanque"],
    "crewman": ["crewman", "équipier", "Besatzungsmitglied", "tripulante"],
    "spotter": ["spotter", "observateur", "Späher", "observador"],
    "sniper": ["sniper", "sniper", "Scharfschütze", "francotirador"],

    # Teams
    "allies": ["Allies", "Alliés", "Alliierte", "Aliados"],
    "axis": ["Axis", "Axe", "Achsenmächte", "Eje"],

    # Stats
    "level": ["level", "niveau", "Level", "nivel"],
    "lvl": ["lvl", "niv", "Lvl", "niv"],
    "combat": ["combat", "combat", "Kampfeffektivität", "combate"],
    "offense": ["attack", "attaque", "Angriff", "ataque"],
    "defense": ["defense", "défense", "Verteidigung", "defensa"],
    "kills": ["kills", "kills", "Kills", "muertes"],
    "deaths": ["deaths", "morts", "Deaths", "bajas"],

    # Units
    "years": ["years", "années", "Jahre", "años"],
    "monthes": ["monthes", "mois", "Monate", "meses"],
    "weeks": ["weeks", "semaines", "Wochen", "semanas"],
    "days": ["days", "jours", "Tage", "días"],
    "hours": ["hours", "heures", "Stunden", "horas"],
    "minutes": ["minutes", "minutes", "Minuten", "minutos"],
    "seconds": ["seconds", "secondes", "Sekunden", "segundos"],

    # Various
    "average": ["average", "moyenne", "Durchschnitt", "promedio"],
    "avg": ["avg", "moy", "avg", "prom"],
    "distribution": ["distribution", "distribution", "Verteilung", "distribución"],
    "players": ["players", "joueurs", "Spieler", "jugadores"],
    "score": ["score", "score", "Punktzahl", "puntuación"],
    "stats": ["stats", "stats", "Statistiken", "estadísticas"],
    "total": ["total", "total", "Summe", "total"],
    "tot": ["tot", "tot", "sum", "tot"],
    "officers": ["officers", "officiers", "Offiziere", "oficiales"],
    "punishment": ["punishment", "punition", "Bestrafung", "castigo"],
    "ratio": ["ratio", "ratio", "Verhältnis", "relación"],
    "victim": ["victim", "victime", "Opfer", "víctima"],

    # automod_forbid_role.py
    "play_as": ["Play as", "A pris le rôle", "Spiele als", "Tomó el rol de"],
    "engaged_action": ["Engaged action :", "Action souhaitée :", "Laufende Aktion", "Acción realizada:"],
    "reason": ["Reason :", "Raison :", "Ursache :", "Razón:"],
    "action_result": ["Action result :", "Résultat de l'action :", "Ergebnis der Aktion", "Resultado de la acción:"],
    "success": ["Success", "Réussite", "Erfolg", "Éxito"],
    "failure": ["Failure", "Échec", "Fehler", "Fallo"],
    "unknown_action": ["Misconfigured action", "Action mal configurée", "Falsch konfigurierte Aktion", "Acción mal configurada"],
    "testmode": ["Test mode (no action)", "Mode test (aucune action)", "Testmodus (keine Aktion)", "Modo prueba (sin acción)"],

    # watch_killrate.py
    "lastusedweapons": ["last used weapon(s)", "dernière(s) arme(s) utilisée(s)", "Zuletzt verwendete Waffe(n)", "última(s) arma(s) usada(s)"],
    "noweaponfound": ["None (arti charger ? No new kill ?)", "Aucune (chargeur arti ? Pas de nouveau kill ?)", "Keiner (arti Ladegerät ? Kein neuer Kill ?)", "Ninguna (¿cargador de artillería? ¿Ninguna nueva baja?)"],

    # language_doorkeeper.py
    "expectedanswer": ["Expected answer", "Réponse attendue", "Erwartete Antwort", "Respuesta esperada"],
    "receivedanswer": ["Received answer", "Réponse reçue", "Antwort erhalten", "Respuesta recibida"],
    "blank": ["(blank)", "(rien)", "(leer)", "(vacío)"],
    "result": ["Result", "Résultat", "Ergebnis", "Resultado"],
    "gaveavalidanswer": ["Gave a valid answer", "A bien répondu à la question", "Hat eine gute Antwort gegeben", "Respondió correctamente"],
    "disconnectedbeforetest": ["Disconnected before being tested.", "est parti avant la question.", "links vor der Frage.", "salió antes de la prueba."],
    "disconnectedbeforekick": ["left before the kick.", "est parti avant le kick.", "vor dem Ausschluss verlassen.", "salió antes del kick."],
    "hasbeenkicked": ["has been kicked.", "a été kické du serveur.", "wurde vom Server geworfen.", "fue expulsado del servidor."],
    "flaggedvalid": ["has been flagged as valid.", "a été flaggé 'FR'.", "wurde als gültig gekennzeichnet.", "ha sido marcado como válido."],
    "processingtime": ["Processing time (secs) : ", "Temps de traitement (secs) : ", "Bearbeitungszeit (Sek.) : ", "Tiempo de procesamiento (seg.): "]
}
