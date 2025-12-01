import matplotlib.pyplot as plt

num_small_businesses = 33300000
num_commercial_businesses = 5500000
small_business_growth_rate = 0.043
commercial_business_growth_rate = 0.087

ch4_2022_ppb = 1907.53
ch4_2023_ppb = 1921.53
ch4_2024_ppb = 1932.67
ch4_growth_rate = [0.73, 0.1114]

co2_2022_ppb = 418.0
co2_2023_ppb = 419.7
co2_2024_ppb = 422.5
co2_growth_rate = [0.41, 0.77]

n_2023_ppb = 336.7
n_2024_ppb = 339.9
n_growth_rate = [0.95]

voc_2022_ppb = 12675.0
voc_2023_ppb = 12531.0
voc_growth_rate = -0.144

so2_2023_ppb = 100.0
so2_2024_ppb = 94.0
so2_growth_rate = -0.06

no2_2021_ppb = 53.0
no2_2022_ppb = 61.0
no2_2023_ppb = 37.0
no2_2024_ppb = 34.0 # assuming a value for 2024
no2_growth_rate = [0.1312, -0.39] 

co_2022_MMmt = 2402
co_2023_MMmt = 2640
co_2024_MMmt = 2770
co_growth_rate = [9.02, 4.7] 

o3_2022_ppb = 61
o3_2023_ppb = 84
o3_2024_ppb = 89
o3_growth_rate = [27.39, 5.62]

partmat_2022_µgm3 = 31.3
partmat_2023_µgm3 = 36.2
partmat_2024_µgm3 = 49.8
partmat_growth_rate = [13.64, 27.31]

pfas_2022_ppb = 1100000
pfas_2023_ppb = 1563509
pfas_2024_ppb = 1600000 # assuming a value for 2024
pfas_growth_rate = 29.65


hg_2023_ppb = 0
hg_2024_ppb = 0
hg_growth_rate = 0

total_business_growth = (num_small_businesses * small_business_growth_rate 
     + num_commercial_businesses * commercial_business_growth_rate)

ch4_increase = (ch4_2024_ppb - ch4_2023_ppb)
co2_increase = (co2_2024_ppb - co2_2023_ppb)
n_increase = (n_2024_ppb - n_2023_ppb)
co_increase = (co_2024_MMmt - co_2023_MMmt)
# so2_increase = (so2_2024_ppb - so2_2023_ppb)
# no2_increase = (no2_2024_ppb - no2_2023_ppb)
pfas_increase = (pfas_2024_ppb - pfas_2023_ppb)
# voc_2024_ppb = 12400.0 # assuming a value for 2024
# voc_increase = (voc_2024_ppb - voc_2023_ppb)
o3_increase = (o3_2024_ppb - o3_2023_ppb)
partmat_increase = (partmat_2024_µgm3 - partmat_2023_µgm3)
hg_increase = (hg_2024_ppb - hg_2023_ppb)
# cd_increase = (cd_2024_ppb - cd_2023_ppb)
# as_increase = (as_2024_ppb - as_2023_ppb)
# pb_increase = (pb_2024_ppb - pb_2023_ppb)
# eto_increase = (eto_2024_ppb - eto_2023_ppb)
# c10h8_2024_ppb = 0
# c10h8_2023_ppb = 0
# c10h8_increase = (c10h8_2024_ppb - c10h8_2023_ppb)
# bap_increase = (bap_2024_ppb - bap_2023_ppb)
# tph_increase = (tph_2024_ppb - tph_2023_ppb)
# btex_increase = (btex_2024_ppb - btex_2023_ppb)
# mtbe_increase = (mtbe_2024_ppb - mtbe_2023_ppb)
# tba_increase = (tba_2024_ppb - tba_2023_ppb)

growth_rates = [small_business_growth_rate, commercial_business_growth_rate, total_business_growth]

pollution_increases = [ch4_increase, co2_increase, n_increase, co_increase, pfas_increase, o3_increase, partmat_increase, hg_increase]

pollution_labels = ['CH4', 'CO2', 'N', 'CO', 'PFAS', 'O3', 'Particulate Matter', 'Hg',]

plt.figure(figsize=(12, 8))
plt.bar(
    pollution_labels, pollution_increases, color='skyblue'
)
plt.xlabel('Pollutant Substance')
plt.ylabel('Increase (mixed units: ppb, MMmt, µg/m³)') 
plt.title('Increase in Pollutants from 2023 to 2024') 
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

print(f"Total Business Growth: {total_business_growth:.2f}")
print("Pollutant Increases (2024 - 2023):")
print(f"Particulate Matter Increase: {partmat_increase:.4f} µgm3")
print(f"CH4 Increase: {ch4_increase:.4f} ppb")
print(f"CO2 Increase: {co2_increase:.4f} ppb")
print(f"N Increase: {n_increase:.4f} ppb")
print(f"CO Increase: {co_increase:.4f} MMmt")
# print(f"SO2 Increase: {so2_increase:.4f} ppb")
# print(f"NO2 Increase: {no2_increase:.4f} ppb")
print(f"PFAS Increase: {pfas_increase:.4f} ppb")
# print(f"VOC Increase: {voc_increase:.4f} ppb")
print(f"O3 Increase: {o3_increase:.4f} ppb") 
print(f"Hg Increase: {hg_increase:.4f} ppb") 
# print(f"Cd Increase: {cd_increase:.4f} ppb")
# print(f"As Increase: {as_increase:.4f} ppb")
# print(f"Pb Increase: {pb_increase:.4f} ppb") 
# print(f"EtO Increase: {eto_increase:.4f} ppb")
# print(f"C10H8 Increase: {c10h8_increase:.4f} ppb") 
# print(f"BaP Increase: {bap_increase:.4f} ppb") 
# print(f"TPH Increase: {tph_increase:.4f} ppb")
# print(f"BTEX Increase: {btex_increase:.4f} ppb")
# print(f"MTBE Increase: {mtbe_increase:.4f} ppb") 
# print(f"tBA Increase: {tba_increase:.4f} ppb")
