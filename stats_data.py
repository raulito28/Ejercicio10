import statistics as st


class StatsData:
    def __init__(self, lista):
        self.l_data = lista
        self.mean = st.mean(lista)
        self.median = st.median(self.l_data)
        self.variance = st.variance(lista)
