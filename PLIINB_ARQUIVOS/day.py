import datetime


dayS = ["segunda", "terça", "quarta", "quinta", "sexta", "sabado", "domingo"]


MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", \
         "setembro", "outubro", "novembro", "dezembro"]

dayNUM = ["um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", \
          "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", \
              "dezoito", "dezenove", "vinte", "vinte e um", "vinte e dois", "vinte e três" \
                  "vinte e quatro", "vinte e cinco", "vinte e seis", "vinte e sete", \
                      "vinte e oito", "vinte e nove", "trinta", "trinta e um"]


#reconhece uma palabvra chave para eventos no mes
def day(text):
    
    text = text.lower()
    today = datetime.date.today()

    if text.count("hoje") > 0:
        return today
    
    day = -1
    day_of_week = -1
    month = -1
    year = today.year
    
    for word in text.split():
        if word in MESES:
            month = MESES.index(word) + 1 # procura pelo nome do mês
        elif word in dayS:
            day_of_week = dayS.index(word) # procura pelo nome do day
        elif word.isdigit():
            day = int(word)
        else:
            for nume in dayNUM:
                found = word.find(nume)
                if found > 0:
                    try :
                        day = int(word[:found])
                    except:
                        pass
    if month < today.month and month != -1: # condição para verificar year atual
        year = year+1
    
    if day < today.day and month == -1 and day != -1: #condição para verificar mes
        month = month + 1
        
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week
        
        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7
        return today + datetime.timedelta(dif)
    
    return datetime.date(month=month, day=day, year=year)