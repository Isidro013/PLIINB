def lin():
    print('-'*30)

def criar(service):
    print("Titulo:")
    tit = reconhecimento().capitalize()
    print(tit)
    lin()
    print("Endereço:")
    ende = reconhecimento().capitalize()
    print(ende)
    lin()
    print("Descrição")
    desc = reconhecimento().capitalize()
    print(desc)
    lin()
    print("Data Inicio")
    dateI = reconhecimento().capitalize()
    print(dateI)
    lin()
    print('Data Fim')
    dateF = reconhecimento().capitalize()
    print(dateF)
    lin()

    print("Hora inicio")
    horaInicio = reconhecimento().capitalize()
    print(horaInicio)
    lin()
    print('Hora Fim')
    horaFim = reconhecimento().capitalize()
    print(horaFim)
    lin()
   
    event = {
      'summary': '{}'.format(tit),
      'location': '{}'.format(ende),
      'description': '{}'.format(desc),
       'start': {
        'dateTime': '{}'.format(day(dateI)) + 'T'+ hours(horaInicio),
        'timeZone': 'Brazil/East',
      },
      'end': {
        'dateTime': '{}'.format(day(dateF)) + 'T'+ hours(horaFim),
        'timeZone': 'Brazil/East',
      },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Compromisso agendado: %s' % (event.get('htmlLink')))