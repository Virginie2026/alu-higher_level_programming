#!/usr/bin/python3
"""Module defining the Base class with JSON and CSV serialization."""
import csv
import json
import os


class Base:
    """Base class for managing id attribute in all classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base instance with id management."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file."""
        filename = f"{cls.__name__}.json"
        if list_objs is None:
            list_dicts = []
        else:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            elif cls.__name__ == "Square":
                dummy = cls(1)
            else:
                dummy = cls()
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as f:
            json_string = f.read()

        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize list_objs to a CSV file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write("")
                return

            writer = csv.writer(f)
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            for obj in list_objs:
                writer.writerow([getattr(obj, field) for field in fieldnames])

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize instances from a CSV file."""
        filename = f"{cls.__name__}.csv"
        if not os.path.exists(filename):
            return []

        instances = []
        with open(filename, "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]

            for row in reader:
                if not row:
                    continue
                dict_repr = {
                    fieldnames[i]: int(row[i]) for i in range(len(fieldnames))
                }
                instances.append(cls.create(**dict_repr))

        return instances
