"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
import random
from django.test import TestCase
from refer.models import Item, ItemItemType, ItemItem

#this values are generated one time when the code is loaded, use it to testes
TEST_VALS = {
    'rand_name': 'name%f ' % (random.random()) * 2,
    'rand_short': 'short%f ' % ( random.random()) * 4,
    'rand_desc': 'desc%f ' % (random.random()) * 200,
    'rand_val': random.random(),
    'max_val': float('infinity'),
    'min_val': - (float('infinity'))
}
#MODEL TESTS
class ItemTest(TestCase):
    def setUp(self):
        "Creates one Item for test"
        Item(name=TEST_VALS['rand_name'],
            short_desc=TEST_VALS['rand_short'],
            long_desc=TEST_VALS['rand_desc']).save()

    def test_insert_and_retrieve(self):
        "Tests the init value is equal to objects value"
        self.assertEqual(1, len(Item.objects.all()))
        if len(Item.objects.all()) > 0:
            self.assertEqual(TEST_VALS['rand_name'],  Item.objects.all()[0].name)
            self.assertEqual(TEST_VALS['rand_short'], Item.objects.all()[0].short_desc)
            self.assertEqual(TEST_VALS['rand_desc'],  Item.objects.all()[0].long_desc)

class ItemItemTypeTest(TestCase):
    def setUp(self):
        "Creates one ItemItemType for test"
        ItemItemType(name=TEST_VALS['rand_name'],
            short_desc=TEST_VALS['rand_short']).save()
    
    def test_insert_and_retrieve(self):
        self.assertEqual(1, len(ItemItemType.objects.all()))
        if len(ItemItemType.objects.all()) > 0:
            self.assertEqual(TEST_VALS['rand_name'],  ItemItemType.objects.all()[0].name)
            self.assertEqual(TEST_VALS['rand_short'], ItemItemType.objects.all()[0].short_desc)

class ItemItemTest(TestCase):
    def setUp(self):
        "Creates one ItemItem for test"
        itemItemType = ItemItemType(name=TEST_VALS['rand_name'],
            short_desc=TEST_VALS['rand_short'])
        itemItemType.save()
        
        itemA = Item(name=TEST_VALS['rand_name'] + 'A',
            short_desc=TEST_VALS['rand_short'] + 'A',
            long_desc=TEST_VALS['rand_desc'] + 'A')
        itemA.save()
        
        itemB = Item(name=TEST_VALS['rand_name'] + 'B',
            short_desc=TEST_VALS['rand_short'] + 'B',
            long_desc=TEST_VALS['rand_desc'] + 'B')
        itemB.save()
        
        ItemItem(from_item=itemA, to_item=itemB, type=itemItemType).save()
        
    def test_insert_and_retrieve(self):
        self.assertEqual(2, len(Item.objects.all()))
        self.assertEqual(1, len(ItemItemType.objects.all()))
        self.assertEqual(1, len(ItemItem.objects.all()))
        print ItemItemType isinstance ItemItem.objects.all()[0].type

#VIEW TESTS
from refer.views import *

class GetTest(TestCase):
    def setUp(self):
        pass
    
    def test_return_item(self):
        "Test open one item"
        pass
    
    def test_return_item_item(self):
        "Test open one subitem"
        pass
    
    def test_return_item_items(self):
        "Test return more subitens"
        pass
    
    def test_return_subitens_filtred_by_type(self):
        "Test return subitens filtred"
        pass
    
    def test_return_tree(self):
        pass