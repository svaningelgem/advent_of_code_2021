from pathlib import Path


class BingoSystem:
    def __init__(self, file):
        self.bords = []

        txt = Path(file).read_text().splitlines()

        self.numbers = [int(x) for x in txt[0].split(',')]
        self.read_bords(txt)

    def read_bords(self, txt):
        current_line = 0
        bord = []
        while True:
            current_line += 1
            if current_line >= len(txt):
                break

            if not txt[current_line].strip():  # Empty line
                if bord:
                    self.bords.append(bord)
                    bord = []
                continue

            bord.extend(int(x) for x in txt[current_line].split(' ') if x)

        if bord:
            self.bords.append(bord)

    def _has_won_horizontal(self, bord, nr_list):
        for i in range(5):
            if all(x in nr_list for x in bord[i*5:i*5+5]):
                return True
        return False

    def _has_won_vertical(self, bord, nr_list):
        for i in range(5):
            if all(x in nr_list for x in bord[i::5]):
                return True
        return False

    def _has_won(self, bord, nr_list):
        return (
            self._has_won_horizontal(bord, nr_list)
            or self._has_won_vertical(bord, nr_list)
        )

    def find_winning_bord(self):
        drawn_nr_list = []
        for nr in self.numbers:
            drawn_nr_list.append(nr)
            for bord in self.bords:
                if self._has_won(bord, drawn_nr_list):
                    return nr * sum(set(bord) - set(drawn_nr_list))

        raise ValueError("BOOM")

    def find_loosing_bord(self):
        drawn_nr_list = []
        bord_has_won = []
        for nr in self.numbers:
            drawn_nr_list.append(nr)
            for bord_idx, bord in enumerate(self.bords):
                if bord_idx in bord_has_won:
                    continue

                if self._has_won(bord, drawn_nr_list):
                    bord_has_won.append(bord_idx)
                    if len(bord_has_won) == len(self.bords):  # Last bord to win
                        return nr * sum(set(bord) - set(drawn_nr_list))

        raise ValueError("BOOM")


a = 1