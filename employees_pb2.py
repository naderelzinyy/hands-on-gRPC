# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: employees.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x65mployees.proto\x12\temployees\"3\n\x08\x45mployee\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\"\x14\n\x12GetEmployeeRequest\"<\n\x13GetEmployeeResponse\x12%\n\x08\x65mployee\x18\x01 \x03(\x0b\x32\x13.employees.Employee\"$\n\x16GetEmployeeByIdRequest\x12\n\n\x02id\x18\x01 \x03(\t\"@\n\x17GetEmployeeByIdResponse\x12%\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x13.employees.Employee\">\n\x15\x43reateEmployeeRequest\x12%\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x13.employees.Employee\"?\n\x16\x43reateEmployeeResponse\x12%\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x13.employees.Employee\">\n\x15UpdateEmployeeRequest\x12%\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x13.employees.Employee\"?\n\x16UpdateEmployeeResponse\x12%\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x13.employees.Employee\"#\n\x15\x44\x65leteEmployeeRequest\x12\n\n\x02id\x18\x01 \x01(\t\"?\n\x16\x44\x65leteEmployeeResponse\x12%\n\x08\x65mployee\x18\x01 \x01(\x0b\x32\x13.employees.Employee2\xc2\x03\n\tEmployees\x12N\n\x0bGetEmployee\x12\x1d.employees.GetEmployeeRequest\x1a\x1e.employees.GetEmployeeResponse\"\x00\x12Z\n\x0fGetEmployeeById\x12!.employees.GetEmployeeByIdRequest\x1a\".employees.GetEmployeeByIdResponse\"\x00\x12W\n\x0e\x43reateEmployee\x12 .employees.CreateEmployeeRequest\x1a!.employees.CreateEmployeeResponse\"\x00\x12W\n\x0eupdateEmployee\x12 .employees.UpdateEmployeeRequest\x1a!.employees.UpdateEmployeeResponse\"\x00\x12W\n\x0e\x64\x65leteEmployee\x12 .employees.DeleteEmployeeRequest\x1a!.employees.DeleteEmployeeResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'employees_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EMPLOYEE']._serialized_start=30
  _globals['_EMPLOYEE']._serialized_end=81
  _globals['_GETEMPLOYEEREQUEST']._serialized_start=83
  _globals['_GETEMPLOYEEREQUEST']._serialized_end=103
  _globals['_GETEMPLOYEERESPONSE']._serialized_start=105
  _globals['_GETEMPLOYEERESPONSE']._serialized_end=165
  _globals['_GETEMPLOYEEBYIDREQUEST']._serialized_start=167
  _globals['_GETEMPLOYEEBYIDREQUEST']._serialized_end=203
  _globals['_GETEMPLOYEEBYIDRESPONSE']._serialized_start=205
  _globals['_GETEMPLOYEEBYIDRESPONSE']._serialized_end=269
  _globals['_CREATEEMPLOYEEREQUEST']._serialized_start=271
  _globals['_CREATEEMPLOYEEREQUEST']._serialized_end=333
  _globals['_CREATEEMPLOYEERESPONSE']._serialized_start=335
  _globals['_CREATEEMPLOYEERESPONSE']._serialized_end=398
  _globals['_UPDATEEMPLOYEEREQUEST']._serialized_start=400
  _globals['_UPDATEEMPLOYEEREQUEST']._serialized_end=462
  _globals['_UPDATEEMPLOYEERESPONSE']._serialized_start=464
  _globals['_UPDATEEMPLOYEERESPONSE']._serialized_end=527
  _globals['_DELETEEMPLOYEEREQUEST']._serialized_start=529
  _globals['_DELETEEMPLOYEEREQUEST']._serialized_end=564
  _globals['_DELETEEMPLOYEERESPONSE']._serialized_start=566
  _globals['_DELETEEMPLOYEERESPONSE']._serialized_end=629
  _globals['_EMPLOYEES']._serialized_start=632
  _globals['_EMPLOYEES']._serialized_end=1082
# @@protoc_insertion_point(module_scope)
