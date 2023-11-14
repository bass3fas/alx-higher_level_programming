#!/usr/bin/python3
""""Defines a Class"""
import json
import csv
import turtle


class Base:
    """to manage id attribute in all your future classes
    and to avoid duplicating the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
         """Initialize a new Base.

        Args:
            id (int): The identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """JSON representation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """JSON representation to python"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """"creating dummy instances """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy_instance = cls(1)
        else:
            dummy_instance = cls()
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """loading from JSON file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                dict_list = cls.from_json_string(json_data)
                return [cls.create(**d) for d in dict_list]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """"saving in CSV format"""
        if list_objs is None:
            list_objs = []
        filename = f"{cls.__name__}.csv"
        with open(filename, 'w', newline='') as file:
            csv_writer = csv.writer(file)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    csv_writer.writerow([obj.id, obj.width,
                                         obj.height, obj.x, obj.y])
                elif cls.__name__ == "Square":
                    csv_writer.writerow([obj.id, obj.size,
                                         obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """reading CSV format file"""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file)
                instances = []
                for row in csv_reader:
                    if cls.__name__ == "Rectangle":
                        instances.append(cls.create(id=int(row[0]),
                                                    width=int(row[1]),
                                                    height=int(row[2]),
                                                    x=int(row[3]),
                                                    y=int(row[4])))
                    elif cls.__name__ == "Square":
                        instances.append(cls.create(id=int(row[0]),
                                                    size=int(row[1]),
                                                    x=int(row[2]),
                                                    y=int(row[3])))
                return instances
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """open window and draw a rectangle"""
        window = turtle.Screen()
        window.bgcolor("white")
        window.title("Drawing Rectangles and Squares")

        t = turtle.Turtle()
        t.speed(2)

        for rect in list_rectangles:
            t.penup()
            t.goto(rect.x, rect.y)
            t.pendown()
            t.color("blue")
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)
            t.forward(rect.width)
            t.left(90)
            t.forward(rect.height)
            t.left(90)

        for square in list_squares:
            t.penup()
            t.goto(square.x, square.y)
            t.pendown()
            t.color("red")
            for _ in range(4):
                t.forward(square.size)
                t.left(90)

        window.mainloop()
