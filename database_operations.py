from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def read(self, path="database.txt") -> set:
        pass

    @abstractmethod
    def write(self, row: str, path="database.txt"):
        pass

    @abstractmethod
    def rewrite(self, id: str, new_row: str, path="database.txt"):
        pass


class TextDB(Database):

    def read(self, path="database.txt") -> list:
        json_list = list()

        with open(f'{path}', 'r') as file:
            for line in file.readlines():
                json_line = {"id": None, "date": None, "category": None, "sum": None, "Annotation": None}
                items = line.split(' ')

                i = -1
                for key in json_line.keys():
                    i += 1
                    json_line[key] = items[i]

                json_list.append(json_line)
        return json_list

    def write(self, row: str, path="database.txt"):
        with open(f"{path}", "a") as file:
            file.write("\n" + row)

    def rewrite(self, row_id: str, new_row: str, path="database.txt"):
        new_lines = list()

        with open(f"{path}", "r") as file:
            lines = file.readlines()
            for line in lines:
                items = line.split(" ")
                if items[0] == row_id:
                    new_lines.append(new_row)
                    continue
                new_lines.append(line)

        with open(f"{path}", "w") as file:
            for line in new_lines:
                file.write(line)
