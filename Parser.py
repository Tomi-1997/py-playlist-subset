import random
import math


class Parser:
    def __init__(self):
        self.titles = []
        self.durations = []
        self.urls = []
        self.calculated = False
        self.res_printed = 0
        self.max_title = 0


    def add_entry(self, title: str, length: int, url: str):
        if isinstance(length, int):

            # For those extra long titles like ('From Movie XYZ, Starring Steve Carrel!')
            if '(' in title:
                title = title[0:title.find('(')]

            self.titles.append(title)
            self.durations.append(length)
            self.urls.append(url)
            self.calculated = False

            # For output formatting
            self.max_title = max(self.max_title, len(title))


    def print(self):
        print(self.titles)
        print(self.durations)

    def pre_search(self):
        self.avg = sum(self.durations) / len(self.durations)
        self.var = sum( [(x - self.avg) ** 2 for x in self.durations] ) / len(self.durations)
        self.std = math.sqrt(self.var)
        self.calculated = True
        self.res_printed = 0

    def search(self, T, EPS = 0, EPS_BIGGER = False):
        print("Seconds Requested: " + str(T))
        if not self.calculated:
            self.pre_search()

        # Approxmiate number of items needed to reach target
        approx = T / (self.avg)

        # High variance? try to include even less, or even more items
        plusminx = self.std / T

        # To Ints
        approx = int(approx)
        plusminx = int(plusminx)

        # Limits
        approx = max(approx, 1)
        plusminx = max(plusminx, 1)

        best_difference = math.inf
        indexes = [i for i in range(len(self.durations))]
        indexes_b = []
        for i in range(10000):
            num = approx + random.randint(-plusminx, plusminx)
            num = max(num, 1)

            # Random indexes
            # [0, 35, 8]
            ind = random.sample(indexes, num)

            # [0, 35, 8] -> duration[0] + duration[35] + duration[8]
            ind_s = 0
            for ind_i in ind:
                ind_s += self.durations[ind_i]

            # Distance from target
            diff = abs(ind_s - T)

            # Close Enough?
            if EPS != 0 and diff < EPS and (not EPS_BIGGER or ind_s > T):
                self.print_indexes_info(ind)

            # Closest?
            if EPS == 0 and diff < best_difference:
                best_difference = diff
                indexes_b = ind
                self.print_indexes_info(indexes_b)

        print(f'Finished, results printed: {self.res_printed}')

    def print_indexes_info(self, index_arr):
        for ind_i in index_arr:
            print(f'Duration: {self.durations[ind_i]}, Title: {self.titles[ind_i].ljust(self.max_title)}, Url: {self.urls[ind_i]}')
        ind_s = 0
        for ind_i in index_arr:
            ind_s += self.durations[ind_i]
        print(f'Seconds Overall: {ind_s}\n')
        self.res_printed += 1
