# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stream.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cstream.proto\"3\n\x0cHelloRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x15\n\rnum_greetings\x18\x02 \x01(\x05\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2:\n\x0cMultiGreeter\x12*\n\x08sayHello\x12\r.HelloRequest\x1a\x0b.HelloReply\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'stream_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=16
  _globals['_HELLOREQUEST']._serialized_end=67
  _globals['_HELLOREPLY']._serialized_start=69
  _globals['_HELLOREPLY']._serialized_end=98
  _globals['_MULTIGREETER']._serialized_start=100
  _globals['_MULTIGREETER']._serialized_end=158
# @@protoc_insertion_point(module_scope)
