#!/usr/bin/python3

""" Description: Creates a class named Base """


class Base():
    """ Base Class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Manage id attribute """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dicts):
        """ returns JSON string representation of list_dicts"""
        if list_dicts is None or len(list_dicts) == 0:
            return "[]"
        return json.dumps(list_dicts)

    @staticmethod
    def from_json_string(json_string):
        """
            returns the list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            writes JSON string of list_objs to a file
        """
        fname = cls.__name__ + ".json"
        content = []

        if list_objs is not None:
            for obj in list_objs:
                obj = obj.to_dictionary()
                json_dict = json.loads(cls.to_json_string(obj))
                content.append(json_dict)

        with open(fname, "w") as jfile:
            json.dump(content, jfile)

    @classmethod
    def create(cls, **dictionary):
        """
            returns an instance with all attributes already set
        """
        from models.rectangle import Rectangle
        from models.square import Square

        if cls.__name__ == "Rectangle":
            mod = Rectangle(2, 7)
        elif cls.__name__ == "Square":
            mod = Square(6)
        mod.update(**dictionary)
        return (mod)

    @classmethod
    def load_from_file(cls):
        """
            returns a list of instances
        """
        fname = cls.__name__ + ".json"

        try:
            with open(fname, encoding='utf8') as jfile:
                content = cls.from_json_string(jfile.read())
        except:
            return []

        instances = []

        for instance in content:
            temp = cls.create(**instance)
            instances.append(temp)

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            serializes in CSV and saves in a file
        """
        fname = cls.__name__ + ".csv"

        if list_objs is None:
            with open(fname, "w") as cfile:
                cfile.write("[]")
        else:
            with open(fname, "w") as cfile:
                writer = csv.writer(cfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.width, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
            deserializes from CSV from a file.
        """
        fname = cls.__name__ + ".csv"

        with open(fname, "r") as cfile:
            if cls.__name__ == "Rectangle":
               reader = csv.DictReader(cfile, fieldnames={'id','width',
                                                          'height', 'x', 'y'})
            elif cls.__name__ == "Square":
               reader = csv.DictReader(cfile, fieldnames={'id', 'size', 'x', 'y'})

            insts = []
            for inst in reader:
                inst = {x: int(y) for x, y in inst.items()}
                temp = cls.create(**inst)
                insts.append(temp)

        return insts
