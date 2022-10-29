class pnmImage(object):


    """
        Класс для работы с файлами в pnm формате
    """


def __init__(self):
    """
        Создание переменных для последуещей работы с pnm файлами
        type - тип файла
        info - ширина и высота в исходном формате
        buffer - массив пикселей
        rgd - максимальное значение цвета
        size - ширина и высота в нужном формате
    """
    self.type = None
    self.info = None
    self.buffer = None
    self.rgb = None
    self.size = None


def open(self, path):
    """

    :param self: класс
    :param path: путь к открываемому файлу
    :return: Sucess при успешном выполнении

    При открытии файла проверяет открыт ли он и является ли файлом pnm
    Считывает всю необходимую информацию для файла
    """
    file = open(path, 'rb')
    if file.closed:
        return "The File is not open"
    self.type = file.readline()
    # add type exception
    if self.type.__str__().find("P6") == -1 and self.type.__str__().find("P5") == -1:
        return "This File type is not supported "
    self.info = file.readline()
    width, height = self.info.__str__().split(' ')
    width = width.removeprefix("b'")
    height = height.removesuffix("\\n'")
    # fix size
    if self.type.__str__().find("P6") != -1:
        self.size = int(width) * int(height) * 3
    else:
        self.size = int(width) * int(height)
    self.rgb = file.readline()
    self.buffer = file.read()
    file.close()
    return "Success"


def save(self, path):
    """

    :param self: класс
    :param path: путь к сохранненому файлу

    Открываем файл, а затем записываем все переменные в новый файл
    """
    file = open(path, 'wb')
    # add out exception
    if file.closed:
        print("not open")
    file.write(self.type)
    file.write(self.info)
    file.write(self.rgb)
    file.write(self.buffer)
    file.close()
