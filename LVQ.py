class model(object):

    def __init__(self):
        """
        Inisialisasi class (constructor)
        :min (array): Data minimum
        :max (array): Data maximum
        :label (array): Label data
        :bobot (array): Bobot data
        """

        self.min = [2, 5, 6, 9.47, 15.40, 4.37, 20.76]
        self.max = [136, 145, 205, 42.92, 99.65, 8.75, 271.32]
        
        self.bobot = [[0.51960041, 0.29535686, 0.17398024, 0.39742447, 0.79136829,
        0.55574885, 0.94646941],
       [0.5481731 , 0.27255562, 0.05880831, 0.39245013, 0.57166096,
        0.42937728, 0.26799873],
       [0.27844395, 0.46015617, 0.38354912, 0.30264184, 0.01468563,
        0.45950717, 0.24101461],
       [0.17745401, 0.39744164, 0.0746021 , 0.29141671, 0.0559883 ,
        0.33549181, 0.36431371],
       [0.21049004, 0.47259936, 0.0791285 , 0.58913546, 0.39608968,
        0.34658478, 0.52111898],
       [0.18216123, 0.34892531, 0.06030708, 0.55587112, 0.42428988,
        0.82889699, 0.14319505],
       [0.14381091, 0.369938  , 0.07350924, 0.57889131, 0.82850461,
        0.5889982 , 0.10521353],
       [0.32400528, 0.45794502, 0.04694031, 0.65720585, 0.55084997,
        0.67309343, 0.24776019],
       [0.12867096, 0.49880427, 0.0611555 , 0.40107903, 0.59595565,
        0.60914402, 0.10579218],
       [0.13031964, 0.09660164, 0.22043063, 0.35232786, 0.8713593 ,
        0.48355157, 0.3347107 ],
       [0.66630957, 0.59336023, 0.23522704, 0.52259519, 0.78473274,
        0.3678178 , 0.33223293],
       [0.14383926, 0.09184971, 0.13102044, 0.68951984, 0.41747537,
        0.27665562, 0.32847903],
       [0.17562558, 0.8882161 , 0.97153333, 0.79582336, 0.79431139,
        0.34352782, 0.19794904],
       [0.68242086, 0.12992479, 0.22276183, 0.47932085, 0.84269263,
        0.48635491, 0.12568735],
       [0.75701314, 0.13635248, 0.22185047, 0.58990257, 0.92029317,
        0.44261492, 0.01305237],
       [0.14120789, 0.91756349, 0.9939359 , 0.406742  , 0.93552776,
        0.34552959, 0.39727848],
       [0.09933643, 0.07184184, 0.01990075, 0.41497889, 0.90792412,
        0.69373026, 0.3635956 ],
       [0.39931911, 0.41051175, 0.2138201 , 0.80384929, 0.90870339,
        0.57078457, 0.67558329],
       [0.12934373, 0.06592468, 0.13261426, 0.53703606, 0.94469433,
        0.32953995, 0.60812968],
       [0.89250211, 0.27525857, 0.07281252, 0.45646583, 0.77479591,
        0.57404606, 0.26733202],
       [0.58114161, 0.23604086, 0.17230946, 0.45199751, 0.76967223,
        0.46944961, 0.65738547],
       [0.79810715, 0.16208719, 0.11530894, 0.42999708, 0.45686099,
        0.56040897, 0.49726977]]

        self.label = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

    def normalisasi(self, data):
        """
        Proses normalisasi data
        :param data (array): Data
        :return: Data yang telah di normalisasi
        """
        
        for i in range(len(data)):
            data[i] = (data[i] - self.min[i]) / (self.max[i] - self.min[i])
            
        return data

    def predict(self, data):
        """
        Proses prediksi data
        :param data (array): Data
        :return: Data yang telah di prediksi
        """

        data = self.normalisasi(data)
        min_distance = float("inf")
        min_index = 0
        for i in range(len(self.bobot)):
            distance = 0
            for j in range(len(data)):
                distance += (data[j] - self.bobot[i][j]) ** 2
            if distance < min_distance:
                min_distance = distance
                min_index = i

        return self.label[min_index]