# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: event-chain.proto
import sys

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2

from . import type_pb2 as type__pb2
_b = sys.version_info[0] < 3 and (
    lambda x: x
) or (lambda x: x.encode('latin1'))
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name='event-chain.proto',
    package='',
    syntax='proto3',
    serialized_options=None,
    serialized_pb=_b('\n\x11\x65vent-chain.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\ntype.proto\"\xb9\x02\n\tEventInfo\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\r\n\x05total\x18\x04 \x01(\r\x12\x1e\n\x07tickets\x18\x05 \x03(\x0b\x32\r.TicketHolder\x12.\n\nstart_time\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x14\n\x0cticket_price\x18\t \x01(\x04\x12\x14\n\x0cparticipants\x18\n \x03(\t\x12\x11\n\tremaining\x18\x0b \x01(\r\x12\x10\n\x08location\x18\x0c \x01(\t\x12*\n\nconsume_tx\x18\r \x01(\x0b\x32\x16.forge_abi.Transaction\"!\n\x0eUpdateHostedTx\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"U\n\x0fParticipantInfo\x12\x0e\n\x06hosted\x18\x01 \x03(\t\x12\x14\n\x0cparticipated\x18\x02 \x03(\t\x12\x0e\n\x06unused\x18\x03 \x03(\t\x12\x0c\n\x04used\x18\x04 \x03(\t\"@\n\nTicketInfo\x12\n\n\x02id\x18\x03 \x01(\r\x12\x15\n\revent_address\x18\x04 \x01(\t\x12\x0f\n\x07is_used\x18\x05 \x01(\x08\"\x8b\x01\n\x0cTicketHolder\x12-\n\rticket_create\x18\x01 \x01(\x0b\x32\x16.forge_abi.Transaction\x12/\n\x0fticket_exchange\x18\x02 \x01(\x0b\x32\x16.forge_abi.Transaction\x12\n\n\x02id\x18\x04 \x01(\r\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\tb\x06proto3'),
    dependencies=[
        google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR, type__pb2.DESCRIPTOR, ],
)


_EVENTINFO = _descriptor.Descriptor(
    name='EventInfo',
    full_name='EventInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='title', full_name='EventInfo.title', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='description', full_name='EventInfo.description', index=1,
            number=2, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='total', full_name='EventInfo.total', index=2,
            number=4, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='tickets', full_name='EventInfo.tickets', index=3,
            number=5, type=11, cpp_type=10, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='start_time', full_name='EventInfo.start_time', index=4,
            number=7, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='end_time', full_name='EventInfo.end_time', index=5,
            number=8, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='ticket_price', full_name='EventInfo.ticket_price', index=6,
            number=9, type=4, cpp_type=4, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='participants', full_name='EventInfo.participants', index=7,
            number=10, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='remaining', full_name='EventInfo.remaining', index=8,
            number=11, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='location', full_name='EventInfo.location', index=9,
            number=12, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='consume_tx', full_name='EventInfo.consume_tx', index=10,
            number=13, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
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
    serialized_start=67,
    serialized_end=380,
)


_UPDATEHOSTEDTX = _descriptor.Descriptor(
    name='UpdateHostedTx',
    full_name='UpdateHostedTx',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='address', full_name='UpdateHostedTx.address', index=0,
            number=1, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
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
    serialized_start=382,
    serialized_end=415,
)


_PARTICIPANTINFO = _descriptor.Descriptor(
    name='ParticipantInfo',
    full_name='ParticipantInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='hosted', full_name='ParticipantInfo.hosted', index=0,
            number=1, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='participated', full_name='ParticipantInfo.participated', index=1,
            number=2, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='unused', full_name='ParticipantInfo.unused', index=2,
            number=3, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='used', full_name='ParticipantInfo.used', index=3,
            number=4, type=9, cpp_type=9, label=3,
            has_default_value=False, default_value=[],
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
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
    serialized_start=417,
    serialized_end=502,
)


