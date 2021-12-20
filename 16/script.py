from functools import reduce


def convert_hex_to_bin(data):
    return "".join([f"{int(c, 16):>04b}" for c in data])


class Operation:

    def __init__(self, op_name):
        self.ops = {
            "sum": self._sum,
            "product": self._product,
            "minimum": self._minimum,
            "maximum": self._maximum,
            "gt": self._gt,
            "lt": self._lt,
            "eq": self._eq,
        }
        self.op_name = op_name

    def __str__(self):
        return f"Operation[{self.op_name}]"

    def __call__(self, values):
        return self.ops[self.op_name](values)

    def _sum(self, values):
        return sum(values)

    def _product(self, values):
        return reduce(lambda a, b: a * b, values)

    def _minimum(self, values):
        return min(values)

    def _maximum(self, values):
        return max(values)

    def _gt(self, values):
        assert len(values) == 2
        return int(values[0] > values[1])

    def _lt(self, values):
        assert len(values) == 2
        return int(values[0] < values[1])

    def _eq(self, values):
        assert len(values) == 2
        return int(values[0] == values[1])


class Packet:

    packet_types = {
        0: "sum",
        1: "product",
        2: "minimum",
        3: "maximum",
        4: "value",
        5: "gt",
        6: "lt",
        7: "eq"
    }

    def __init__(
        self,
        packet_version,
        type_id,
        value=None,
        subpackets=None,
        length_type_id=None
    ):
        self.packet_version = packet_version
        self.type_id = type_id
        self.subpackets = subpackets
        self.value = value

    @staticmethod
    def get_value(data):
        c = "1"
        value = ""
        while c == "1":
            segment = data[:5]
            data = data[5:]
            c = segment[0]
            value += segment[1:]
        return data, int(value, 2)

    @classmethod
    def packet_generator(cls, data, n_subpackets=0):
        packets = list()
        while data and "1" in data:

            packet_version = int(data[:3], 2)
            data = data[3:]

            type_id = int(data[:3], 2)
            type_id = cls.packet_types.get(type_id, str(type_id))
            data = data[3:]

            subpackets = list()
            value = None

            if type_id == "value":
                data, value = cls.get_value(data)
            else:
                length_type_id = int(data[:1], 2)
                data = data[1:]

                if length_type_id == 0:
                    bits = int(data[:15], 2)
                    data = data[15:]
                    _, subpackets = cls.packet_generator(data[:bits])
                    data = data[bits:]
                else:
                    n_packs = int(data[:11], 2)
                    data = data[11:]
                    data, subpackets = cls.packet_generator(data, n_packs)

            packet = Packet(
                packet_version=packet_version,
                type_id=type_id,
                value=value,
                subpackets=subpackets,
            )

            packets.append(packet)
            if n_subpackets > 0:
                if len(packets) == n_subpackets:
                    break

        return data, packets


def solve_part_1(packets):

    def get_sum(packet):
        value = packet.packet_version
        value += sum([get_sum(pckt) for pckt in packet.subpackets])
        return value

    return sum([get_sum(pckt) for pckt in packets])


def calculate(packets, op, ops=list()):
    
    values = []
    for pckt in packets:
        if pckt.value:
            values.append(pckt.value)
        else:
            ops.append(pckt.type_id)
            subop = Operation(pckt.type_id)
            value = calculate(pckt.subpackets, subop, ops)
            values.append(value)

    return op(values)


def solve_part_2(packets):
    pckt = packets[0]
    ops = [pckt.type_id]
    op = Operation(pckt.type_id)
    result = calculate(pckt.subpackets, op, ops)
    return result


def main():
    with open("input") as f:
        data = f.read().strip()

    data = convert_hex_to_bin(data)
    _, packets = Packet.packet_generator(data)

    print("Part 1:", solve_part_1(packets))
    print("Part 2:", solve_part_2(packets))


if __name__ == "__main__":
    main()
