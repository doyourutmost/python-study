# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: helloworld.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10helloworld.proto\"3\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rnum_greetings\x18\x02 \x01(\t\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2:\n\x0cMultiGreeter\x12*\n\x08sayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x30\x01\x42\tZ\x07.;protob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'helloworld_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  _globals['DESCRIPTOR']._options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\007.;proto'
  _globals['_HELLOREQUEST']._serialized_start=20
  _globals['_HELLOREQUEST']._serialized_end=71
  _globals['_HELLOREPLY']._serialized_start=73
  _globals['_HELLOREPLY']._serialized_end=102
  _globals['_MULTIGREETER']._serialized_start=104
  _globals['_MULTIGREETER']._serialized_end=162
# @@protoc_insertion_point(module_scope)
