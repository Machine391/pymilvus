# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\x12\x13milvus.proto.schema\x1a\x0c\x63ommon.proto\"\xbc\x02\n\x0b\x46ieldSchema\x12\x0f\n\x07\x66ieldID\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x16\n\x0eis_primary_key\x18\x03 \x01(\x08\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x30\n\tdata_type\x18\x05 \x01(\x0e\x32\x1d.milvus.proto.schema.DataType\x12\x36\n\x0btype_params\x18\x06 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x37\n\x0cindex_params\x18\x07 \x03(\x0b\x32!.milvus.proto.common.KeyValuePair\x12\x0e\n\x06\x61utoID\x18\x08 \x01(\x08\x12.\n\x05state\x18\t \x01(\x0e\x32\x1f.milvus.proto.schema.FieldState\"w\n\x10\x43ollectionSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x0e\n\x06\x61utoID\x18\x03 \x01(\x08\x12\x30\n\x06\x66ields\x18\x04 \x03(\x0b\x32 .milvus.proto.schema.FieldSchema\"\x19\n\tBoolArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x08\"\x18\n\x08IntArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x05\"\x19\n\tLongArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x03\"\x1a\n\nFloatArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x02\"\x1b\n\x0b\x44oubleArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x01\"\x1a\n\nBytesArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\x0c\"\x1b\n\x0bStringArray\x12\x0c\n\x04\x64\x61ta\x18\x01 \x03(\t\"\x92\x03\n\x0bScalarField\x12\x33\n\tbool_data\x18\x01 \x01(\x0b\x32\x1e.milvus.proto.schema.BoolArrayH\x00\x12\x31\n\x08int_data\x18\x02 \x01(\x0b\x32\x1d.milvus.proto.schema.IntArrayH\x00\x12\x33\n\tlong_data\x18\x03 \x01(\x0b\x32\x1e.milvus.proto.schema.LongArrayH\x00\x12\x35\n\nfloat_data\x18\x04 \x01(\x0b\x32\x1f.milvus.proto.schema.FloatArrayH\x00\x12\x37\n\x0b\x64ouble_data\x18\x05 \x01(\x0b\x32 .milvus.proto.schema.DoubleArrayH\x00\x12\x37\n\x0bstring_data\x18\x06 \x01(\x0b\x32 .milvus.proto.schema.StringArrayH\x00\x12\x35\n\nbytes_data\x18\x07 \x01(\x0b\x32\x1f.milvus.proto.schema.BytesArrayH\x00\x42\x06\n\x04\x64\x61ta\"t\n\x0bVectorField\x12\x0b\n\x03\x64im\x18\x01 \x01(\x03\x12\x37\n\x0c\x66loat_vector\x18\x02 \x01(\x0b\x32\x1f.milvus.proto.schema.FloatArrayH\x00\x12\x17\n\rbinary_vector\x18\x03 \x01(\x0cH\x00\x42\x06\n\x04\x64\x61ta\"\xd1\x01\n\tFieldData\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.milvus.proto.schema.DataType\x12\x12\n\nfield_name\x18\x02 \x01(\t\x12\x33\n\x07scalars\x18\x03 \x01(\x0b\x32 .milvus.proto.schema.ScalarFieldH\x00\x12\x33\n\x07vectors\x18\x04 \x01(\x0b\x32 .milvus.proto.schema.VectorFieldH\x00\x12\x10\n\x08\x66ield_id\x18\x05 \x01(\x03\x42\x07\n\x05\x66ield\"w\n\x03IDs\x12\x30\n\x06int_id\x18\x01 \x01(\x0b\x32\x1e.milvus.proto.schema.LongArrayH\x00\x12\x32\n\x06str_id\x18\x02 \x01(\x0b\x32 .milvus.proto.schema.StringArrayH\x00\x42\n\n\x08id_field\"\xb1\x01\n\x10SearchResultData\x12\x13\n\x0bnum_queries\x18\x01 \x01(\x03\x12\r\n\x05top_k\x18\x02 \x01(\x03\x12\x33\n\x0b\x66ields_data\x18\x03 \x03(\x0b\x32\x1e.milvus.proto.schema.FieldData\x12\x0e\n\x06scores\x18\x04 \x03(\x02\x12%\n\x03ids\x18\x05 \x01(\x0b\x32\x18.milvus.proto.schema.IDs\x12\r\n\x05topks\x18\x06 \x03(\x03*\x9c\x01\n\x08\x44\x61taType\x12\x08\n\x04None\x10\x00\x12\x08\n\x04\x42ool\x10\x01\x12\x08\n\x04Int8\x10\x02\x12\t\n\x05Int16\x10\x03\x12\t\n\x05Int32\x10\x04\x12\t\n\x05Int64\x10\x05\x12\t\n\x05\x46loat\x10\n\x12\n\n\x06\x44ouble\x10\x0b\x12\n\n\x06String\x10\x14\x12\x0b\n\x07VarChar\x10\x15\x12\x10\n\x0c\x42inaryVector\x10\x64\x12\x0f\n\x0b\x46loatVector\x10\x65*V\n\nFieldState\x12\x10\n\x0c\x46ieldCreated\x10\x00\x12\x11\n\rFieldCreating\x10\x01\x12\x11\n\rFieldDropping\x10\x02\x12\x10\n\x0c\x46ieldDropped\x10\x03\x42U\n\x0eio.milvus.grpcB\x0bSchemaProtoP\x01Z1github.com/milvus-io/milvus-proto/go-api/schemapb\xa0\x01\x01\x62\x06proto3')

