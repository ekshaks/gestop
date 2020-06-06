# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/landmarkList.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/landmarkList.proto',
  package='hand_tracking',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18proto/landmarkList.proto\x12\rhand_tracking\"\x87\x01\n\x0cLandmarkList\x12\x36\n\x08landmark\x18\x01 \x03(\x0b\x32$.hand_tracking.LandmarkList.Landmark\x12\x12\n\nhandedness\x18\x02 \x01(\x08\x1a+\n\x08Landmark\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\x62\x06proto3'
)




_LANDMARKLIST_LANDMARK = _descriptor.Descriptor(
  name='Landmark',
  full_name='hand_tracking.LandmarkList.Landmark',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='hand_tracking.LandmarkList.Landmark.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='hand_tracking.LandmarkList.Landmark.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='hand_tracking.LandmarkList.Landmark.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=136,
  serialized_end=179,
)

_LANDMARKLIST = _descriptor.Descriptor(
  name='LandmarkList',
  full_name='hand_tracking.LandmarkList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='landmark', full_name='hand_tracking.LandmarkList.landmark', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='handedness', full_name='hand_tracking.LandmarkList.handedness', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_LANDMARKLIST_LANDMARK, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=179,
)

_LANDMARKLIST_LANDMARK.containing_type = _LANDMARKLIST
_LANDMARKLIST.fields_by_name['landmark'].message_type = _LANDMARKLIST_LANDMARK
DESCRIPTOR.message_types_by_name['LandmarkList'] = _LANDMARKLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LandmarkList = _reflection.GeneratedProtocolMessageType('LandmarkList', (_message.Message,), {

  'Landmark' : _reflection.GeneratedProtocolMessageType('Landmark', (_message.Message,), {
    'DESCRIPTOR' : _LANDMARKLIST_LANDMARK,
    '__module__' : 'proto.landmarkList_pb2'
    # @@protoc_insertion_point(class_scope:hand_tracking.LandmarkList.Landmark)
    })
  ,
  'DESCRIPTOR' : _LANDMARKLIST,
  '__module__' : 'proto.landmarkList_pb2'
  # @@protoc_insertion_point(class_scope:hand_tracking.LandmarkList)
  })
_sym_db.RegisterMessage(LandmarkList)
_sym_db.RegisterMessage(LandmarkList.Landmark)


# @@protoc_insertion_point(module_scope)