_TICKETINFO = _descriptor.Descriptor(
    name='TicketInfo',
    full_name='TicketInfo',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='id', full_name='TicketInfo.id', index=0,
            number=3, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='event_address', full_name='TicketInfo.event_address', index=1,
            number=4, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='is_used', full_name='TicketInfo.is_used', index=2,
            number=5, type=8, cpp_type=7, label=1,
            has_default_value=False, default_value=False,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
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
    serialized_start=504,
    serialized_end=568,
)


_TICKETHOLDER = _descriptor.Descriptor(
    name='TicketHolder',
    full_name='TicketHolder',
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name='ticket_create', full_name='TicketHolder.ticket_create', index=0,
            number=1, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='ticket_exchange', full_name='TicketHolder.ticket_exchange', index=1,
            number=2, type=11, cpp_type=10, label=1,
            has_default_value=False, default_value=None,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='id', full_name='TicketHolder.id', index=2,
            number=4, type=13, cpp_type=3, label=1,
            has_default_value=False, default_value=0,
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name='address', full_name='TicketHolder.address', index=3,
            number=5, type=9, cpp_type=9, label=1,
            has_default_value=False, default_value=_b("").decode('utf-8'),
            message_type=None, enum_type=None, containing_type=None,
            is_extension=False, extension_scope=None,
            serialized_options=None, file=DESCRIPTOR,
        ),
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
    serialized_start=571,
    serialized_end=710,
)

_EVENTINFO.fields_by_name['tickets'].message_type = _TICKETHOLDER
_EVENTINFO.fields_by_name['start_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTINFO.fields_by_name['end_time'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_EVENTINFO.fields_by_name['consume_tx'].message_type = type__pb2._TRANSACTION
_TICKETHOLDER.fields_by_name['ticket_create'].message_type = type__pb2._TRANSACTION
_TICKETHOLDER.fields_by_name['ticket_exchange'].message_type = type__pb2._TRANSACTION
DESCRIPTOR.message_types_by_name['EventInfo'] = _EVENTINFO
DESCRIPTOR.message_types_by_name['UpdateHostedTx'] = _UPDATEHOSTEDTX
DESCRIPTOR.message_types_by_name['ParticipantInfo'] = _PARTICIPANTINFO
DESCRIPTOR.message_types_by_name['TicketInfo'] = _TICKETINFO
DESCRIPTOR.message_types_by_name['TicketHolder'] = _TICKETHOLDER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventInfo = _reflection.GeneratedProtocolMessageType(
    'EventInfo', (_message.Message,), dict(
        DESCRIPTOR=_EVENTINFO,
        __module__='event_chain_pb2',
        # @@protoc_insertion_point(class_scope:EventInfo)
    ),
)
_sym_db.RegisterMessage(EventInfo)

UpdateHostedTx = _reflection.GeneratedProtocolMessageType(
    'UpdateHostedTx', (_message.Message,), dict(
        DESCRIPTOR=_UPDATEHOSTEDTX,
        __module__='event_chain_pb2',
        # @@protoc_insertion_point(class_scope:UpdateHostedTx)
    ),
)
_sym_db.RegisterMessage(UpdateHostedTx)

ParticipantInfo = _reflection.GeneratedProtocolMessageType(
    'ParticipantInfo', (_message.Message,), dict(
        DESCRIPTOR=_PARTICIPANTINFO,
        __module__='event_chain_pb2',
        # @@protoc_insertion_point(class_scope:ParticipantInfo)
    ),
)
_sym_db.RegisterMessage(ParticipantInfo)

TicketInfo = _reflection.GeneratedProtocolMessageType(
    'TicketInfo', (_message.Message,), dict(
        DESCRIPTOR=_TICKETINFO,
        __module__='event_chain_pb2',
        # @@protoc_insertion_point(class_scope:TicketInfo)
    ),
)
_sym_db.RegisterMessage(TicketInfo)

TicketHolder = _reflection.GeneratedProtocolMessageType(
    'TicketHolder', (_message.Message,), dict(
        DESCRIPTOR=_TICKETHOLDER,
        __module__='event_chain_pb2',
        # @@protoc_insertion_point(class_scope:TicketHolder)
    ),
)
_sym_db.RegisterMessage(TicketHolder)


# @@protoc_insertion_point(module_scope)