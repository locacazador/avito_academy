import csv
import os
from collections import defaultdict
from typing import Tuple, Dict, DefaultDict


class BaseFileException(Exception):
    """Base class exception for the interaction with files"""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class EmptyFileException(BaseFileException):
    """Raised when there is not data in file"""

    pass


class WrongFileFormatException(BaseFileException):
    """Raised when the file has unexpected format to process"""

    pass


def parse_csv(path: str) -> Tuple:
    """
    Collect data from csv-file into iterable data structure.

    :param path: relative path of file - report, csv format. Expected
           ';' delimiter and header contains fields: Full name, Department,
           Branch, Position, Grade, Salary
    :return: Data - list of named tuples - stores all the information
             about the employees from report

    Example:
             'ФИО полностью;Департамент;Отдел;Должность;Оценка;Оклад
             Баранов Трофим Васильевич;Продажи;B2B;Sales manager;3.8;106600
             Творимир Давыдович Суханов;Маркетинг;Performance;Маркетинг-менеджер;4.0;65900' ->

            (
             ('Баранов Трофим Васильевич', 'Продажи', 'B2B', 'Sales Manager', 3.8, 106600),

             ('Творимир Давыдович Суханов', 'Маркетинг', 'Perfomance', 'Маркетинг-Менеджер', 4.0, 65900)
            )
            # todo: -> namedDict structure (new func)
    """

    data = []
    with open(path, 'r') as file:
        reader = csv.reader(file)
        for idx, row in enumerate(reader):
            if idx and row:  # first contains header, take non empty rows
                data.append(tuple(row[0].split(';')))
    if not data:
        raise EmptyFileException('Пустой файл. Попробуйте другой')
    data = tuple(data)
    return data


def get_department_hierarchy(report_data: Tuple) -> DefaultDict[str, set]:
    """
    Provide information about branches in departments

    :param report_data: parsed data from csv-report of employees
    :return: hierarchy as dict with keys - Department and values - branch
    """
    # todo: Exceptions
    out_dict = defaultdict(set)
    try:
        for employee in report_data:
            department = str(employee[2])
            branch = str(employee[3])
            out_dict[department].add(branch)
        return out_dict
    except IndexError:
        raise WrongFileFormatException('Неверный формат файла')


def print_hierarchy(hierarchy: DefaultDict[str, set]) -> None:
    """
    Print the hierarchy stdout

    :param hierarchy:
    :return: None
    """

    for item in hierarchy:
        print(f'Department is {item}:\n\t', end='')
        print('\n\t'.join(hierarchy[item]))


def fill_dict_department_info(employee: str, dict_to_fill: Dict) -> Dict:
    """
    Fill the dictionary of department

    :param employee: Current employee of the company
    :param dict_to_fill: aggregate information of departments in the company
           Expected fields: name of department,
           population of department,
           salary range of the department
           current amount of total salary in the department
    :return: filled dict with values of current employee
    """

    try:
        _, department, _, _, _, salary = employee
    except ValueError:
        raise WrongFileFormatException('Неверный формат файла')
    salary = int(salary)
    data_of_department = dict_to_fill.get(department)
    if not data_of_department:
        data_of_department = {
            'population': 0,
            'salary_range_tuple': tuple([salary, salary]),  # lets choice salary of first employee
            'mean_salary': 0,
            'sum_salary': 0
        }
        dict_to_fill.update({department: data_of_department})
    data_of_department['population'] += 1
    data_of_department['sum_salary'] += salary
    min_salary, max_salary = data_of_department['salary_range_tuple']
    if salary < min_salary:
        new_salary_range = (salary, max_salary)
    elif salary > max_salary:
        new_salary_range = (min_salary, salary)
    else:
        new_salary_range = data_of_department['salary_range_tuple']
    data_of_department['salary_range_tuple'] = new_salary_range
    return dict_to_fill


def get_department_report(report_data: Tuple[str]) -> Dict[str, dict]:
    """
    Provide agg information of department

    :param report_data:
    :return: Aggregate data of department: name, population,
             minimum & maximum and mean amount of salary
    """

    out_agg_data = {}
    for emp in report_data:
        out_agg_data = fill_dict_department_info(employee=emp, dict_to_fill=out_agg_data)
    # fill the mean salary by division of mean_salary by population
    for department, department_info in out_agg_data.items():
        out_agg_data[department]['mean_salary'] = round(department_info['sum_salary']
                                                        / department_info['population'],
                                                        3)
    return out_agg_data


def convert_department_data_to_str(department_data: Dict, department: str) -> Tuple[str]:
    """
    Collect strings in order to proper output

    :param department_data: dict of aggregate data of the department
    :param department: name of department
    :return: tuple of strings to provide output
    """

    return tuple([f'Department name is {department}:',
                  f'\tNumber of employees: {department_data["population"]}',
                  '\tSalary range between {} {}'.format(*department_data['salary_range_tuple']),
                  f'\tThe mean salary is {department_data["mean_salary"]}'
                  ])


def print_department_report(department_report: Dict) -> None:
    """
    Print to stdout information of the department

    :param department_report: dict of aggregate data of the department
    :return: None
    """

    for department, department_data in department_report.items():
        for item in convert_department_data_to_str(department_data, department):
            print(item)


def export_department_report_to_csv(department_report: Dict, output_filename: str) -> None:
    """
    Create csv file with department report

    :param department_report: dict of aggregate data of the department
    :param output_filename: relative path of the file with the extension
    :return: None
    """

    with open(output_filename, 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(['Наименование департамента',
                         'Штат департамента',
                         'Зарплатная вилка',
                         'Средняя зарплата'])  # todo: Consts
        for department, department_data in department_report.items():
            writer.writerow([department,
                             department_data['population'],
                             '-'.join(str(x) for x in department_data['salary_range_tuple']),
                             department_data['mean_salary']
                             ])


def process_command(command: int, report_data: Tuple) -> None:
    """
    Process user's command according to the list  of possible commands

    :param report_data:
    :param command: user's choice of proposals in menu
    :return: None
    """

    if command == 1:
        hierarchy = get_department_hierarchy(report_data)
        print_hierarchy(hierarchy)
    elif command == 2:
        department_report = get_department_report(report_data)
        print_department_report(department_report)
    elif command == 3:
        department_report = get_department_report(report_data)
        export_department_report_to_csv(department_report, input('Введите название файла с расширением:\n'))
    elif command == 0:
        exit()
    print_menu()


def print_menu() -> None:
    """
    Print the list of possible commands to user

    :return: None
    """

    menu = '''
1. Получить иерархию команд.
2. Получить сводный отчет по департаментам.
3. Получить сводный отчет по департаментам в формате csv-файла.
0. Выход.
    '''
    print(menu)


def main():
    print_menu()
    command = True
    data_processed = False
    data_of_departments = None
    while command:
        try:
            command = int(input())  # try for one line not the whole part
            if command not in [0, 1, 2, 3]:  # todo: const
                print('Неизвестная команда. Повторите ввод')
                continue
            if not data_processed and command:
                csv_filename = input('Введите относительный путь к csv-файлу с отчетом о сотрудниках.\n')
                while not os.path.exists(csv_filename):
                    csv_filename = input('Неверный путь до файла. Введите еще раз.\n')
                data_of_departments = parse_csv(csv_filename)
                data_processed = True
            process_command(command, data_of_departments)
        except ValueError:
            print('Введено не число.')
            continue
        except (EmptyFileException, WrongFileFormatException) as e:
            print(str(e))
            continue


if __name__ == '__main__':
    main()


# todo: mypy --strict --disallow-any
