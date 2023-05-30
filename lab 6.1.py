import warnings
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings("ignore")

data = [
    [0.02, 0.0371, 0.0428, 0.0207, 0.0954, 0.0986, 0.1539, 0.1601, 0.3109, 0.2111, 0.1609, 0.1582, 0.2238, 0.0645,
     0.066, 0],
    [0.0453, 0.0523, 0.0843, 0.0689, 0.1183, 0.2583, 0.2156, 0.3481, 0.3337, 0.2872, 0.4918, 0.6552, 0.6919, 0.7797,
     0.7464, 0],
    [0.0262, 0.0582, 0.1099, 0.1083, 0.0974, 0.228, 0.2431, 0.3771, 0.5598, 0.6194, 0.6333, 0.706, 0.5544, 0.532,
     0.6479, 0],
    [0.01, 0.0171, 0.0623, 0.0205, 0.0205, 0.0368, 0.1098, 0.1276, 0.0598, 0.1264, 0.0881, 0.1992, 0.0184, 0.2261,
     0.1729, 0],
    [0.0762, 0.0666, 0.0481, 0.0394, 0.059, 0.0649, 0.1209, 0.2467, 0.3564, 0.4459, 0.4152, 0.3952, 0.4256, 0.4135,
     0.4528, 0],
    [0.0286, 0.0453, 0.0277, 0.0174, 0.0384, 0.099, 0.1201, 0.1833, 0.2105, 0.3039, 0.2988, 0.425, 0.6343, 0.8198,
     1.0, 0],
    [0.0317, 0.0956, 0.1321, 0.1408, 0.1674, 0.171, 0.0731, 0.1401, 0.2083, 0.3513, 0.1786, 0.0658, 0.0513, 0.3752,
     0.5419, 0],
    [0.0519, 0.0548, 0.0842, 0.0319, 0.1158, 0.0922, 0.1027, 0.0613, 0.1465, 0.2838, 0.2802, 0.3086, 0.2657, 0.3801,
     0.5626, 0],
    [0.0223, 0.0375, 0.0484, 0.0475, 0.0647, 0.0591, 0.0753, 0.0098, 0.0684, 0.1487, 0.1156, 0.1654, 0.3833, 0.3598,
     0.1713, 0],
    [0.0164, 0.0173, 0.0347, 0.007, 0.0187, 0.0671, 0.1056, 0.0697, 0.0962, 0.0251, 0.0801, 0.1056, 0.1266, 0.089,
     0.0198, 0],
    [0.0039, 0.0063, 0.0152, 0.0336, 0.031, 0.0284, 0.0396, 0.0272, 0.0323, 0.0452, 0.0492, 0.0996, 0.1424, 0.1194,
     0.0628, 0],
    [0.0123, 0.0309, 0.0169, 0.0313, 0.0358, 0.0102, 0.0182, 0.0579, 0.1122, 0.0835, 0.0548, 0.0847, 0.2026, 0.2557,
     0.187, 0],
    [0.0079, 0.0086, 0.0055, 0.025, 0.0344, 0.0546, 0.0528, 0.0958, 0.1009, 0.124, 0.1097, 0.1215, 0.1874, 0.3383,
     0.3227, 0],
    [0.009, 0.0062, 0.0253, 0.0489, 0.1197, 0.1589, 0.1392, 0.0987, 0.0955, 0.1895, 0.1896, 0.2547, 0.4073, 0.2988,
     0.2901, 0],
    [0.0124, 0.0433, 0.0604, 0.0449, 0.0597, 0.0355, 0.0531, 0.0343, 0.1052, 0.212, 0.164, 0.1901, 0.3026, 0.2019,
     0.0592, 0],
    [0.0298, 0.0615, 0.065, 0.0921, 0.1615, 0.2294, 0.2176, 0.2033, 0.1459, 0.0852, 0.2476, 0.3645, 0.2777, 0.2826,
     0.3237, 0],
    [0.0352, 0.0116, 0.0191, 0.0469, 0.0737, 0.1185, 0.1683, 0.1541, 0.1466, 0.2912, 0.2328, 0.2237, 0.247, 0.156,
     0.3491, 0],
    [0.0192, 0.0607, 0.0378, 0.0774, 0.1388, 0.0809, 0.0568, 0.0219, 0.1037, 0.1186, 0.1237, 0.1601, 0.352, 0.4479,
     0.3769, 0],
    [0.027, 0.0092, 0.0145, 0.0278, 0.0412, 0.0757, 0.1026, 0.1138, 0.0794, 0.152, 0.1675, 0.137, 0.1361, 0.1345,
     0.2144, 0],
    [0.0126, 0.0149, 0.0641, 0.1732, 0.2565, 0.2559, 0.2947, 0.411, 0.4983, 0.592, 0.5832, 0.5419, 0.5472, 0.5314,
     0.4981, 0],
    [0.0473, 0.0509, 0.0819, 0.1252, 0.1783, 0.307, 0.3008, 0.2362, 0.383, 0.3759, 0.3021, 0.2909, 0.2301, 0.1411,
     0.1582, 0],
    [0.0664, 0.0575, 0.0842, 0.0372, 0.0458, 0.0771, 0.0771, 0.113, 0.2353, 0.1838, 0.2869, 0.4129, 0.3647, 0.1984,
     0.284, 0],
    [0.0099, 0.0484, 0.0299, 0.0297, 0.0652, 0.1077, 0.2363, 0.2385, 0.0075, 0.1882, 0.1456, 0.1892, 0.3176, 0.134,
     0.2169, 0],
    [0.0115, 0.015, 0.0136, 0.0076, 0.0211, 0.1058, 0.1023, 0.044, 0.0931, 0.0734, 0.074, 0.0622, 0.1055, 0.1183,
     0.1721, 0],
    [0.0293, 0.0644, 0.039, 0.0173, 0.0476, 0.0816, 0.0993, 0.0315, 0.0736, 0.086, 0.0414, 0.0472, 0.0835, 0.0938,
     0.1466, 0],
    [0.0201, 0.0026, 0.0138, 0.0062, 0.0133, 0.0151, 0.0541, 0.021, 0.0505, 0.1097, 0.0841, 0.0942, 0.1204, 0.042,
     0.0031, 0],
    [0.0151, 0.032, 0.0599, 0.105, 0.1163, 0.1734, 0.1679, 0.1119, 0.0889, 0.1205, 0.0847, 0.1518, 0.2305, 0.2793,
     0.3404, 0],
    [0.0177, 0.03, 0.0288, 0.0394, 0.063, 0.0526, 0.0688, 0.0633, 0.0624, 0.0613, 0.168, 0.3476, 0.4561, 0.5188,
     0.6308, 0],
    [0.01, 0.0275, 0.019, 0.0371, 0.0416, 0.0201, 0.0314, 0.0651, 0.1896, 0.2668, 0.3376, 0.3282, 0.2432, 0.1268,
     0.1278, 0],
    [0.0189, 0.0308, 0.0197, 0.0622, 0.008, 0.0789, 0.144, 0.1451, 0.1789, 0.2522, 0.2607, 0.371, 0.3906, 0.2672,
     0.2716, 0],
    [0.024, 0.0218, 0.0324, 0.0569, 0.033, 0.0513, 0.0897, 0.0713, 0.0569, 0.0389, 0.1934, 0.2434, 0.2906, 0.2606,
     0.3811, 0],
    [0.0084, 0.0153, 0.0291, 0.0432, 0.0951, 0.0752, 0.0414, 0.0259, 0.0692, 0.1753, 0.197, 0.1167, 0.1683, 0.0814,
     0.2179, 0],
    [0.0195, 0.0213, 0.0058, 0.019, 0.0319, 0.0571, 0.1004, 0.0668, 0.0691, 0.0242, 0.0728, 0.0639, 0.3002, 0.3854,
     0.4767, 0],
    [0.0442, 0.0477, 0.0049, 0.0581, 0.0278, 0.0678, 0.1664, 0.149, 0.0974, 0.1268, 0.1109, 0.2375, 0.2007, 0.214,
     0.1109, 0],
    [0.0311, 0.0491, 0.0692, 0.0831, 0.0079, 0.02, 0.0981, 0.1016, 0.2025, 0.0767, 0.1767, 0.2555, 0.2812, 0.2722,
     0.3227, 0],
    [0.0206, 0.0132, 0.0533, 0.0569, 0.0647, 0.1432, 0.1344, 0.2041, 0.1571, 0.1573, 0.2327, 0.1785, 0.1507, 0.1916,
     0.2061, 0],
    [0.0094, 0.0166, 0.0398, 0.0359, 0.0681, 0.0706, 0.102, 0.0893, 0.0381, 0.1328, 0.1303, 0.0273, 0.0644, 0.0712,
     0.1204, 0],
    [0.0333, 0.0221, 0.027, 0.0481, 0.0679, 0.0981, 0.0843, 0.1172, 0.0759, 0.092, 0.1475, 0.0522, 0.1119, 0.097,
     0.1174, 0],
    [0.0123, 0.0022, 0.0196, 0.0206, 0.018, 0.0492, 0.0033, 0.0398, 0.0791, 0.0475, 0.1152, 0.052, 0.1192, 0.1943,
     0.184, 0],
    [0.0091, 0.0213, 0.0206, 0.0505, 0.0657, 0.0795, 0.097, 0.0872, 0.0743, 0.0837, 0.1579, 0.0898, 0.0309, 0.1856,
     0.2969, 0],
    [0.0068, 0.0232, 0.0513, 0.0444, 0.0249, 0.0637, 0.0422, 0.113, 0.1911, 0.2475, 0.1606, 0.0922, 0.2398, 0.322,
     0.4295, 0],
    [0.0093, 0.0185, 0.0056, 0.0064, 0.026, 0.0458, 0.047, 0.0057, 0.0425, 0.064, 0.0888, 0.1599, 0.1541, 0.2768,
     0.2176, 0],
    [0.0211, 0.0319, 0.0415, 0.0286, 0.0121, 0.0438, 0.1299, 0.139, 0.0695, 0.0568, 0.0869, 0.1935, 0.1478, 0.1871,
     0.1994, 0],
    [0.0093, 0.0269, 0.0217, 0.0339, 0.0305, 0.1172, 0.145, 0.0638, 0.074, 0.136, 0.2132, 0.3738, 0.3738, 0.2673,
     0.2333, 0],
    [0.0257, 0.0447, 0.0388, 0.0239, 0.1315, 0.1323, 0.1608, 0.2145, 0.0847, 0.0561, 0.0891, 0.0861, 0.1531, 0.1524,
     0.1849, 0],
    [0.0408, 0.0653, 0.0397, 0.0604, 0.0496, 0.1817, 0.1178, 0.1024, 0.0583, 0.2176, 0.2459, 0.3332, 0.3087, 0.2613,
     0.3232, 0],
    [0.0308, 0.0339, 0.0202, 0.0889, 0.157, 0.175, 0.092, 0.1353, 0.1593, 0.2795, 0.3336, 0.294, 0.1608, 0.3335,
     0.4985, 0],
    [0.0373, 0.0281, 0.0232, 0.0225, 0.0179, 0.0733, 0.0841, 0.1031, 0.0993, 0.0802, 0.1564, 0.2565, 0.2624, 0.1179,
     0.0597, 0],
    [0.019, 0.0038, 0.0642, 0.0452, 0.0333, 0.069, 0.0901, 0.1454, 0.074, 0.0349, 0.1459, 0.3473, 0.3197, 0.2823,
     0.0166, 0],
    [0.0119, 0.0582, 0.0623, 0.06, 0.1397, 0.1883, 0.1422, 0.1447, 0.0487, 0.0864, 0.2143, 0.372, 0.2665, 0.2113,
     0.1103, 0],
    [0.0353, 0.0713, 0.0326, 0.0272, 0.037, 0.0792, 0.1083, 0.0687, 0.0298, 0.088, 0.1078, 0.0979, 0.225, 0.2819,
     0.2099, 0],
    [0.0131, 0.0068, 0.0308, 0.0311, 0.0085, 0.0767, 0.0771, 0.064, 0.0726, 0.0901, 0.075, 0.0844, 0.1226, 0.1619,
     0.2317, 0],
    [0.0087, 0.0046, 0.0081, 0.023, 0.0586, 0.0682, 0.0993, 0.0717, 0.0576, 0.0818, 0.1315, 0.1862, 0.2789, 0.2579,
     0.224, 0],
    [0.0293, 0.0378, 0.0257, 0.0062, 0.013, 0.0612, 0.0895, 0.1107, 0.0973, 0.0751, 0.0528, 0.1209, 0.1763, 0.2039,
     0.2727, 0],
    [0.0132, 0.008, 0.0188, 0.0141, 0.0436, 0.0668, 0.0609, 0.0131, 0.0899, 0.0922, 0.1445, 0.1475, 0.2087, 0.2558,
     0.2603, 0],
    [0.0201, 0.0116, 0.0123, 0.0245, 0.0547, 0.0208, 0.0891, 0.0836, 0.1335, 0.1199, 0.1742, 0.1387, 0.2042, 0.258,
     0.2616, 0],
    [0.0152, 0.0102, 0.0113, 0.0263, 0.0097, 0.0391, 0.0857, 0.0915, 0.0949, 0.1504, 0.1911, 0.2115, 0.2249, 0.2573,
     0.1701, 0],
    [0.0216, 0.0124, 0.0174, 0.0152, 0.0608, 0.1026, 0.1139, 0.0877, 0.116, 0.0866, 0.1564, 0.078, 0.0997, 0.0915,
     0.0662, 0],
    [0.0225, 0.0019, 0.0075, 0.0097, 0.0445, 0.0906, 0.0889, 0.0655, 0.1624, 0.1452, 0.1442, 0.0948, 0.0618, 0.1641,
     0.0708, 0],
    [0.0125, 0.0152, 0.0218, 0.0175, 0.0362, 0.0696, 0.0873, 0.0616, 0.1252, 0.1302, 0.0888, 0.05, 0.0628, 0.1274,
     0.0801, 0],
    [0.013, 0.0006, 0.0088, 0.0456, 0.0525, 0.0778, 0.0931, 0.0941, 0.1711, 0.1483, 0.1532, 0.11, 0.089, 0.1236,
     0.1197, 0],
    [0.0135, 0.0045, 0.0051, 0.0289, 0.0561, 0.0929, 0.1031, 0.0883, 0.1596, 0.1908, 0.1576, 0.1112, 0.1197, 0.1174,
     0.1415, 0],
    [0.0086, 0.0215, 0.0242, 0.0445, 0.0667, 0.0771, 0.0499, 0.0906, 0.1229, 0.1185, 0.0775, 0.1101, 0.1042, 0.0853,
     0.0456, 0],
    [0.0067, 0.0096, 0.0024, 0.0058, 0.0197, 0.0618, 0.0432, 0.0951, 0.0836, 0.118, 0.0978, 0.0909, 0.0656, 0.0593,
     0.0832, 0],
    [0.0071, 0.0103, 0.0135, 0.0494, 0.0253, 0.0806, 0.0701, 0.0738, 0.0117, 0.0898, 0.0289, 0.1554, 0.1437, 0.1035,
     0.1424, 0],
    [0.0176, 0.0172, 0.0501, 0.0285, 0.0262, 0.0351, 0.0362, 0.0535, 0.0258, 0.0474, 0.0526, 0.1854, 0.104, 0.0948,
     0.0912, 0],
    [0.0265, 0.044, 0.0137, 0.0084, 0.0305, 0.0438, 0.0341, 0.078, 0.0844, 0.0779, 0.0327, 0.206, 0.1908, 0.1065,
     0.1457, 0],
    [0.0368, 0.0403, 0.0317, 0.0293, 0.082, 0.1342, 0.1161, 0.0663, 0.0155, 0.0506, 0.0906, 0.2545, 0.1464, 0.1272,
     0.1223, 0],
    [0.0195, 0.0142, 0.0181, 0.0406, 0.0391, 0.0249, 0.0892, 0.0973, 0.084, 0.1191, 0.1522, 0.1322, 0.1434, 0.1244,
     0.0653, 0],
    [0.0216, 0.0215, 0.0273, 0.0139, 0.0357, 0.0785, 0.0906, 0.0908, 0.1151, 0.0973, 0.1203, 0.1102, 0.1192, 0.1762,
     0.239, 0],
    [0.0065, 0.0122, 0.0068, 0.0108, 0.0217, 0.0284, 0.0527, 0.0575, 0.1054, 0.1109, 0.0937, 0.0827, 0.092, 0.0911,
     0.1487, 0],
    [0.0036, 0.0078, 0.0092, 0.0387, 0.053, 0.1197, 0.1243, 0.1026, 0.1239, 0.0888, 0.0937, 0.1245, 0.1599, 0.1542,
     0.1846, 0],
    [0.0208, 0.0186, 0.0131, 0.0211, 0.061, 0.0613, 0.0612, 0.0506, 0.0989, 0.1093, 0.1063, 0.1179, 0.1291, 0.1591,
     0.168, 0],
    [0.0139, 0.0222, 0.0089, 0.0108, 0.0215, 0.0136, 0.0659, 0.0954, 0.0786, 0.1015, 0.1261, 0.0828, 0.0493, 0.0848,
     0.1514, 0],
    [0.0109, 0.0093, 0.0121, 0.0378, 0.0679, 0.0863, 0.1004, 0.0664, 0.0941, 0.1036, 0.0972, 0.0501, 0.1546, 0.3404,
     0.4804, 0],
    [0.0202, 0.0104, 0.0325, 0.0239, 0.0807, 0.1529, 0.1154, 0.0608, 0.1317, 0.137, 0.0843, 0.0269, 0.1254, 0.3046,
     0.5584, 0],
    [0.0239, 0.0189, 0.0466, 0.044, 0.0657, 0.0742, 0.138, 0.1099, 0.1384, 0.1376, 0.0938, 0.0259, 0.1499, 0.2851,
     0.5743, 0],
    [0.0336, 0.0294, 0.0476, 0.0539, 0.0794, 0.0804, 0.1136, 0.1228, 0.1235, 0.0842, 0.0357, 0.0689, 0.1705, 0.3257,
     0.4602, 0],
    [0.0231, 0.0351, 0.003, 0.0304, 0.0339, 0.086, 0.1738, 0.1351, 0.1063, 0.0347, 0.0575, 0.1382, 0.2274, 0.4038,
     0.5223, 0],
    [0.0108, 0.0086, 0.0058, 0.046, 0.0752, 0.0887, 0.1015, 0.0494, 0.0472, 0.0393, 0.1106, 0.1412, 0.2202, 0.2976,
     0.4116, 0],
    [0.0229, 0.0369, 0.004, 0.0375, 0.0455, 0.1452, 0.2211, 0.1188, 0.075, 0.1631, 0.2709, 0.3358, 0.4091, 0.44,
     0.5485, 0],
    [0.01, 0.0194, 0.0155, 0.0489, 0.0839, 0.1009, 0.1627, 0.2071, 0.2696, 0.299, 0.3242, 0.3565, 0.3951, 0.5201,
     0.6953, 0],
    [0.0409, 0.0421, 0.0573, 0.013, 0.0183, 0.1019, 0.1054, 0.107, 0.2302, 0.2259, 0.2373, 0.3323, 0.3827, 0.484,
     0.6812, 0],
    [0.0217, 0.034, 0.0392, 0.0236, 0.1081, 0.1164, 0.1398, 0.1009, 0.1147, 0.1777, 0.4079, 0.4113, 0.3973, 0.5078,
     0.6509, 0],
    [0.0378, 0.0318, 0.0423, 0.035, 0.1787, 0.1635, 0.0887, 0.0817, 0.1779, 0.2053, 0.3135, 0.3118, 0.3686, 0.3885,
     0.585, 0],
    [0.0365, 0.1632, 0.1636, 0.1421, 0.113, 0.1306, 0.2112, 0.2268, 0.2992, 0.3735, 0.3042, 0.0387, 0.2679, 0.5397,
     0.6204, 0],
    [0.0188, 0.037, 0.0953, 0.0824, 0.0249, 0.0488, 0.1424, 0.1972, 0.1873, 0.1806, 0.2139, 0.1523, 0.1975, 0.4844,
     0.7298, 0],
    [0.0856, 0.0454, 0.0382, 0.0203, 0.0385, 0.0534, 0.214, 0.311, 0.2837, 0.2751, 0.2707, 0.0946, 0.102, 0.4519,
     0.6737, 0],
    [0.0274, 0.0242, 0.0621, 0.056, 0.1129, 0.0973, 0.1823, 0.1745, 0.144, 0.1808, 0.2366, 0.0906, 0.1749, 0.4012,
     0.5187, 0],
    [0.0235, 0.0291, 0.0749, 0.0519, 0.0227, 0.0834, 0.0677, 0.2002, 0.2876, 0.3674, 0.2974, 0.0837, 0.1912, 0.504,
     0.6352, 0],
    [0.0126, 0.0519, 0.0621, 0.0518, 0.1072, 0.2587, 0.2304, 0.2067, 0.3416, 0.4284, 0.3015, 0.1207, 0.3299, 0.5707,
     0.6962, 0],
    [0.0253, 0.0808, 0.0507, 0.0244, 0.1724, 0.3823, 0.3729, 0.3583, 0.3429, 0.2197, 0.2653, 0.3223, 0.5582, 0.6916,
     0.7943, 0],
    [0.026, 0.0192, 0.0254, 0.0061, 0.0352, 0.0701, 0.1263, 0.108, 0.1523, 0.163, 0.103, 0.2187, 0.1542, 0.263,
     0.294, 0],
    [0.0459, 0.0437, 0.0347, 0.0456, 0.0067, 0.089, 0.1798, 0.1741, 0.1598, 0.1408, 0.2693, 0.3259, 0.4545, 0.5785,
     0.4471, 0],
    [0.0025, 0.0309, 0.0171, 0.0228, 0.0434, 0.1224, 0.1947, 0.1661, 0.1368, 0.143, 0.0994, 0.225, 0.2444, 0.3239,
     0.3039, 0],
    [0.0291, 0.04, 0.0771, 0.0809, 0.0521, 0.1051, 0.0145, 0.0674, 0.1294, 0.1146, 0.0942, 0.0794, 0.0252, 0.1191,
     0.1045, 0],
    [0.0181, 0.0146, 0.0026, 0.0141, 0.0421, 0.0473, 0.0361, 0.0741, 0.1398, 0.1045, 0.0904, 0.0671, 0.0997, 0.1056,
     0.0346, 0],
    [0.0491, 0.0279, 0.0592, 0.127, 0.1772, 0.1908, 0.2217, 0.0768, 0.1246, 0.2028, 0.0947, 0.2497, 0.2209, 0.3195,
     0.334, 1],
    [0.1313, 0.2339, 0.3059, 0.4264, 0.401, 0.1791, 0.1853, 0.0055, 0.1929, 0.2231, 0.2907, 0.2259, 0.3136, 0.3302,
     0.366, 1],
    [0.0201, 0.0423, 0.0554, 0.0783, 0.062, 0.0871, 0.1201, 0.2707, 0.1206, 0.0279, 0.2251, 0.2615, 0.177, 0.3709,
     0.4533, 1],
    [0.0629, 0.1065, 0.1526, 0.1229, 0.1437, 0.119, 0.0884, 0.0907, 0.2107, 0.3597, 0.5466, 0.5205, 0.5127, 0.5395,
     0.6558, 1],
    [0.0335, 0.0134, 0.0696, 0.118, 0.0348, 0.118, 0.1948, 0.1607, 0.3036, 0.4372, 0.5533, 0.5771, 0.7022, 0.7067,
     0.7367, 1],
    [0.0587, 0.121, 0.1268, 0.1498, 0.1436, 0.0561, 0.0832, 0.0672, 0.1372, 0.2352, 0.3208, 0.4257, 0.5201, 0.4914,
     0.595, 1],
    [0.0162, 0.0253, 0.0262, 0.0386, 0.0645, 0.0472, 0.1056, 0.1388, 0.0598, 0.1334, 0.2969, 0.4754, 0.5677, 0.569,
     0.6421, 1],
    [0.0307, 0.0523, 0.0653, 0.0521, 0.0611, 0.0577, 0.0665, 0.0664, 0.146, 0.2792, 0.3877, 0.4992, 0.4981, 0.4972,
     0.5607, 1],
    [0.0116, 0.0179, 0.0449, 0.1096, 0.1913, 0.0924, 0.0761, 0.1092, 0.0757, 0.1006, 0.25, 0.3988, 0.3809, 0.4753,
     0.6165, 1],
    [0.0331, 0.0423, 0.0474, 0.0818, 0.0835, 0.0756, 0.0374, 0.0961, 0.0548, 0.0193, 0.0897, 0.1734, 0.1936, 0.2803,
     0.3313, 1],
    [0.0428, 0.0555, 0.0708, 0.0618, 0.1215, 0.1524, 0.1543, 0.0391, 0.061, 0.0113, 0.1255, 0.2473, 0.3011, 0.3747,
     0.452, 1],
    [0.0599, 0.0474, 0.0498, 0.0387, 0.1026, 0.0773, 0.0853, 0.0447, 0.1094, 0.0351, 0.1582, 0.2023, 0.2268, 0.2829,
     0.3819, 1],
    [0.0264, 0.0071, 0.0342, 0.0793, 0.1043, 0.0783, 0.1417, 0.1176, 0.0453, 0.0945, 0.1132, 0.084, 0.0717, 0.1968,
     0.2633, 1],
    [0.021, 0.0121, 0.0203, 0.1036, 0.1675, 0.0418, 0.0723, 0.0828, 0.0494, 0.0686, 0.1125, 0.1741, 0.271, 0.3087,
     0.3575, 1],
    [0.053, 0.0885, 0.1997, 0.2604, 0.3225, 0.2247, 0.0617, 0.2287, 0.095, 0.074, 0.161, 0.2226, 0.2703, 0.3365,
     0.4266, 1],
    [0.0454, 0.0472, 0.0697, 0.1021, 0.1397, 0.1493, 0.1487, 0.0771, 0.1171, 0.1675, 0.2799, 0.3323, 0.4012, 0.4296,
     0.535, 1],
    [0.0283, 0.0599, 0.0656, 0.0229, 0.0839, 0.1673, 0.1154, 0.1098, 0.137, 0.1767, 0.1995, 0.2869, 0.3275, 0.3769,
     0.4169, 1],
    [0.0114, 0.0222, 0.0269, 0.0384, 0.1217, 0.2062, 0.1489, 0.0929, 0.135, 0.1799, 0.2486, 0.2973, 0.3672, 0.4394,
     0.5258, 1],
    [0.0414, 0.0436, 0.0447, 0.0844, 0.0419, 0.1215, 0.2002, 0.1516, 0.0818, 0.1975, 0.2309, 0.3025, 0.3938, 0.505,
     0.5872, 1],
    [0.0094, 0.0333, 0.0306, 0.0376, 0.1296, 0.1795, 0.1909, 0.1692, 0.187, 0.1725, 0.2228, 0.3106, 0.4144, 0.5157,
     0.5369, 1],
    [0.0228, 0.0106, 0.013, 0.0842, 0.1117, 0.1506, 0.1776, 0.0997, 0.1428, 0.2227, 0.2621, 0.3109, 0.2859, 0.3316,
     0.3755, 1],
    [0.0363, 0.0478, 0.0298, 0.021, 0.1409, 0.1916, 0.1349, 0.1613, 0.1703, 0.1444, 0.1989, 0.2154, 0.2863, 0.357,
     0.398, 1],
    [0.0261, 0.0266, 0.0223, 0.0749, 0.1364, 0.1513, 0.1316, 0.1654, 0.1864, 0.2013, 0.289, 0.365, 0.351, 0.3495,
     0.4325, 1],
    [0.0346, 0.0509, 0.0079, 0.0243, 0.0432, 0.0735, 0.0938, 0.1134, 0.1228, 0.1508, 0.1809, 0.239, 0.2947, 0.2866,
     0.401, 1],
    [0.0162, 0.0041, 0.0239, 0.0441, 0.063, 0.0921, 0.1368, 0.1078, 0.1552, 0.1779, 0.2164, 0.2568, 0.3089, 0.3829,
     0.4393, 1],
    [0.0249, 0.0119, 0.0277, 0.076, 0.1218, 0.1538, 0.1192, 0.1229, 0.2119, 0.2531, 0.2855, 0.2961, 0.3341, 0.4287,
     0.5205, 1],
    [0.027, 0.0163, 0.0341, 0.0247, 0.0822, 0.1256, 0.1323, 0.1584, 0.2017, 0.2122, 0.221, 0.2399, 0.2964, 0.4061,
     0.5095, 1],
    [0.0388, 0.0324, 0.0688, 0.0898, 0.1267, 0.1515, 0.2134, 0.2613, 0.2832, 0.2718, 0.3645, 0.3934, 0.3843, 0.4677,
     0.5364, 1],
    [0.0228, 0.0853, 0.1, 0.0428, 0.1117, 0.1651, 0.1597, 0.2116, 0.3295, 0.3517, 0.333, 0.3643, 0.402, 0.4731,
     0.5196, 1],
    [0.0715, 0.0849, 0.0587, 0.0218, 0.0862, 0.1801, 0.1916, 0.1896, 0.296, 0.4186, 0.4867, 0.5249, 0.5959, 0.6855,
     0.8573, 1],
    [0.0209, 0.0261, 0.012, 0.0768, 0.1064, 0.168, 0.3016, 0.346, 0.3314, 0.4125, 0.3943, 0.1334, 0.4622, 0.997,
     0.9137, 1],
    [0.0374, 0.0586, 0.0628, 0.0534, 0.0255, 0.1422, 0.2072, 0.2734, 0.307, 0.2597, 0.3483, 0.3999, 0.4574, 0.595,
     0.7924, 1],
    [0.1371, 0.1226, 0.1385, 0.1484, 0.1776, 0.1428, 0.1773, 0.2161, 0.163, 0.2067, 0.4257, 0.5484, 0.7131, 0.7003,
     0.6777, 1],
    [0.0443, 0.0446, 0.0235, 0.1008, 0.2252, 0.2611, 0.2061, 0.1668, 0.1801, 0.3083, 0.3794, 0.5364, 0.6173, 0.7842,
     0.8392, 1],
    [0.115, 0.1163, 0.0866, 0.0358, 0.0232, 0.1267, 0.2417, 0.2661, 0.4346, 0.5378, 0.3816, 0.0991, 0.0616, 0.1795,
     0.3907, 1],
    [0.0968, 0.0821, 0.0629, 0.0608, 0.0617, 0.1207, 0.0944, 0.4223, 0.5744, 0.5025, 0.3488, 0.17, 0.2076, 0.3087,
     0.4224, 1],
    [0.079, 0.0707, 0.0352, 0.166, 0.133, 0.0226, 0.0771, 0.2678, 0.5664, 0.6609, 0.5002, 0.2583, 0.165, 0.4347,
     0.4515, 1],
    [0.1083, 0.107, 0.0257, 0.0837, 0.0748, 0.1125, 0.3322, 0.459, 0.5526, 0.5966, 0.5304, 0.2251, 0.2402, 0.2689,
     0.6646, 1],
    [0.0094, 0.0611, 0.1136, 0.1203, 0.0403, 0.1227, 0.2495, 0.4566, 0.6587, 0.5079, 0.335, 0.0834, 0.3004, 0.3957,
     0.3769, 1],
    [0.1088, 0.1278, 0.0926, 0.1234, 0.1276, 0.1731, 0.1948, 0.4262, 0.6828, 0.5761, 0.4733, 0.2362, 0.1023, 0.2904,
     0.4713, 1],
    [0.043, 0.0902, 0.0833, 0.0813, 0.0165, 0.0277, 0.0569, 0.2057, 0.3887, 0.7106, 0.7342, 0.5033, 0.3, 0.1951,
     0.2767, 1],
    [0.0731, 0.1249, 0.1665, 0.1496, 0.1443, 0.277, 0.2555, 0.1712, 0.0466, 0.1114, 0.1739, 0.316, 0.3249, 0.2164,
     0.2031, 1],
    [0.0164, 0.0627, 0.0738, 0.0608, 0.0233, 0.1048, 0.1338, 0.0644, 0.1522, 0.078, 0.1791, 0.2681, 0.1788, 0.1039,
     0.198, 1],
    [0.0412, 0.1135, 0.0518, 0.0232, 0.0646, 0.1124, 0.1787, 0.2407, 0.2682, 0.2058, 0.1546, 0.2671, 0.3141, 0.2904,
     0.3531, 1],
    [0.0707, 0.1252, 0.1447, 0.1644, 0.1693, 0.0844, 0.0715, 0.0947, 0.1583, 0.1247, 0.234, 0.1764, 0.2284, 0.3115,
     0.4725, 1],
    [0.0526, 0.0563, 0.1219, 0.1206, 0.0246, 0.1022, 0.0539, 0.0439, 0.2291, 0.1632, 0.2544, 0.2807, 0.3011, 0.3361,
     0.3024, 1],
    [0.0516, 0.0944, 0.0622, 0.0415, 0.0995, 0.2431, 0.1777, 0.2018, 0.2611, 0.1294, 0.2646, 0.2778, 0.4432, 0.3672,
     0.2035, 1],
    [0.0299, 0.0688, 0.0992, 0.1021, 0.08, 0.0629, 0.013, 0.0813, 0.1761, 0.0998, 0.0523, 0.0904, 0.2655, 0.3099,
     0.352, 1],
    [0.0721, 0.1574, 0.1112, 0.1085, 0.0666, 0.18, 0.1108, 0.2794, 0.1408, 0.0795, 0.2534, 0.392, 0.3375, 0.161,
     0.1889, 1],
    [0.1021, 0.083, 0.0577, 0.0627, 0.0635, 0.1328, 0.0988, 0.1787, 0.1199, 0.1369, 0.2509, 0.2631, 0.2796, 0.2977,
     0.3823, 1],
    [0.0654, 0.0649, 0.0737, 0.1132, 0.2482, 0.1257, 0.1797, 0.0989, 0.246, 0.3422, 0.2128, 0.1377, 0.4032, 0.5684,
     0.2398, 1],
    [0.0712, 0.0901, 0.1276, 0.1497, 0.1284, 0.1165, 0.1285, 0.1684, 0.183, 0.2127, 0.2891, 0.3985, 0.4576, 0.5821,
     0.5027, 1],
    [0.0207, 0.0535, 0.0334, 0.0818, 0.074, 0.0324, 0.0918, 0.107, 0.1553, 0.1234, 0.1796, 0.1787, 0.1247, 0.2577,
     0.337, 1],
    [0.0209, 0.0278, 0.0115, 0.0445, 0.0427, 0.0766, 0.1458, 0.143, 0.1894, 0.1853, 0.1748, 0.1556, 0.1476, 0.1378,
     0.2584, 1],
    [0.0231, 0.0315, 0.017, 0.0226, 0.041, 0.0116, 0.0223, 0.0805, 0.2365, 0.2461, 0.2245, 0.152, 0.1732, 0.3099,
     0.438, 1],
    [0.0131, 0.0201, 0.0045, 0.0217, 0.023, 0.0481, 0.0742, 0.0333, 0.1369, 0.2079, 0.2295, 0.199, 0.1184, 0.1891,
     0.2949, 1],
    [0.0233, 0.0394, 0.0416, 0.0547, 0.0993, 0.1515, 0.1674, 0.1513, 0.1723, 0.2078, 0.1239, 0.0236, 0.1771, 0.3115,
     0.499, 1],
    [0.0117, 0.0069, 0.0279, 0.0583, 0.0915, 0.1267, 0.1577, 0.1927, 0.2361, 0.2169, 0.118, 0.0754, 0.2782, 0.3758,
     0.5093, 1],
    [0.0211, 0.0128, 0.0015, 0.045, 0.0711, 0.1563, 0.1518, 0.1206, 0.1666, 0.1345, 0.0785, 0.0367, 0.1227, 0.2614,
     0.428, 1],
    [0.0047, 0.0059, 0.008, 0.0554, 0.0883, 0.1278, 0.1674, 0.1373, 0.2922, 0.3469, 0.3265, 0.3263, 0.2301, 0.1253,
     0.2102, 1],
    [0.0201, 0.0178, 0.0274, 0.0232, 0.0724, 0.0833, 0.1232, 0.1298, 0.2085, 0.272, 0.2188, 0.3037, 0.2959, 0.2059,
     0.0906, 1],
    [0.0107, 0.0453, 0.0289, 0.0713, 0.1075, 0.1019, 0.1606, 0.2119, 0.3061, 0.2936, 0.3104, 0.3431, 0.2456, 0.1887,
     0.1184, 1],
    [0.0235, 0.022, 0.0167, 0.0516, 0.0746, 0.1121, 0.1258, 0.1717, 0.3074, 0.3199, 0.2946, 0.2484, 0.251, 0.1806,
     0.1413, 1],
    [0.0258, 0.0433, 0.0547, 0.0681, 0.0784, 0.125, 0.1296, 0.1729, 0.2794, 0.2954, 0.2506, 0.2601, 0.2249, 0.2115,
     0.127, 1],
    [0.0305, 0.0363, 0.0214, 0.0227, 0.0456, 0.0665, 0.0939, 0.0972, 0.2535, 0.3127, 0.2192, 0.2621, 0.2419, 0.2179,
     0.1159, 1],
    [0.0217, 0.0152, 0.0346, 0.0346, 0.0484, 0.0526, 0.0773, 0.0862, 0.1451, 0.211, 0.2343, 0.2087, 0.1645, 0.1689,
     0.165, 1],
    [0.0072, 0.0027, 0.0089, 0.0061, 0.042, 0.0865, 0.1182, 0.0999, 0.1976, 0.2318, 0.2472, 0.288, 0.2126, 0.0708,
     0.1194, 1],
    [0.0163, 0.0198, 0.0202, 0.0386, 0.0752, 0.1444, 0.1487, 0.1484, 0.2442, 0.2822, 0.3691, 0.375, 0.3927, 0.3308,
     0.1085, 1],
    [0.0221, 0.0065, 0.0164, 0.0487, 0.0519, 0.0849, 0.0812, 0.1833, 0.2228, 0.181, 0.2549, 0.2984, 0.2624, 0.1893,
     0.0668, 1],
    [0.0411, 0.0277, 0.0604, 0.0525, 0.0489, 0.0385, 0.0611, 0.1117, 0.1237, 0.23, 0.137, 0.1335, 0.2137, 0.1526,
     0.0775, 1],
    [0.0137, 0.0297, 0.0116, 0.0082, 0.0241, 0.0253, 0.0279, 0.013, 0.0489, 0.0874, 0.11, 0.1084, 0.1094, 0.1023,
     0.0601, 1],
    [0.0015, 0.0186, 0.0289, 0.0195, 0.0515, 0.0817, 0.1005, 0.0124, 0.1168, 0.1476, 0.2118, 0.2575, 0.2354, 0.1334,
     0.0092, 1],
    [0.013, 0.012, 0.0436, 0.0624, 0.0428, 0.0349, 0.0384, 0.0446, 0.1318, 0.1375, 0.2026, 0.2389, 0.2112, 0.1444,
     0.0742, 1],
    [0.0134, 0.0172, 0.0178, 0.0363, 0.0444, 0.0744, 0.08, 0.0456, 0.0368, 0.125, 0.2405, 0.2325, 0.2523, 0.1472,
     0.0669, 1],
    [0.0179, 0.0136, 0.0408, 0.0633, 0.0596, 0.0808, 0.209, 0.3465, 0.5276, 0.5965, 0.6254, 0.4507, 0.3693, 0.2864,
     0.1635, 1],
    [0.018, 0.0444, 0.0476, 0.0698, 0.1615, 0.0887, 0.0596, 0.1071, 0.3175, 0.2918, 0.3273, 0.3035, 0.3033, 0.2587,
     0.1682, 1],
    [0.0329, 0.0216, 0.0386, 0.0627, 0.1158, 0.1482, 0.2054, 0.1605, 0.2532, 0.2672, 0.3056, 0.3161, 0.2314, 0.2067,
     0.1804, 1],
    [0.0191, 0.0173, 0.0291, 0.0301, 0.0463, 0.069, 0.0576, 0.1103, 0.2423, 0.3134, 0.4786, 0.5239, 0.4393, 0.344,
     0.2869, 1],
    [0.0294, 0.0123, 0.0117, 0.0113, 0.0497, 0.0998, 0.1326, 0.1117, 0.2984, 0.3473, 0.4231, 0.5044, 0.5237, 0.4398,
     0.3236, 1],
    [0.0635, 0.0709, 0.0453, 0.0333, 0.0185, 0.126, 0.1015, 0.1918, 0.3362, 0.39, 0.4674, 0.5632, 0.5506, 0.4343,
     0.3052, 1],
    [0.0201, 0.0165, 0.0344, 0.033, 0.0397, 0.0443, 0.0684, 0.0903, 0.1739, 0.2571, 0.2931, 0.3108, 0.3603, 0.3002,
     0.2718, 1],
    [0.0197, 0.0394, 0.0384, 0.0076, 0.0251, 0.0629, 0.0747, 0.0578, 0.1357, 0.1695, 0.1734, 0.247, 0.3141, 0.3297,
     0.2759, 1],
    [0.0394, 0.042, 0.0446, 0.0551, 0.0597, 0.1416, 0.0956, 0.0802, 0.1618, 0.2558, 0.3078, 0.3404, 0.34, 0.3951,
     0.3352, 1],
    [0.031, 0.0221, 0.0433, 0.0191, 0.0964, 0.1827, 0.1106, 0.1702, 0.2804, 0.4432, 0.5222, 0.5611, 0.5379, 0.4048,
     0.2245, 1],
    [0.0423, 0.0321, 0.0709, 0.0108, 0.107, 0.0973, 0.0961, 0.1323, 0.2462, 0.2696, 0.3412, 0.4292, 0.3682, 0.394,
     0.2965, 1],
    [0.0095, 0.0308, 0.0539, 0.0411, 0.0613, 0.1039, 0.1016, 0.1394, 0.2592, 0.3745, 0.4229, 0.4499, 0.5404, 0.4303,
     0.3333, 1],
    [0.0096, 0.0404, 0.0682, 0.0688, 0.0887, 0.0932, 0.0955, 0.214, 0.2546, 0.2952, 0.4025, 0.5148, 0.4901, 0.4127,
     0.3575, 1],
    [0.0269, 0.0383, 0.0505, 0.0707, 0.1313, 0.2103, 0.2263, 0.2524, 0.3595, 0.5915, 0.6675, 0.5679, 0.5175, 0.3334,
     0.2002, 1],
    [0.034, 0.0625, 0.0381, 0.0257, 0.0441, 0.1027, 0.1287, 0.185, 0.2647, 0.4117, 0.5245, 0.5341, 0.5554, 0.3915,
     0.295, 1],
    [0.0209, 0.0191, 0.0411, 0.0321, 0.0698, 0.1579, 0.1438, 0.1402, 0.3048, 0.3914, 0.3504, 0.3669, 0.3943, 0.3311,
     0.3331, 1],
    [0.0368, 0.0279, 0.0103, 0.0566, 0.0759, 0.0679, 0.097, 0.1473, 0.2164, 0.2544, 0.2936, 0.2935, 0.2657, 0.3187,
     0.2794, 1],
    [0.0089, 0.0274, 0.0248, 0.0237, 0.0224, 0.0845, 0.1488, 0.1224, 0.1569, 0.2119, 0.3003, 0.3094, 0.2743, 0.2547,
     0.187, 1],
    [0.0158, 0.0239, 0.015, 0.0494, 0.0988, 0.1425, 0.1463, 0.1219, 0.1697, 0.1923, 0.2361, 0.2719, 0.3049, 0.2986,
     0.2226, 1],
    [0.0156, 0.021, 0.0282, 0.0596, 0.0462, 0.0779, 0.1365, 0.078, 0.1038, 0.1567, 0.2476, 0.2783, 0.2896, 0.2956,
     0.3189, 1],
    [0.0315, 0.0252, 0.0167, 0.0479, 0.0902, 0.1057, 0.1024, 0.1209, 0.1241, 0.1533, 0.2128, 0.2536, 0.2686, 0.2803,
     0.1886, 1],
    [0.0056, 0.0267, 0.0221, 0.0561, 0.0936, 0.1146, 0.0706, 0.0996, 0.1673, 0.1859, 0.2481, 0.2712, 0.2934, 0.2637,
     0.188, 1],
    [0.0203, 0.0121, 0.038, 0.0128, 0.0537, 0.0874, 0.1021, 0.0852, 0.1136, 0.1747, 0.2198, 0.2721, 0.2105, 0.1727,
     0.204, 1],
    [0.0392, 0.0108, 0.0267, 0.0257, 0.041, 0.0491, 0.1053, 0.169, 0.2105, 0.2471, 0.268, 0.3049, 0.2863, 0.2294,
     0.1165, 1],
    [0.0129, 0.0141, 0.0309, 0.0375, 0.0767, 0.0787, 0.0662, 0.1108, 0.1777, 0.2245, 0.2431, 0.3134, 0.3206, 0.2917,
     0.2249, 1],
    [0.005, 0.0017, 0.027, 0.045, 0.0958, 0.083, 0.0879, 0.122, 0.1977, 0.2282, 0.2521, 0.3484, 0.3309, 0.2614,
     0.1782, 1],
    [0.0366, 0.0421, 0.0504, 0.025, 0.0596, 0.0252, 0.0958, 0.0991, 0.1419, 0.1847, 0.2222, 0.2648, 0.2508, 0.2291,
     0.1555, 1],
    [0.0238, 0.0318, 0.0422, 0.0399, 0.0788, 0.0766, 0.0881, 0.1143, 0.1594, 0.2048, 0.2652, 0.31, 0.2381, 0.1918,
     0.143, 1],
    [0.0116, 0.0744, 0.0367, 0.0225, 0.0076, 0.0545, 0.111, 0.1069, 0.1708, 0.2271, 0.3171, 0.2882, 0.2657, 0.2307,
     0.1889, 1],
    [0.0131, 0.0387, 0.0329, 0.0078, 0.0721, 0.1341, 0.1626, 0.1902, 0.261, 0.3193, 0.3468, 0.3738, 0.3055, 0.1926,
     0.1385, 1],
    [0.0335, 0.0258, 0.0398, 0.057, 0.0529, 0.1091, 0.1709, 0.1684, 0.1865, 0.266, 0.3188, 0.3553, 0.3116, 0.1965,
     0.178, 1],
    [0.0272, 0.0378, 0.0488, 0.0848, 0.1127, 0.1103, 0.1349, 0.2337, 0.3113, 0.3997, 0.3941, 0.3309, 0.2926, 0.176,
     0.1739, 1],
    [0.0187, 0.0346, 0.0168, 0.0177, 0.0393, 0.163, 0.2028, 0.1694, 0.2328, 0.2684, 0.3108, 0.2933, 0.2275, 0.0994,
     0.1801, 1],
    [0.0323, 0.0101, 0.0298, 0.0564, 0.076, 0.0958, 0.099, 0.1018, 0.103, 0.2154, 0.3085, 0.3425, 0.299, 0.1402,
     0.1235, 1],
    [0.0522, 0.0437, 0.018, 0.0292, 0.0351, 0.1171, 0.1257, 0.1178, 0.1258, 0.2529, 0.2716, 0.2374, 0.1878, 0.0983,
     0.0683, 1],
    [0.0303, 0.0353, 0.049, 0.0608, 0.0167, 0.1354, 0.1465, 0.1123, 0.1945, 0.2354, 0.2898, 0.2812, 0.1578, 0.0273,
     0.0673, 1],
    [0.026, 0.0363, 0.0136, 0.0272, 0.0214, 0.0338, 0.0655, 0.14, 0.1843, 0.2354, 0.272, 0.2442, 0.1665, 0.0336,
     0.1302, 1]
]

