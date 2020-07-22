def lin():
    print('-'*30)

def editarEventos(events, service):
    lin()
    print('Deseja editar algum evento')
    print('SIM / NÃO')
    lin()
    inicio = reconhecimento().lower()
    if inicio == 'sim':
        lin()
        print("Editando Eventos")
        lin()

        print("Escolha um titulo")
        titulo = reconhecimento().lower()
        print(titulo.lower())
        lin()

        encontrado = False
        for event in events:
           if (event['summary'].lower() == titulo):
               editar(event, service)
               encontrado = True

        if (encontrado == False):
            lin()
            print("Evento não encontrado!")
            editarEventos(events, service)


def editar(event, service):
    print("Escolha um novo titulo")
    titulo = reconhecimento().lower()
    print(titulo.lower())
    lin()

    print("Data Inicio")
    dateI = reconhecimento().capitalize()
    print(dateI)

    print('Data Fim')
    dateF = reconhecimento().capitalize()
    print(dateF)
    lin()

    print('Hora inicio')
    horaInicio = reconhecimento().capitalize()
    print(horaInicio)
    lin()
    print('Hora Fim')
    horaFim = reconhecimento().capitalize()
    print(horaFim)
    lin()

    event['summary'] = titulo
    event['start'] = {
                        'dateTime': '{}'.format(day(dateI)) + 'T'+ hours(horaInicio),
                        'timeZone': 'Brazil/East',
                    }

    event['end'] = {
                    'dateTime': '{}'.format(day(dateF)) + 'T'+ hours(horaFim),
                    'timeZone': 'Brazil/East',
                   }


    
    updated_event = service.events().update(calendarId='primary', eventId=event['id'], body=event).execute()

    print('Evento Atualizado...', updated_event['updated'])
    input("Pressione uma tecla para continuar...")
