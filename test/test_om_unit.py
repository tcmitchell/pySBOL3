import os
import unittest

import sbol3

MODULE_LOCATION = os.path.dirname(os.path.abspath(__file__))
SBOL3_LOCATION = os.path.join(MODULE_LOCATION, 'SBOLTestSuite', 'SBOL3')


class TestMeasure(unittest.TestCase):

    def setUp(self) -> None:
        sbol3.set_defaults()

    def tearDown(self) -> None:
        sbol3.set_defaults()

    def test_create(self):
        unit = 'https://sbolstandard.org/examples/millimolePerLitre'
        value = 0.1
        types = ['https://identifiers.org/SBO:0000196',
                 'https://identifiers.org/SBO:0000197']
        measure = sbol3.Measure(value, unit)
        measure.types = types
        self.assertIsNotNone(measure)
        self.assertIsInstance(measure, sbol3.Measure)
        self.assertEqual(value, measure.value)
        self.assertCountEqual(types, measure.types)
        self.assertEqual(unit, measure.unit)

    def test_read_from_file(self):
        test_file = os.path.join(SBOL3_LOCATION, 'measurement_entity',
                                 'measurement', 'measurement.nt')
        doc = sbol3.Document()
        doc.read(test_file, sbol3.NTRIPLES)
        uri = 'https://sbolstandard.org/examples/M9_Glucose_CAA/CaCl2/measure1'
        measure = doc.find(uri)
        self.assertIsNotNone(measure)
        self.assertIsInstance(measure, sbol3.Measure)
        self.assertEqual(0.1, measure.value)
        self.assertCountEqual(['https://identifiers.org/SBO:0000196',
                               'https://identifiers.org/SBO:0000197'],
                              measure.types)
        self.assertEqual('https://sbolstandard.org/examples/millimolePerLitre',
                         measure.unit)
        self.assertEqual('measure1', measure.display_id)


class TestPrefixedUnit(unittest.TestCase):

    def setUp(self) -> None:
        sbol3.set_defaults()

    def tearDown(self) -> None:
        sbol3.set_defaults()

    def test_create(self):
        sbol3.set_namespace('https://github.com/synbiodex/pysbol3')
        display_id = 'millimole'
        symbol = display_id
        label = display_id
        prefix = 'https://sbolstandard.org/examples/milli'
        unit = 'https://sbolstandard.org/examples/mole'
        punit = sbol3.PrefixedUnit(display_id, symbol, label, unit, prefix)
        self.assertIsNotNone(punit)
        self.assertIsInstance(punit, sbol3.PrefixedUnit)
        self.assertCountEqual(prefix, punit.prefix)
        self.assertEqual(unit, punit.unit)
        self.assertEqual(symbol, punit.symbol)
        self.assertEqual(label, punit.label)
        self.assertEqual(display_id, punit.display_id)

    def test_read_from_file(self):
        test_file = os.path.join(SBOL3_LOCATION, 'measurement_entity',
                                 'measurement', 'measurement.nt')
        doc = sbol3.Document()
        doc.read(test_file, sbol3.NTRIPLES)
        uri = 'https://sbolstandard.org/examples/millimole'
        punit = doc.find(uri)
        self.assertIsNotNone(punit)
        self.assertIsInstance(punit, sbol3.PrefixedUnit)
        self.assertCountEqual('https://sbolstandard.org/examples/milli', punit.prefix)
        self.assertEqual('https://sbolstandard.org/examples/mole', punit.unit)
        self.assertEqual('millimole', punit.label)
        self.assertEqual('millimole', punit.name)
        self.assertEqual('millimole', punit.display_id)


class TestSingularUnit(unittest.TestCase):

    def setUp(self) -> None:
        sbol3.set_defaults()

    def tearDown(self) -> None:
        sbol3.set_defaults()

    def test_create(self):
        sbol3.set_namespace('https://github.com/synbiodex/pysbol3')
        display_id = 'litre'
        symbol = display_id
        label = display_id
        unit = 'https://sbolstandard.org/examples/litre'
        factor = 0.001
        sunit = sbol3.SingularUnit(display_id, symbol, label)
        sunit.unit = unit
        sunit.factor = factor
        self.assertIsNotNone(sunit)
        self.assertIsInstance(sunit, sbol3.SingularUnit)
        self.assertEqual(0.001, sunit.factor)
        self.assertEqual(unit, sunit.unit)
        self.assertEqual(symbol, sunit.symbol)
        self.assertEqual(label, sunit.label)

    def test_read_from_file(self):
        test_file = os.path.join(SBOL3_LOCATION, 'measurement_entity',
                                 'measurement', 'measurement.nt')
        doc = sbol3.Document()
        doc.read(test_file, sbol3.NTRIPLES)
        uri = 'https://sbolstandard.org/examples/litre'
        sunit = doc.find(uri)
        self.assertIsNotNone(sunit)
        self.assertIsInstance(sunit, sbol3.SingularUnit)
        self.assertEqual(0.001, sunit.factor)
        self.assertIsNone(sunit.unit)
        self.assertIsNone(sunit.symbol)
        self.assertCountEqual(['L', 'L2'], sunit.alternative_symbols)
        self.assertEqual('liter', sunit.label)
        self.assertCountEqual(['liter', 'litre2'], sunit.alternative_labels)
        self.assertIsNotNone(sunit.comment)
        self.assertIsNotNone(sunit.long_comment)
        self.assertEqual('liter', sunit.name)
        self.assertIsNotNone(sunit.description)
        self.assertEqual('litre', sunit.display_id)


if __name__ == '__main__':
    unittest.main()
