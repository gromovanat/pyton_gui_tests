from comtypes.client import CreateObject
import os

# создаем путь к директории проекта через: берем положение текущего файла и поднимемся вверх по дереву 2 раза
project_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

xl = CreateObject("Excel.Application")
# запускаем в видимом режиме
xl.Visible = 1
wb = xl.Workbooks.Add()
# создаем таблицу из 10 строк через цикл
for i in range(10):
    xl.Range["A%s" % (i+1)].Value[()] = "group %s" % i
#сохраняем файл в директории проекта
wb.SaveAs(os.path.join(project_dir, "groups.xlsx"))
# закрыть Exel
xl.Quit()
# в директории проекта появляется сохраненный файл
