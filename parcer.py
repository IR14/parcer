import requests as rq
import pandas as pd

miem = pd.DataFrame(
    {'LAB': ['Международная лаборатория суперкомпьютерного атомистического моделирования и многомасштабного анализа',
             'Научная лаборатория Интернета вещей и киберфизических систем',
             'Учебно-исследовательская лаборатория Интернет технологий и сервисов',
             'Учебно-исследовательская лаборатория функциональной безопасности космических аппаратов и систем',
             'Научно-учебная лаборатория квантовой наноэлектроники',
             'Научно-учебная лаборатория телекоммуникационных систем'],
     'LINK': ['https://samma.hse.ru/persons',
              'https://miem.hse.ru/liot/persons',
              'https://miem.hse.ru/uvpmiem/lab/internetekcon/persons',
              'https://miem.hse.ru/uvpmiem/lab/ka/labpersons',
              'https://miem.hse.ru/quantum/persons',
              'https://miem.hse.ru/telecom/persons']})

cs = pd.DataFrame(
    {'LAB': ['Международная лаборатория интеллектуальных систем и структурного анализа',
             'Международная лаборатория теоретической информатики',
             'Международная лаборатория стохастических алгоритмов и анализа многомерных данных',
             'Международная лаборатория алгебраической топологии и ее приложений',
             'Научно-учебная лаборатория компании Яндекс',
             'Научно-учебная лаборатория методов анализа больших данных',
             'Научно-учебная лаборатория анализа данных в финансовых технологиях',
             'Научно-учебная лаборатория моделирования и управления сложными системами',
             'Научно-учебная лаборатория биоинформатики',
             'Научно-учебная лаборатория моделей и методов вычислительной прагматики',
             'Научно-учебная лаборатория процессно-ориентированных информационных систем (ПОИС)'],
     'LINK': ['https://cs.hse.ru/ai/issa/persons',
              'https://cs.hse.ru/big-data/tcs-lab/persons',
              'https://cs.hse.ru/hdilab/persons',
              'https://cs.hse.ru/ata-lab/staff',
              'https://cs.hse.ru/big-data/yandexlab/persons',
              'https://cs.hse.ru/lambda/persons',
              'https://cs.hse.ru/big-data/bayeslab/daft/persons',
              'https://cs.hse.ru/big-data/csmc/people',
              'https://cs.hse.ru/big-data/bioinform/persons',
              'https://cs.hse.ru/ai/computational-pragmatics/persons',
              'https://pais.hse.ru/persons']})

eco = pd.DataFrame(
    {'LAB': ['Международная лаборатория стохастического анализа и его приложений',
             'Международная лаборатория макроэкономического анализа',
             'Международная лаборатория экспериментальной и поведенческой экономики',
             'Международная лаборатория институционального анализа экономических реформ',
             'Научно-учебная лаборатория исследований спорта',
             'Научно-учебная лаборатория корпоративных финансов',
             'Лаборатория по финансовой инженерии и риск-менеджменту',
             'Научно-учебная лаборатория макроструктурного моделирования экономики России',
             'Научно-учебная лаборатория измерения благосостояния',
             'Проектно-учебная лаборатория анализа финансовых рынков'],
     'LINK': ['https://lsa.hse.ru/persons',
              'https://macro.hse.ru/persons',
              'https://epee.hse.ru/persons',
              'https://lia.hse.ru/persons',
              'https://economics.hse.ru/sport/persons',
              'https://cfcenter.hse.ru/persons',
              'https://fermlab.hse.ru/persons',
              'https://economics.hse.ru/gmsm/persons',
              'https://economics.hse.ru/welfare/persons',
              'https://fmlab.hse.ru/persons']})

math = pd.DataFrame(
    {'LAB': ['Международная лаборатория зеркальной симметрии и автоморфных форм',
             'Международная лаборатория теории представлений и математической физики ВШЭ – Сколтех'],
     'LINK': ['https://ms.hse.ru/persons',
              'https://mf.hse.ru/persons']})

physic = pd.DataFrame(
    {'LAB': ['Международная лаборатория физики конденсированного состояния'],
     'LINK': ['https://cmp.hse.ru/staff']})

# идентификаторы
group = 'fa-card__group persons-department__group'  # объект списка сотрудников
person = 'fa-person__item'  # нахождение данных о текущем сотруднике в group
name = 'fa-person__name'  # ФИО сотрудника
info = 'fa-person__info'  # должность лабы
end = 'extra-left'  # ускоряет работу
link = 'www.hse.ru/'  # личная ссылка
contact = 'Контакты'  # телефон
mail = 'Электронная почта'  # почта
google = 'https://scholar.google'  # цитируемость
tag = 'b-person-data__inner b-person-data__tags'  # объект списка интересов
passion = 'tag_small'  # итересы
token = 'gsc_md_hist_b'  # объект таблицы цитирования на сайте google.schoolar
token_year = 'class="gsc_g_t"'  # объект с годами
token_value = 'gsc_g_al'  # объект с значениями по годам

def full_name(text):
    alphabet_ru = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')

    left, right = 0, len(text) - 1

    while alphabet_ru.isdisjoint(text[left].lower()):
        left += 1
    while alphabet_ru.isdisjoint(text[right].lower()):
        right -= 1

    return text[left:right + 1]


