from datetime import date

class TransformObj:
    def objects_to_values(self, list_objs: list[object]) -> list[list]:
        values = []
        for obj in list_objs:
            obj_values = []
            for key, value in obj.__dict__.items():
                if not key.startswith("__"):
                    if isinstance(value, date):
                        obj_values.append(value.strftime("%Y-%m-%d"))
                    else:
                        obj_values.append(value)
            values.append(obj_values)
        return values