_DATATYPE = DESCRIPTOR.enum_types_by_name['DataType']
DataType = enum_type_wrapper.EnumTypeWrapper(_DATATYPE)
_FIELDSTATE = DESCRIPTOR.enum_types_by_name['FieldState']
FieldState = enum_type_wrapper.EnumTypeWrapper(_FIELDSTATE)
globals()['None'] = 0
Bool = 1
Int8 = 2
Int16 = 3
Int32 = 4
Int64 = 5
Float = 10
Double = 11
String = 20
VarChar = 21
BinaryVector = 100
FloatVector = 101
FieldCreated = 0
FieldCreating = 1
FieldDropping = 2
FieldDropped = 3


_FIELDSCHEMA = DESCRIPTOR.message_types_by_name['FieldSchema']
_COLLECTIONSCHEMA = DESCRIPTOR.message_types_by_name['CollectionSchema']
_BOOLARRAY = DESCRIPTOR.message_types_by_name['BoolArray']
_INTARRAY = DESCRIPTOR.message_types_by_name['IntArray']
_LONGARRAY = DESCRIPTOR.message_types_by_name['LongArray']
_FLOATARRAY = DESCRIPTOR.message_types_by_name['FloatArray']
_DOUBLEARRAY = DESCRIPTOR.message_types_by_name['DoubleArray']
_BYTESARRAY = DESCRIPTOR.message_types_by_name['BytesArray']
_STRINGARRAY = DESCRIPTOR.message_types_by_name['StringArray']
_SCALARFIELD = DESCRIPTOR.message_types_by_name['ScalarField']
_VECTORFIELD = DESCRIPTOR.message_types_by_name['VectorField']
_FIELDDATA = DESCRIPTOR.message_types_by_name['FieldData']
_IDS = DESCRIPTOR.message_types_by_name['IDs']
_SEARCHRESULTDATA = DESCRIPTOR.message_types_by_name['SearchResultData']
FieldSchema = _reflection.GeneratedProtocolMessageType('FieldSchema', (_message.Message,), {
  'DESCRIPTOR' : _FIELDSCHEMA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.FieldSchema)
  })
_sym_db.RegisterMessage(FieldSchema)

CollectionSchema = _reflection.GeneratedProtocolMessageType('CollectionSchema', (_message.Message,), {
  'DESCRIPTOR' : _COLLECTIONSCHEMA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.CollectionSchema)
  })
_sym_db.RegisterMessage(CollectionSchema)

BoolArray = _reflection.GeneratedProtocolMessageType('BoolArray', (_message.Message,), {
  'DESCRIPTOR' : _BOOLARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.BoolArray)
  })
_sym_db.RegisterMessage(BoolArray)

IntArray = _reflection.GeneratedProtocolMessageType('IntArray', (_message.Message,), {
  'DESCRIPTOR' : _INTARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.IntArray)
  })
