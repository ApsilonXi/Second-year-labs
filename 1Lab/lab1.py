class NewClass:

    def __init__(self):
        self.employe = str()
        self.obj = str()
        self.data = str()
        self.time = str()
        self.notice = str()
        self.RecordReceive = list()
        self.RecordReturn = list()

    def RecordsReceive(self, employe, obj, data, time, notice):

        self.RecordReceive = [
            ('Петров И.И.', '444', '12.01.21', '13:45', 'Примечаний нет'), 
            ('Петров И.И.', '345', '16.02.21', '12:12', 'Примечаний нет'),
            ('Иванов Ф.А.', '222', '13.04.22', '11:00', 'Примечаний нет')
        ]

        self.RecordReceive.append((employe, obj, data, time, notice))
        return self.RecordReceive

    def RecordsReturn(self, employe, obj, data):

        self.RecordReturn = [
            ('Соколова В.И.', '444', '11.12.21'), 
            ('Панов П.Р.', '345', '14.12.21'),
            ('Панов П.Р.', '222', '16.06.22')
        ]

        self.RecordReturn.append((employe, obj, data))
        return self.RecordReturn

    def Info(self, employe, data):

        for i in range(len(self.RecordReceive)):
            if self.RecordReceive[i][0] == employe:
                print(employe, self.RecordReceive[i][1])

        data_up = data[0].split('.')
        data_down = data[1].split('.')

        for i in range(len(self.RecordReceive)):
            i_data = self.RecordReceive[i][2].split('.')
            if (int(i_data[2]) >= int(data_up[2])) and (int(i_data[2]) <= int(data_down[2])):
                if (int(i_data[1]) >= int(data_up[1])) and (int(i_data[1]) <= int(data_down[1])):
                    if (int(i_data[0]) >= int(data_up[0])) or (int(i_data[0]) <= int(data_down[0])):
                        print(self.RecordReceive[i][2], self.RecordReceive[i][1])

        print('----------------')
        print(self.RecordReceive)
        print('----------------')
        print(self.RecordReturn)
Securite = NewClass()

print('Запись сдачи под охрану объекта: ')
Securite.RecordsReceive(
    employe = input('ФИО сотрудника: '),
    obj = input('Номер объекта: '),
    data = input('Дата сдачи: '),
    time = input('Время сдачи: '),
    notice = input('Примечание: ')
)

print('-----------------------')

print('Запись снятия с охраны объекта: ')
Securite.RecordsReturn(
    employe = input('ФИО сотрудника: '),
    obj = input('Номер объекта: '),
    data = input('Дата снятия: ')
)

print('----------------------------')

employe_z = input('Сотрудник: ')
data_z = [input('Верхняя граница: '), input('Нижняя граница: ')]
Securite.Info(employe_z, data_z)