if __name__ == '__main__':

    data_set = data

    true_set = [row for row in data_set if row[-1] == 1]
    false_set = [row for row in data_set if row[-1] == 0]

    train_set = true_set[:int(0.8 * len(true_set))] + false_set[:int(0.8 * len(false_set))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    val_set = true_set[int(0.8 * len(true_set)):] + false_set[int(0.8 * len(false_set)):]
    val_x = [row[:-1] for row in val_set]
    val_y = [row[-1] for row in val_set]

    learning = float(input())
    epoh = int(input())
    clasifikator = MLPClassifier(6, activation="tanh", learning_rate_init=learning, max_iter=epoh, random_state=0)
    clasifikator.fit(train_x, train_y)


    tocnost = 0
    for i in range(len(train_x)):
        predicted_class = clasifikator.predict([train_x[i]])[0]
        true_class = train_y[i]
        if true_class == predicted_class:
            tocnost += 1

    tocnost = tocnost / len(train_set)


    val_tocnost = 0
    for i in range(len(val_x)):
        predicted_class = clasifikator.predict([val_x[i]])[0]
        true_class = val_y[i]
        if true_class == predicted_class:
            val_tocnost += 1

    val_tocnost = val_tocnost / len(val_set)


    if tocnost > val_tocnost + val_tocnost*0.15:
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")


    print(f'Tochnost so trenirachko mnozhestvo: {tocnost}')
    print(f'Tochnost so validacisko mnozhestvo: {val_tocnost}')