_sym_db.RegisterMessage(IntArray)

LongArray = _reflection.GeneratedProtocolMessageType('LongArray', (_message.Message,), {
  'DESCRIPTOR' : _LONGARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.LongArray)
  })
_sym_db.RegisterMessage(LongArray)

FloatArray = _reflection.GeneratedProtocolMessageType('FloatArray', (_message.Message,), {
  'DESCRIPTOR' : _FLOATARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.FloatArray)
  })
_sym_db.RegisterMessage(FloatArray)

DoubleArray = _reflection.GeneratedProtocolMessageType('DoubleArray', (_message.Message,), {
  'DESCRIPTOR' : _DOUBLEARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.DoubleArray)
  })
_sym_db.RegisterMessage(DoubleArray)

BytesArray = _reflection.GeneratedProtocolMessageType('BytesArray', (_message.Message,), {
  'DESCRIPTOR' : _BYTESARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.BytesArray)
  })
_sym_db.RegisterMessage(BytesArray)

StringArray = _reflection.GeneratedProtocolMessageType('StringArray', (_message.Message,), {
  'DESCRIPTOR' : _STRINGARRAY,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.StringArray)
  })
_sym_db.RegisterMessage(StringArray)

ScalarField = _reflection.GeneratedProtocolMessageType('ScalarField', (_message.Message,), {
  'DESCRIPTOR' : _SCALARFIELD,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.ScalarField)
  })
_sym_db.RegisterMessage(ScalarField)

VectorField = _reflection.GeneratedProtocolMessageType('VectorField', (_message.Message,), {
  'DESCRIPTOR' : _VECTORFIELD,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.VectorField)
  })
_sym_db.RegisterMessage(VectorField)

FieldData = _reflection.GeneratedProtocolMessageType('FieldData', (_message.Message,), {
  'DESCRIPTOR' : _FIELDDATA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.FieldData)
  })
_sym_db.RegisterMessage(FieldData)

IDs = _reflection.GeneratedProtocolMessageType('IDs', (_message.Message,), {
  'DESCRIPTOR' : _IDS,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.IDs)
  })
_sym_db.RegisterMessage(IDs)

SearchResultData = _reflection.GeneratedProtocolMessageType('SearchResultData', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHRESULTDATA,
  '__module__' : 'schema_pb2'
  # @@protoc_insertion_point(class_scope:milvus.proto.schema.SearchResultData)
  })
_sym_db.RegisterMessage(SearchResultData)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\016io.milvus.grpcB\013SchemaProtoP\001Z1github.com/milvus-io/milvus-proto/go-api/schemapb\240\001\001'
  _DATATYPE._serialized_start=1722
  _DATATYPE._serialized_end=1878
  _FIELDSTATE._serialized_start=1880
  _FIELDSTATE._serialized_end=1966
  _FIELDSCHEMA._serialized_start=52
  _FIELDSCHEMA._serialized_end=368
  _COLLECTIONSCHEMA._serialized_start=370
  _COLLECTIONSCHEMA._serialized_end=489
  _BOOLARRAY._serialized_start=491
  _BOOLARRAY._serialized_end=516
  _INTARRAY._serialized_start=518
  _INTARRAY._serialized_end=542
  _LONGARRAY._serialized_start=544
  _LONGARRAY._serialized_end=569
  _FLOATARRAY._serialized_start=571
  _FLOATARRAY._serialized_end=597
  _DOUBLEARRAY._serialized_start=599
  _DOUBLEARRAY._serialized_end=626
  _BYTESARRAY._serialized_start=628
  _BYTESARRAY._serialized_end=654
  _STRINGARRAY._serialized_start=656
  _STRINGARRAY._serialized_end=683
  _SCALARFIELD._serialized_start=686
  _SCALARFIELD._serialized_end=1088
  _VECTORFIELD._serialized_start=1090
  _VECTORFIELD._serialized_end=1206
  _FIELDDATA._serialized_start=1209
  _FIELDDATA._serialized_end=1418
  _IDS._serialized_start=1420
  _IDS._serialized_end=1539
  _SEARCHRESULTDATA._serialized_start=1542
  _SEARCHRESULTDATA._serialized_end=1719
# @@protoc_insertion_point(module_scope)
