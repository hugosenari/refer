from datetime import datetime
from django.db import models
from refer.models import *

# abstract common models fields
class ItemModel (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    short_desc = models.CharField(max_length=120)
    pub_date = models.DateTimeField(default=datetime.now())
    
    class Meta:
        abstract = True
        ordering = ['name']
    
    def __unicode__(self):
        return self.name

# THE OBJECT (most important system object)
class Item (ItemModel):
    long_desc = models.TextField(null=True)

class ItemItemType (ItemModel):
    pass

class ItemRealted(ItemItemType):
    pass

class ItemChild(ItemItemType):
    pass

class ItemExample(ItemItemType):
    pass

# Set a relation of Items
class ItemItem (models.Model):
    from_item = models.ForeignKey(Item, related_name='from_item')
    to_item =   models.ForeignKey(Item, related_name='to_item')
    type = models.ForeignKey(ItemItemType)
    
    def __unicode__(self):
        return u"%s %s" % (self.from_item, self.to_item)

class ItemDictionary(ItemChild):
    "Dictionary was maded to represents code language"
    pass


class ItemLexical(ItemChild):
    "Used in items that are lexical items"
    pass

class ItemTokens(ItemLexical):
    "Use in tokens of language: ie {}, (), :, etc. "
    pass

class ItemKeywords(ItemLexical):
    "Use in code reserved keywords: ie class, static, var, etc."
    pass


class ItemAtribute(ItemChild):
    "Define vars"
    pass

class ItemMethod(ItemAtribute):
    "Define functions"
    pass

class ItemParams(ItemAtribute):
    "Define function params"
    pass

class ItemConstant(ItemAtribute):
    "Define constants"
    pass


class ItemUrl(ItemChild):
    "This is a link for oficial documentation"
    pass