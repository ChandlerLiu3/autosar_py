"""Unit tests for BSW-related XML elements"""

# pylint: disable=missing-class-docstring, missing-function-docstring
import os
import sys
import unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))
import autosar.xml.element as ar_element  # noqa E402
import autosar  # noqa E402


class TestServiceSoftwareComponentType(unittest.TestCase):

    def test_read_write_empty(self):
        element = ar_element.ServiceSoftwareComponentType("ServiceType")
        writer = autosar.xml.Writer()
        xml = '''<SERVICE-SW-COMPONENT-TYPE>
  <SHORT-NAME>ServiceType</SHORT-NAME>
</SERVICE-SW-COMPONENT-TYPE>'''
        self.assertEqual(writer.write_str_elem(element), xml)
        reader = autosar.xml.Reader()
        parsed: ar_element.ServiceSoftwareComponentType = reader.read_str_elem(xml)
        self.assertIsInstance(parsed, ar_element.ServiceSoftwareComponentType)
        self.assertEqual(parsed.name, "ServiceType")


class TestBswModuleDescription(unittest.TestCase):

    def test_read_write_module_id(self):
        element = ar_element.BswModuleDescription("BswM", module_id="042")
        writer = autosar.xml.Writer()
        xml = '''<BSW-MODULE-DESCRIPTION>
  <SHORT-NAME>BswM</SHORT-NAME>
  <MODULE-ID>042</MODULE-ID>
</BSW-MODULE-DESCRIPTION>'''
        self.assertEqual(writer.write_str_elem(element), xml)
        reader = autosar.xml.Reader()
        parsed: ar_element.BswModuleDescription = reader.read_str_elem(xml)
        self.assertIsInstance(parsed, ar_element.BswModuleDescription)
        self.assertEqual(parsed.name, "BswM")
        self.assertEqual(parsed.module_id, "042")


class TestBswModuleEntry(unittest.TestCase):

    def test_read_write_basic_fields(self):
        element = ar_element.BswModuleEntry(
            "MainFunction",
            service_id="3",
            is_reentrant=False,
            is_synchronous=True,
            call_type="SCHEDULED",
            execution_context="TASK",
            sw_service_impl_policy="STANDARD",
        )
        writer = autosar.xml.Writer()
        xml = '''<BSW-MODULE-ENTRY>
  <SHORT-NAME>MainFunction</SHORT-NAME>
  <SERVICE-ID>3</SERVICE-ID>
  <IS-REENTRANT>false</IS-REENTRANT>
  <IS-SYNCHRONOUS>true</IS-SYNCHRONOUS>
  <CALL-TYPE>SCHEDULED</CALL-TYPE>
  <EXECUTION-CONTEXT>TASK</EXECUTION-CONTEXT>
  <SW-SERVICE-IMPL-POLICY>STANDARD</SW-SERVICE-IMPL-POLICY>
</BSW-MODULE-ENTRY>'''
        self.assertEqual(writer.write_str_elem(element), xml)
        reader = autosar.xml.Reader()
        parsed: ar_element.BswModuleEntry = reader.read_str_elem(xml)
        self.assertIsInstance(parsed, ar_element.BswModuleEntry)
        self.assertFalse(parsed.is_reentrant)
        self.assertTrue(parsed.is_synchronous)
        self.assertEqual(parsed.call_type, "SCHEDULED")


class TestSwcBswMapping(unittest.TestCase):

    def test_read_write_behavior_refs(self):
        element = ar_element.SwcBswMapping(
            "Mapping_0",
            bsw_behavior_ref="/Bsw/BswInternalBehavior",
            swc_behavior_ref="/Swc/SwcInternalBehavior",
        )
        writer = autosar.xml.Writer()
        xml = '''<SWC-BSW-MAPPING>
  <SHORT-NAME>Mapping_0</SHORT-NAME>
  <BSW-BEHAVIOR-REF DEST="BSW-INTERNAL-BEHAVIOR">/Bsw/BswInternalBehavior</BSW-BEHAVIOR-REF>
  <SWC-BEHAVIOR-REF DEST="SWC-INTERNAL-BEHAVIOR">/Swc/SwcInternalBehavior</SWC-BEHAVIOR-REF>
</SWC-BSW-MAPPING>'''
        self.assertEqual(writer.write_str_elem(element), xml)
        reader = autosar.xml.Reader()
        parsed: ar_element.SwcBswMapping = reader.read_str_elem(xml)
        self.assertIsInstance(parsed, ar_element.SwcBswMapping)
        self.assertEqual(parsed.bsw_behavior_ref, "/Bsw/BswInternalBehavior")
        self.assertEqual(parsed.swc_behavior_ref, "/Swc/SwcInternalBehavior")


class TestBswImplementation(unittest.TestCase):

    def test_read_write_empty(self):
        element = ar_element.BswImplementation("BswImpl")
        writer = autosar.xml.Writer()
        xml = '''<BSW-IMPLEMENTATION>
  <SHORT-NAME>BswImpl</SHORT-NAME>
</BSW-IMPLEMENTATION>'''
        self.assertEqual(writer.write_str_elem(element), xml)
        reader = autosar.xml.Reader()
        parsed: ar_element.BswImplementation = reader.read_str_elem(xml)
        self.assertIsInstance(parsed, ar_element.BswImplementation)
        self.assertEqual(parsed.name, "BswImpl")


if __name__ == '__main__':
    unittest.main()
