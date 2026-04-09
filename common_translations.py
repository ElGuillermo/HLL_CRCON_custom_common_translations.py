"""
common_translations.py

Common translation set
for HLL CRCON (https://github.com/MarechJ/hll_rcon_tool)
custom plugins

Source : https://github.com/ElGuillermo

Feel free to use/modify/distribute, as long as you keep this note in your code
"""

# Translations
# key : english, french, german, spanish, polish, brazilian portuguese, russian, chinese
# ----------------------------------------------

TRANSL = {
    # Roles
    "armycommander": ["commander", "commandant", "Kommandant", "comandante", "dowódca", "comandante", "командир", "指挥官"],
    "officer": ["squad leader", "officier", "Offizier", "líder de escuadrón", "dowódca drużyny", "líder de esquadrão", "офицер", "小队长"],
    "rifleman": ["rifleman", "fusilier", "Schütze", "fusilero", "strzelec", "fuzileiro", "стрелок", "步枪手"],
    "assault": ["assault", "assault", "Sturmangreifer", "asalto", "szturmowiec", "assalto", "штурмовик", "突击手"],
    "automaticrifleman": ["automatic rifleman", "fusilier automatique", "Automatikgewehrschütze", "fusilero automático", "strzelec automatyczny", "fuzileiro automático", "автоматический стрелок", "自动步枪手"],
    "medic": ["medic", "médecin", "Sanitäter", "médico", "medyk", "médico", "медик", "医务兵"],
    "support": ["support", "soutien", "Unterstützung", "apoyo", "wsparcie", "suporte", "поддержка", "支援兵"],
    "heavymachinegunner": ["heavy machinegunner", "mitrailleur", "Maschinengewehrschütze", "ametrallador pesado", "strzelec km", "metralhador pesado", "тяжелый пулеметчик", "重机枪手"],
    "antitank": ["antitank", "antichar", "Panzerabwehr", "antitanque", "przeciwpancerny", "antitanque", "противотанковый", "反坦克手"],
    "engineer": ["engineer", "ingénieur", "Pionier", "ingeniero", "inżynier", "engenheiro", "инженер", "工兵"],
    "tankcommander": ["tank commander", "commandant de char", "Panzerkommandant", "comandante de tanque", "dowódca czołgu", "comandante de tanque", "командир танка", "坦克指挥官"],
    "crewman": ["crewman", "équipier", "Besatzungsmitglied", "tripulante", "członek załogi", "tripulante", "член экипажа", "乘员"],
    "artilleryobserver": ["artillery observer", "observateur d'artillerie", "Artilleriebeobachter", "observador de artillería", "obserwator artylerii", "observador de artilharia", "артиллерийский наблюдатель", "炮兵观察员"],
    "operator": ["artillery operator", "opérateur d'artillerie", "Artilleriebediener", "operador de artillería", "operator artylerii", "operador de artilharia", "оператор артиллерии", "炮兵操作员"],
    "gunner": ["artillery gunner", "servant d'artillerie", "Artillerieschütze", "artillero", "operator artylerii", "atirador de artilharia", "артиллерист-наводчик", "炮手"],
    "sniper": ["sniper", "sniper", "Scharfschütze", "francotirador", "snajper", "atirador de elite", "снайпер", "狙击手"],
    "spotter": ["spotter", "observateur", "Späher", "observador", "obserwator", "observador", "наблюдатель", "侦察兵"],

    # Units
    "infantry": ["infantry", "infanterie", "Infanterie", "infantería", "piechota", "infantaria", "пехота", "步兵"],
    "armor": ["armor", "blindés", "Panzerung", "blindados", "pancerne", "blindados", "бронетехника", "装甲部队"],
    "artillery": ["artillery", "artillerie", "Artillerie", "artillería", "artyleria", "artilharia", "артиллерия", "火炮"],
    "reconnaissance": ["reconnaissance", "reconnaissance", "Aufklärung", "reconocimiento", "rozpoznanie", "reconhecimento", "разведка", "侦察"],
    # "infantry_short": ["inf", "inf", "inf", "inf", "pie", "inf", "пех", "步兵"],
    # "armor_short": ["arm", "bli", "pz", "bli", "czo", "bli", "тнк", "装甲"],
    # "artillery_short": ["art", "art", "art", "art", "art", "art", "арт", "火炮"],
    # "recon_short": ["rec", "rec", "aufk", "rec", "zwi", "rec", "разв", "侦察"],

    # Teams
    "all_players": ["all players", "tous les joueurs", "Alle Spieler", "todos los jugadores", "wszyscy gracze", "todos os jogadores", "все игроки", "所有玩家"],
    "allies": ["Allies", "Alliés", "Alliierte", "Aliados", "Alianci", "Aliados", "Союзники", "盟军"],
    "axis": ["Axis", "Axe", "Achsenmächte", "Eje", "Oś", "Eixo", "Ось", "轴心国"],
    # "allies_short": ["all", "all", "all", "ali", "ali", "ali", "соз", "盟军"],
    # "axis_short": ["axi", "axe", "ach", "eje", "oś", "eix", "ось", "轴心"],

    # Stats
    "level": ["level", "niveau", "Level", "nivel", "poziom", "nível", "уровень", "等级"],
    "lvl": ["lvl", "niv", "Lvl", "nvl", "poz", "nvl", "ур", "级"],
    "combat": ["combat", "combat", "kampf", "combate", "walka", "combate", "боевой счет", "战斗"],
    "offense": ["attack", "attaque", "Angriff", "ataque", "atak", "ataque", "нападение", "进攻"],
    "defense": ["defense", "défense", "Verteidigung", "defensa", "obrona", "defesa", "защита", "防御"],
    # support (already defined in Roles)
    "kills": ["kills", "kills", "kills", "bajas", "zabójstwa", "abates", "убийства", "击杀"],
    "deaths": ["deaths", "morts", "tode", "muertes", "zgony", "mortes", "смерти", "死亡"],

    # "team_kills": ["team kills", "team kills", "team kills", "team kills", "team kills", "team kills", "убийства своих", "队友击杀"],
    # "vehicle_kills": ["vehicle kills", "kills véhicules", "fahrzeug kills", "bajas de vehículos", "zabójstwa w pojeździe", "abates de veículos", "убийства в технике", "载具击杀"],
    # "vehicles_destroyed": ["vehicles destroyed", "véhicules détruits", "fahrzeuge zerstört", "vehículos destruidos", "pojazdy zniszczone", "veículos destruídos", "техника уничтожена", "载具销毁"],
    # "teamplay": ["combat + support", "combat + soutien", "kampf + unterstützung", "combate + apoyo", "walka + wsparcie", "combate + apoio", "бой + поддержка", "团队配合"],
    # "offdef": ["offensive + defensive", "attaque + défense", "offensiv + defensiv", "ofensiva + defensiva", "ataki + obrona", "ofensiva + defensiva", "атака + оборона", "攻防比"],
    # "kd": ["kills / deaths", "kills / morts", "kills / tode", "kills / deaths", "zabójstwa / zgony", "kills / mortes", "убийства / смерти", "KD比"],
    # "kpm": ["kills / minute", "kills / minute", "kills / minute", "bajas / minuto", "zabójstwa / minutę", "abates / minuto", "убийств / минуту", "击杀 / 分"],

    # "team_kills_short": ["TK", "TK", "TK", "TK", "TK", "TK", "ТК", "队友击杀"],
    # "vehicle_kills_short": ["v.kills", "kills/véhic", "fzg.kills", "bajas/veh", "zab. poj.", "abates/veí", "уб. тех.", "载具击杀"],
    # "vehicles_destroyed_short": ["v.destr", "véhic.détru", "fzg.zen", "veh.destr.", "poj.znisz", "veí.destru", "техн. унич", "载具销毁"],
    # "teamplay_short": ["cmb+sup", "cmb+sup", "kpf+unt", "cmb+sup", "wal+wsp", "cmb+sup", "бой+под", "团队配合"],
    # "offdef_short": ["off+def", "off+def", "off+def", "off+def", "off+def", "off+def", "атк+обр", "攻防比"],
    # "kd_short": ["kills/deaths", "kills/morts", "kills/tode", "kills/deaths", "zab./zgony", "kills/mortes", "уб./см.", "KD比"],
    # "kpm_short": ["kills/min", "kills/min", "kills/min", "bajas/min", "zab./min", "abates/min", "уб./мин", "击杀/分"],

    # Units
    "years": ["years", "années", "Jahre", "años", "lata", "anos", "годы", "年"],
    "monthes": ["monthes", "mois", "Monate", "meses", "miesiące", "meses", "месяцы", "月"],
    "weeks": ["weeks", "semaines", "Wochen", "semanas", "tygodnie", "semanas", "недели", "周"],
    "days": ["days", "jours", "Tage", "días", "dni", "dias", "дни", "天"],
    "hours": ["hours", "heures", "Stunden", "horas", "godziny", "horas", "часы", "小时"],
    "minutes": ["minutes", "minutes", "Minuten", "minutos", "minuty", "minutos", "минуты", "分钟"],
    "seconds": ["seconds", "secondes", "Sekunden", "segundos", "sekundy", "segundos", "секунды", "秒"],

    # all_time_stats
    # (hooks_custom_chatcommands.py -> WARNING : circular import)
    # "firsttimehere": ["first time here", "tu es venu(e) il y a", "zum ersten Mal hier"],
    # "gamesessions": ["game sessions", "sessions de jeu", "Spielesitzungen"],
    # "playedgames": ["played games", "parties jouées", "gespielte Spiele"],
    # "cumulatedplaytime": ["cumulated play time", "temps de jeu cumulé", "kumulierte Spielzeit"],
    # "averagesession": ["average session", "session moyenne", "Durchschnittliche Sitzung"],
    # "punishments": ["punishments", "punitions", "Strafen"],
    # "nopunish": ["None ! Well done !", "Aucune ! Félicitations !", "Keiner! Gut gemacht!"],
    # "favoriteweapons": ["favorite weapons", "armes favorites", "Lieblingswaffen"],
    # "victims": ["victims", "victimes", "Opfer"],
    # "nemesis": ["nemesis", "nemesis", "Nemesis"],

    # Various
    "average": ["average", "moyenne", "Durchschnitt", "promedio", "średnia", "média", "средний", "平均"],
    "avg": ["avg", "moy", "avg", "prom", "śr", "méd", "ср", "均"],
    "distribution": ["distribution", "distribution", "Verteilung", "distribución", "dystrybucja", "distribuição", "распределение", "分布"],
    "players": ["players", "joueurs", "Spieler", "jugadores", "gracze", "jogadores", "игроки", "玩家"],
    "squads": ["squads", "escouades", "Trupps", "escuadras", "drużyny", "esquadrões", "отряды", "小队"],
    "score": ["score", "score", "Punktzahl", "puntuación", "wynik", "pontuação", "счет", "得分"],
    "stats": ["stats", "stats", "Statistiken", "estadísticas", "statystyki", "estatísticas", "статистика", "统计数据"],
    "total": ["total", "total", "Summe", "total", "suma", "total", "всего", "总计"],
    "tot": ["tot", "tot", "sum", "tot", "suma", "tot", "итог", "总"],
    "officers": ["officers", "officiers", "Offiziere", "oficiales", "oficerowie", "oficiais", "офицеры", "军官"],
    "punishment": ["punishment", "punition", "Bestrafung", "castigo", "kara", "punição", "наказание", "惩罚"],
    "ratio": ["ratio", "ratio", "Verhältnis", "ratio", "stosunek", "razão", "соотношение", "比率"],
    "victim": ["victim", "victime", "Opfer", "víctima", "ofiara", "vítima", "жертва", "受害者"],
    "na": ["N/A", "N/D", "N.V.", "N/D", "N/D", "B/D", "Н/Д", "无"],  # "Not available"

    # automod_forbid_role.py
    "play_as": ["Play as", "A pris le rôle", "Spiele als", "Jugar como", "Graj jako", "Jogar como", "Играет как", "扮演"],
    "engaged_action": ["Engaged action :", "Action souhaitée :", "Laufende Aktion", "Acción realizada :", "Podjęte działanie :", "Ação engajada :", "Начатое действие :", "进行的操作 :"],
    "reason": ["Reason :", "Raison :", "Ursache :", "Razón :", "Powód :", "Motivo :", "Причина :", "原因 :"],
    "action_result": ["Action result :", "Résultat de l'action :", "Ergebnis der Aktion", "Resultado de la acción :", "Wynik działania :", "Resultado da ação :", "Результат действия :", "操作结果 :"],
    "success": ["Success", "Réussite", "Erfolg", "Éxito", "Sukces", "Sucesso", "Успех", "成功"],
    "failure": ["Failure", "Échec", "Fehler", "Fallo", "Niepowodzenie", "Falha", "Провал", "失败"],
    "unknown_action": ["Misconfigured action", "Action mal configurée", "Falsch konfigurierte Aktion", "Acción mal configurada", "Źle skonfigurowana akcja", "Ação mal configurada", "Неверно настроенное действие", "配置错误的操作"],
    "testmode": ["Test mode (no action)", "Mode test (aucune action)", "Testmodus (keine Aktion)", "Modo de prueba (sin acción)", "Tryb testowy (brak akcji)", "Modo de teste (sem ação)", "Тестовый режим (без действий)", "测试模式 (无操作)"],

    # watch_killrate.py
    "lastusedweapons": ["last used weapon(s)", "dernière(s) arme(s) utilisée(s)", "Zuletzt verwendete Waffe(n)", "última(s) arma(s) usada(s)", "ostatnia(e) użyta(e) broń(e)", "última(s) arma(s) utilizada(s)", "последнее(ие) использованное(ые) оружие", "最后使用的武器"],
    "noweaponfound": ["None (arti charger ? No new kill ?)", "Aucune (chargeur arti ? Pas de nouveau kill ?)", "Keiner (arti Ladegerät ? Kein neuer Kill ?)", "Ninguna (cargador de artillería ? No hay nueva muerte ?)", "Brak (ładowarka artylerii ? Brak nowego zabójstwa ?)", "Nenhuma (carregador de artilharia ? Sem novo abate ?)", "Нет (арти зарядное устройство ? Нет нового убийства ?)", "无 (火炮装填 ? 没有新的击杀 ?)"],

    # language_doorkeeper.py
    "expectedanswer": ["Expected answer", "Réponse attendue", "Erwartete Antwort", "Respuesta esperada", "Oczekiwana odpowiedź", "Resposta esperada", "Ожидаемый ответ", "预期答案"],
    "receivedanswer": ["Received answer", "Réponse reçue", "Antwort erhalten", "Respuesta recibida", "Otrzymana odpowiedź", "Resposta recebida", "Полученный ответ", "收到答案"],
    "blank": ["(blank)", "(rien)", "(leer)", "(en blanco)", "(puste)", "(em branco)", "(пусто)", "(空白)"],
    "result": ["Result", "Résultat", "Ergebnis", "Resultado", "Wynik", "Resultado", "Результат", "结果"],
    "gaveavalidanswer": ["Gave a valid answer", "A bien répondu à la question", "Hat eine gute Antwort gegeben", "Dio una respuesta válida", "Udzielił poprawnej odpowiedzi", "Deu uma resposta válida", "Дал правильный ответ", "给出了一个有效答案"],
    "disconnectedbeforetest": ["Disconnected before being tested.", "est parti avant la question.", "links vor der Frage.", "Se desconectó antes de ser probado.", "Odłączył się przed sprawdzeniem.", "Desconectou antes de ser testado.", "Отключился до проверки.", "在测试前断开连接。"],
    "disconnectedbeforekick": ["left before the kick.", "est parti avant le kick.", "vor dem Ausschluss verlassen.", "Se fue antes de la expulsión.", "Odszedł przed wykopaniem.", "Saiu antes do kick.", "Ушел до кика.", "在踢出前离开了。"],
    "hasbeenkicked": ["has been kicked.", "a été kické du serveur.", "wurde vom Server geworfen.", "ha sido expulsado.", "został wyrzucony.", "foi kickado.", "был кикнут.", "已被踢出服务器。"],
    "flaggedvalid": ["has been flagged as valid.", "a été flaggé 'FR'.", "wurde als gültig gekennzeichnet.", "ha sido marcado como válido.", "został oznaczony jako ważny.", "foi sinalizado como válido.", "был помечен как действительный.", "已被标记为有效。"],
    "processingtime": ["Processing time (secs) : ", "Temps de traitement (secs) : ", "Bearbeitungszeit (Sek.) : ", "Tiempo de procesamiento (segundos) : ", "Czas przetwarzania (sek.) : ", "Tempo de processamento (seg) : ", "Время обработки (сек) : ", "处理时间 (秒) : "]
}
