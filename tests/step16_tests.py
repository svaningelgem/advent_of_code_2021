from pathlib import Path

from step16 import decode_hex, Packet, get_version_sum

TEST_INPUT = Path(__file__).parent / 'step16.txt'
REAL_INPUT = Path(__file__).parent.parent / 'src/step16.txt'


def test_step16():
    assert decode_hex('D2FE28') == '110100101111111000101000'
    assert decode_hex('38006F45291200') == '00111000000000000110111101000101001010010001001000000000'
    assert decode_hex('EE00D40C823060') == '11101110000000001101010000001100100000100011000001100000'

    sut = Packet('D2FE28')
    assert sut.version == 6
    assert sut.packet_id == 4
    assert sut.is_literal
    assert sut._value == 2021

    sut = Packet('38006F45291200')
    assert sut.version == 1
    assert sut.packet_id == 6
    assert not sut.is_literal
    assert sut._value is None
    assert len(sut.sub_packets) == 2
    assert sut.sub_packets[0]._value == 10
    assert sut.sub_packets[1]._value == 20

    sut = Packet('EE00D40C823060')
    assert sut.version == 7
    assert sut.packet_id == 3
    assert not sut.is_literal
    assert sut._value is None
    assert len(sut.sub_packets) == 3
    assert sut.sub_packets[0]._value == 1
    assert sut.sub_packets[1]._value == 2
    assert sut.sub_packets[2]._value == 3

    assert get_version_sum('8A004A801A8002F478') == 16
    assert get_version_sum('620080001611562C8802118E34') == 12
    assert get_version_sum('C0015000016115A2E0802F182340') == 23
    assert get_version_sum('A0016C880162017C3686B18A3D4780') == 31


def test_step16_real_data():
    assert get_version_sum(REAL_INPUT.read_text()) == 879


def test_step16_part2():
    assert Packet('C200B40A82').value == 3
    assert Packet('04005AC33890').value == 54
    assert Packet('880086C3E88112').value == 7
    assert Packet('CE00C43D881120').value == 9
    assert Packet('D8005AC2A8F0').value == 1
    assert Packet('F600BC2D8F').value == 0
    assert Packet('9C005AC2F8F0').value == 0
    assert Packet('9C0141080250320F1802104A08').value == 1


def test_step16_part2_real_data():
    assert Packet(REAL_INPUT.read_text()).value == 539051801941
