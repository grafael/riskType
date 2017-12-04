from models import CustomField, RiskType

class CustomFieldSerializer():
    
    @staticmethod
    def serialize(cf):
        return {
            "label" : cf.label,
            "type": cf.type,
            "required": cf.required,
            "val": cf.val
        }

    @staticmethod
    def deserialize(js):
        cf = CustomField()
        cf.label = js["label"]
        cf.required = js["required"]
        cf.type = js["type"]
        cf.val = js["val"]

        return cf


class RiskTypeSerializer():
    
    @staticmethod
    def serialize(rt):
        fields = []
        for f in rt.fields:
            fields.append(CustomFieldSerializer.serialize(f))

        return {
            "name": rt.name,
            "fields": fields
        }

    @staticmethod
    def deserialize(js):
        rt = RiskType()
        rt.name = js["name"]

        fields = []
        for field in js["fields"]:
            fields.append(CustomFieldSerializer.deserialize(field))
        
        rt.fields = fields

        return rt