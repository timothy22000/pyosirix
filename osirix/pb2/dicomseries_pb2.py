# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dicomseries.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import osirix.pb2.utilities_pb2 as utilities__pb2
import osirix.pb2.types_pb2 as types__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dicomseries.proto',
  package='osirixgrpc',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11\x64icomseries.proto\x12\nosirixgrpc\x1a\x0futilities.proto\x1a\x0btypes.proto\"M\n\x18\x44icomSeriesPathsResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\r\n\x05paths\x18\x02 \x03(\t\"y\n!DicomSeriesPreviousSeriesResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x30\n\x0fprevious_series\x18\x02 \x01(\x0b\x32\x17.osirixgrpc.DicomSeries\"q\n\x1d\x44icomSeriesNextSeriesResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12,\n\x0bnext_series\x18\x02 \x01(\x0b\x32\x17.osirixgrpc.DicomSeries\"t\n\x1f\x44icomSeriesSortedImagesResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12-\n\rsorted_images\x18\x02 \x03(\x0b\x32\x16.osirixgrpc.DicomImage\"e\n\x18\x44icomSeriesStudyResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12%\n\x05study\x18\x02 \x01(\x0b\x32\x16.osirixgrpc.DicomStudy\"g\n\x19\x44icomSeriesImagesResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12&\n\x06images\x18\x02 \x03(\x0b\x32\x16.osirixgrpc.DicomImage\"g\n$DicomSeriesSeriesInstanceUIDResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x1b\n\x13series_instance_uid\x18\x02 \x01(\t\"h\n$DicomSeriesSeriesSOPClassUIDResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x1c\n\x14series_sop_class_uid\x18\x02 \x01(\t\"f\n$DicomSeriesSeriesDescriptionResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x1a\n\x12series_description\x18\x02 \x01(\t\"S\n\x1b\x44icomSeriesModalityResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x10\n\x08modality\x18\x02 \x01(\t\"K\n\x17\x44icomSeriesNameResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x0c\n\x04name\x18\x02 \x01(\t\"\xaa\x01\n\x17\x44icomSeriesDateResponse\x12\"\n\x06status\x18\x01 \x01(\x0b\x32\x12.osirixgrpc.Status\x12\x0c\n\x04year\x18\x02 \x01(\x05\x12\r\n\x05month\x18\x03 \x01(\x05\x12\x0b\n\x03\x64\x61y\x18\x04 \x01(\x05\x12\x0c\n\x04hour\x18\x05 \x01(\x05\x12\x0e\n\x06minute\x18\x06 \x01(\x05\x12\x0e\n\x06second\x18\x07 \x01(\x05\x12\x13\n\x0bmillisecond\x18\x08 \x01(\x05\x62\x06proto3'
  ,
  dependencies=[utilities__pb2.DESCRIPTOR,types__pb2.DESCRIPTOR,])




_DICOMSERIESPATHSRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesPathsResponse',
  full_name='osirixgrpc.DicomSeriesPathsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesPathsResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='paths', full_name='osirixgrpc.DicomSeriesPathsResponse.paths', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=63,
  serialized_end=140,
)


_DICOMSERIESPREVIOUSSERIESRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesPreviousSeriesResponse',
  full_name='osirixgrpc.DicomSeriesPreviousSeriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesPreviousSeriesResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='previous_series', full_name='osirixgrpc.DicomSeriesPreviousSeriesResponse.previous_series', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=142,
  serialized_end=263,
)


_DICOMSERIESNEXTSERIESRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesNextSeriesResponse',
  full_name='osirixgrpc.DicomSeriesNextSeriesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesNextSeriesResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='next_series', full_name='osirixgrpc.DicomSeriesNextSeriesResponse.next_series', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=265,
  serialized_end=378,
)


_DICOMSERIESSORTEDIMAGESRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesSortedImagesResponse',
  full_name='osirixgrpc.DicomSeriesSortedImagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesSortedImagesResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sorted_images', full_name='osirixgrpc.DicomSeriesSortedImagesResponse.sorted_images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=380,
  serialized_end=496,
)


_DICOMSERIESSTUDYRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesStudyResponse',
  full_name='osirixgrpc.DicomSeriesStudyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesStudyResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='study', full_name='osirixgrpc.DicomSeriesStudyResponse.study', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=498,
  serialized_end=599,
)


_DICOMSERIESIMAGESRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesImagesResponse',
  full_name='osirixgrpc.DicomSeriesImagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesImagesResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='images', full_name='osirixgrpc.DicomSeriesImagesResponse.images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=601,
  serialized_end=704,
)


_DICOMSERIESSERIESINSTANCEUIDRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesSeriesInstanceUIDResponse',
  full_name='osirixgrpc.DicomSeriesSeriesInstanceUIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesSeriesInstanceUIDResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='series_instance_uid', full_name='osirixgrpc.DicomSeriesSeriesInstanceUIDResponse.series_instance_uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=706,
  serialized_end=809,
)


_DICOMSERIESSERIESSOPCLASSUIDRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesSeriesSOPClassUIDResponse',
  full_name='osirixgrpc.DicomSeriesSeriesSOPClassUIDResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesSeriesSOPClassUIDResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='series_sop_class_uid', full_name='osirixgrpc.DicomSeriesSeriesSOPClassUIDResponse.series_sop_class_uid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=811,
  serialized_end=915,
)


_DICOMSERIESSERIESDESCRIPTIONRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesSeriesDescriptionResponse',
  full_name='osirixgrpc.DicomSeriesSeriesDescriptionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesSeriesDescriptionResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='series_description', full_name='osirixgrpc.DicomSeriesSeriesDescriptionResponse.series_description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=917,
  serialized_end=1019,
)


_DICOMSERIESMODALITYRESPONSE = _descriptor.Descriptor(
  name='DicomSeriesModalityResponse',
  full_name='osirixgrpc.DicomSeriesModalityResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesModalityResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='modality', full_name='osirixgrpc.DicomSeriesModalityResponse.modality', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1021,
  serialized_end=1104,
)


_DICOMSERIESNAMERESPONSE = _descriptor.Descriptor(
  name='DicomSeriesNameResponse',
  full_name='osirixgrpc.DicomSeriesNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesNameResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='osirixgrpc.DicomSeriesNameResponse.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=1106,
  serialized_end=1181,
)


_DICOMSERIESDATERESPONSE = _descriptor.Descriptor(
  name='DicomSeriesDateResponse',
  full_name='osirixgrpc.DicomSeriesDateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='osirixgrpc.DicomSeriesDateResponse.status', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='year', full_name='osirixgrpc.DicomSeriesDateResponse.year', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='month', full_name='osirixgrpc.DicomSeriesDateResponse.month', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='day', full_name='osirixgrpc.DicomSeriesDateResponse.day', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='hour', full_name='osirixgrpc.DicomSeriesDateResponse.hour', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='minute', full_name='osirixgrpc.DicomSeriesDateResponse.minute', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='second', full_name='osirixgrpc.DicomSeriesDateResponse.second', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='millisecond', full_name='osirixgrpc.DicomSeriesDateResponse.millisecond', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1184,
  serialized_end=1354,
)

_DICOMSERIESPATHSRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESPREVIOUSSERIESRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESPREVIOUSSERIESRESPONSE.fields_by_name['previous_series'].message_type = types__pb2._DICOMSERIES
_DICOMSERIESNEXTSERIESRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESNEXTSERIESRESPONSE.fields_by_name['next_series'].message_type = types__pb2._DICOMSERIES
_DICOMSERIESSORTEDIMAGESRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESSORTEDIMAGESRESPONSE.fields_by_name['sorted_images'].message_type = types__pb2._DICOMIMAGE
_DICOMSERIESSTUDYRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESSTUDYRESPONSE.fields_by_name['study'].message_type = types__pb2._DICOMSTUDY
_DICOMSERIESIMAGESRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESIMAGESRESPONSE.fields_by_name['images'].message_type = types__pb2._DICOMIMAGE
_DICOMSERIESSERIESINSTANCEUIDRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESSERIESSOPCLASSUIDRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESSERIESDESCRIPTIONRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESMODALITYRESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESNAMERESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
_DICOMSERIESDATERESPONSE.fields_by_name['status'].message_type = utilities__pb2._STATUS
DESCRIPTOR.message_types_by_name['DicomSeriesPathsResponse'] = _DICOMSERIESPATHSRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesPreviousSeriesResponse'] = _DICOMSERIESPREVIOUSSERIESRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesNextSeriesResponse'] = _DICOMSERIESNEXTSERIESRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesSortedImagesResponse'] = _DICOMSERIESSORTEDIMAGESRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesStudyResponse'] = _DICOMSERIESSTUDYRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesImagesResponse'] = _DICOMSERIESIMAGESRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesSeriesInstanceUIDResponse'] = _DICOMSERIESSERIESINSTANCEUIDRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesSeriesSOPClassUIDResponse'] = _DICOMSERIESSERIESSOPCLASSUIDRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesSeriesDescriptionResponse'] = _DICOMSERIESSERIESDESCRIPTIONRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesModalityResponse'] = _DICOMSERIESMODALITYRESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesNameResponse'] = _DICOMSERIESNAMERESPONSE
DESCRIPTOR.message_types_by_name['DicomSeriesDateResponse'] = _DICOMSERIESDATERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DicomSeriesPathsResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesPathsResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESPATHSRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesPathsResponse)
  })
_sym_db.RegisterMessage(DicomSeriesPathsResponse)

DicomSeriesPreviousSeriesResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesPreviousSeriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESPREVIOUSSERIESRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesPreviousSeriesResponse)
  })
_sym_db.RegisterMessage(DicomSeriesPreviousSeriesResponse)

DicomSeriesNextSeriesResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesNextSeriesResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESNEXTSERIESRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesNextSeriesResponse)
  })
_sym_db.RegisterMessage(DicomSeriesNextSeriesResponse)

DicomSeriesSortedImagesResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesSortedImagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESSORTEDIMAGESRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesSortedImagesResponse)
  })
_sym_db.RegisterMessage(DicomSeriesSortedImagesResponse)

DicomSeriesStudyResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesStudyResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESSTUDYRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesStudyResponse)
  })
_sym_db.RegisterMessage(DicomSeriesStudyResponse)

DicomSeriesImagesResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesImagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESIMAGESRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesImagesResponse)
  })
_sym_db.RegisterMessage(DicomSeriesImagesResponse)

DicomSeriesSeriesInstanceUIDResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesSeriesInstanceUIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESSERIESINSTANCEUIDRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesSeriesInstanceUIDResponse)
  })
_sym_db.RegisterMessage(DicomSeriesSeriesInstanceUIDResponse)

DicomSeriesSeriesSOPClassUIDResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesSeriesSOPClassUIDResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESSERIESSOPCLASSUIDRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesSeriesSOPClassUIDResponse)
  })
_sym_db.RegisterMessage(DicomSeriesSeriesSOPClassUIDResponse)

DicomSeriesSeriesDescriptionResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesSeriesDescriptionResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESSERIESDESCRIPTIONRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesSeriesDescriptionResponse)
  })
_sym_db.RegisterMessage(DicomSeriesSeriesDescriptionResponse)

DicomSeriesModalityResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesModalityResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESMODALITYRESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesModalityResponse)
  })
_sym_db.RegisterMessage(DicomSeriesModalityResponse)

DicomSeriesNameResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESNAMERESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesNameResponse)
  })
_sym_db.RegisterMessage(DicomSeriesNameResponse)

DicomSeriesDateResponse = _reflection.GeneratedProtocolMessageType('DicomSeriesDateResponse', (_message.Message,), {
  'DESCRIPTOR' : _DICOMSERIESDATERESPONSE,
  '__module__' : 'dicomseries_pb2'
  # @@protoc_insertion_point(class_scope:osirixgrpc.DicomSeriesDateResponse)
  })
_sym_db.RegisterMessage(DicomSeriesDateResponse)


# @@protoc_insertion_point(module_scope)