def phone(text):
    ex = []

    while text.find('<br>') != -1:

        text = text[text.find('<br>') + len('<br>'):]

        if text.find('<br>') == -1:
            ex.append(text)
        else:
            ex.append(text[:text.find('<br>')])

    for i in range(len(ex)):
        ex[i] = ex[i].replace(' ', '')
        ex[i] = ex[i].replace('(', '')
        ex[i] = ex[i].replace(')', '')
        ex[i] = ex[i].replace('-', '')

    return ex


def setmail(text):
    temp = eval('[' + text + ']')

    try:
        temp[temp.index('-at-')] = '@'
    except:
        temp[temp.index('at')] = '@'

    return ''.join(temp)


def rate(text, passion):
    ex = []

    while True:

        try:

            text = text[text.index(passion) + len(passion) + 1:]

            try:
                ex.append(full_name(text[:text.index(passion)]))
            except ValueError:
                ex.append(full_name(text))

        except ValueError:
            break

    return ex


def years(text):
    ex = []

    while text.find('right') != -1:
        text = text[text.index('right') + len('right'):]
        ex.append(text[text.index('>') + 1:text.index('>') + 5])

    return ex


def values(text, token_value, year_list):
    ex = []

    prev, now = None, None

    while text.find('z-index:') != -1:

        text = text[text.index('z-index:') + len('z-index:'):]

        prev, now = now, text[:1]

        if prev != None and now != None:
            if int(prev) - int(now) > 1:
                for i in range(int(prev) - int(now) - 1):
                    ex.append('0')

        text = text[text.index(token_value) + len(token_value):]
        ex.append(text[text.index('>') + 1:text.index('<')])

    if int(now) != 1:
        for i in range(int(now) - 1):
            ex.append('0')

    if len(year_list) != len(ex):
        for i in range(len(year_list) - len(ex)):
            ex.insert(0, '0')

    return ex


def parcer(df, group, person, name, info, link, contact, mail, google, tag, passion):
    department = {'NAME': [], 'LINK': [], 'VAC': [], 'LAB': [], 'MAIL': [],
                  'PHONE': [], 'TAG': [], 'RATE': [], 'YEAR': [], 'NUM': []}

    flag = False

    print('Please wait, the program will take about 5 min.')

    for i in df['LINK']:

        try:

            data = rq.get(i)

            try:

                data = data.text[data.text.index(group):data.text.index(end)]

                while data.find(person) != -1:

                    try:

                        data = data[data.index(person):]
                        data = data[data.index(name):]
                        data = data[data.index(link):]

                        try:
                            department['LINK'].append('https://' + data[:data.index('"')])
                        except:
                            department['LINK'].append('None')

                        try:
                            department['NAME'].append(full_name(data[data.index('"') + 1:data.index(info)]))
                        except:
                            department['NAME'].append('None')

                        if department['NAME'][-1] == 'None':

                            department['NAME'].pop()
                            department['LINK'].pop()

                        else:

                            try:
                                department['VAC'].append(
                                    full_name(data[data.index(info) + len(info) + 1:data.index('/div')]))
                            except:
                                department['VAC'].append('None')

                            department['LAB'].append(df['LAB'][df['LINK'].values.tolist().index(i)])

                            if department['LINK'][-1] != 'None':

                                temp = rq.get(department['LINK'][-1])

                                try:
                                    temp = temp.text[temp.text.index(contact):]
                                    department['PHONE'].append(phone(temp[temp.index('<dd>'):temp.index('</dd>')]))
                                except:
                                    department['PHONE'].append('None')

                                try:
                                    temp = temp[temp.index(mail):]
                                    department['MAIL'].append(setmail(temp[temp.index('[') + 1:temp.index(']')]))
                                except:
                                    department['MAIL'].append('None')

                                try:
                                    temp = temp[temp.index(google):]
                                    temp = temp[temp.index('user='):]
                                    department['RATE'].append('https://scholar.google.com/citations?' + temp[
                                                                                                        :temp.index(
                                                                                                            'AAAAJ') + len(
                                                                                                            'AAAAJ')])
                                except:
                                    department['RATE'].append('None')

                                try:
                                    temp = temp[temp.index(tag):]
                                    department['TAG'].append(rate(temp[:temp.index('/div')], passion))
                                except:
                                    department['TAG'].append('None')

                                if department['RATE'][-1] != 'None':

                                    try:
                                        temp = rq.get(department['RATE'][-1])

                                        temp = temp.text[temp.text.index(token):]
                                        department['YEAR'].append(years(temp[temp.index(token_year):temp.index(
                                            'class="' + token_value[:len(token_value) - 1] + '"')]))

                                        w = temp[temp.index('class="' + token_value[:len(token_value) - 1] + '"'):]
                                        department['NUM'].append(values(w[:w.index('</div>')], token_value,
                                                                        department['YEAR'][-1]))
                                    except:
                                        department['YEAR'].append('None')
                                        department['NUM'].append('None')
                                else:
                                    department['YEAR'].append('None')
                                    department['NUM'].append('None')

                    except ValueError:
                        flag = True

            except ValueError:
                print("Department group hasn't found")
                flag = True

        except rq.exceptions.RequestException:
            print('Connection timeout occured!')
            flag = True

    print('SUCCESS!')

    return department, flag

global_data = []
for i in (miem, cs, eco, math, physic):
    global_data.append(parcer(i, group, person, name, info, link, contact, mail, google, tag, passion))
