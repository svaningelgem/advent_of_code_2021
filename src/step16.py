import io
import operator
from functools import reduce
from typing import Union


def decode_hex(txt: str) -> str:
    s = bin(int(txt.strip(), 16))[2:]  # strip '0b' in front of it.
    if len(s) % 8 != 0:  # Not exactly 8 positions
        s = s.zfill(8 * ((len(s) // 8) + 1))
    return s




class Packet:
    def __init__(self, packet: Union[io.StringIO, str]):
        if isinstance(packet, str):
            packet = io.StringIO(decode_hex(packet))

        self.version = int(packet.read(3), 2)
        self.packet_id = int(packet.read(3), 2)

        self.is_literal = self.packet_id == 4

        self._value = None
        self.sub_packets = []
        self.decode_contents(packet)

    def decode_contents(self, packet: io.StringIO):
        if self.is_literal:
            self.decode_literal(packet)
        else:
            self.decode_operator(packet)

    def decode_literal(self, packet: io.StringIO):
        should_stop = False
        literal = ''
        while not should_stop:
            current_value = packet.read(5)
            should_stop = current_value[0] == '0'
            literal += current_value[1:]
        self._value = int(literal, 2)

    def decode_operator(self, packet):
        length_type_id = packet.read(1)
        if length_type_id == '0':
            size_to_read = int(packet.read(15), 2)
            bits_to_interpret = packet.read(size_to_read)
            new_stream = io.StringIO(bits_to_interpret)
            while new_stream.tell() < size_to_read:
                self.sub_packets.append(Packet(new_stream))
        else:
            packets_to_read = int(packet.read(11), 2)
            for _ in range(packets_to_read):
                self.sub_packets.append(Packet(packet))

    @property
    def value(self) -> int:
        sub_packets_values = [x.value for x in self.sub_packets]

        if self.packet_id == 0:  # sum
            return sum(sub_packets_values)

        if self.packet_id == 1:  # product
            return reduce(operator.mul, sub_packets_values, 1)

        if self.packet_id == 2:  # min
            return min(sub_packets_values)

        if self.packet_id == 3:  # max
            return max(sub_packets_values)

        if self.packet_id == 4:  # -- literal
            return self._value

        if self.packet_id == 5:  # greater than
            assert len(sub_packets_values) == 2
            return 1 if sub_packets_values[0] > sub_packets_values[1] else 0

        if self.packet_id == 6:  # less than
            assert len(self.sub_packets) == 2
            return 1 if sub_packets_values[0] < sub_packets_values[1] else 0

        if self.packet_id == 7:  # equal
            assert len(self.sub_packets) == 2
            return 1 if sub_packets_values[0] == sub_packets_values[1] else 0


def get_version_sum(packet):
    total = 0

    packets_to_count = [Packet(packet)]
    while packets_to_count:
        current = packets_to_count.pop()
        total += current.version
        packets_to_count.extend(current.sub_packets)

    return total
