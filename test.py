{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "6ff1526a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "3cea144b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\odemeo\\\\Documents\\\\Field_Data_Processing\\\\CACO_MET\\\\HoM_2021-06-29.csv'"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "path_nm='C:\\\\Users\\\\odemeo\\\\Documents\\\\Field_Data_Processing\\\\CACO_MET\\\\'\n",
    "file_name='HoM_2021-06-29.csv'\n",
    "path_nm + file_name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "bf4fe8b9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Date and Time in UTC</th>\n",
       "      <th>SampNum</th>\n",
       "      <th>Battery</th>\n",
       "      <th>BoardTemp</th>\n",
       "      <th>signalPercent</th>\n",
       "      <th>WXTDn</th>\n",
       "      <th>WXTDm</th>\n",
       "      <th>WXTDx</th>\n",
       "      <th>WXTSn</th>\n",
       "      <th>WXTSm</th>\n",
       "      <th>WXTSx</th>\n",
       "      <th>WXTTa</th>\n",
       "      <th>WXTUa</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2021-06-29 14:56:00</td>\n",
       "      <td>2</td>\n",
       "      <td>3.684</td>\n",
       "      <td>32.25</td>\n",
       "      <td>-9999</td>\n",
       "      <td>170</td>\n",
       "      <td>202</td>\n",
       "      <td>238</td>\n",
       "      <td>0.0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>7.0</td>\n",
       "      <td>26.3</td>\n",
       "      <td>77.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2021-06-29 14:57:00</td>\n",
       "      <td>3</td>\n",
       "      <td>3.654</td>\n",
       "      <td>32.00</td>\n",
       "      <td>-9999</td>\n",
       "      <td>173</td>\n",
       "      <td>205</td>\n",
       "      <td>232</td>\n",
       "      <td>3.1</td>\n",
       "      <td>4.8</td>\n",
       "      <td>7.1</td>\n",
       "      <td>26.4</td>\n",
       "      <td>77.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2021-06-29 14:58:00</td>\n",
       "      <td>4</td>\n",
       "      <td>3.654</td>\n",
       "      <td>31.75</td>\n",
       "      <td>-9999</td>\n",
       "      <td>180</td>\n",
       "      <td>210</td>\n",
       "      <td>247</td>\n",
       "      <td>2.8</td>\n",
       "      <td>4.7</td>\n",
       "      <td>7.1</td>\n",
       "      <td>26.4</td>\n",
       "      <td>78.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2021-06-29 14:59:00</td>\n",
       "      <td>2</td>\n",
       "      <td>4.745</td>\n",
       "      <td>32.00</td>\n",
       "      <td>-9999</td>\n",
       "      <td>190</td>\n",
       "      <td>215</td>\n",
       "      <td>247</td>\n",
       "      <td>2.6</td>\n",
       "      <td>4.5</td>\n",
       "      <td>7.0</td>\n",
       "      <td>26.4</td>\n",
       "      <td>77.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2021-06-29 15:00:00</td>\n",
       "      <td>3</td>\n",
       "      <td>4.730</td>\n",
       "      <td>32.00</td>\n",
       "      <td>-9999</td>\n",
       "      <td>169</td>\n",
       "      <td>207</td>\n",
       "      <td>243</td>\n",
       "      <td>2.6</td>\n",
       "      <td>4.8</td>\n",
       "      <td>7.0</td>\n",
       "      <td>26.4</td>\n",
       "      <td>76.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122589</th>\n",
       "      <td>2021-09-22 18:06:00</td>\n",
       "      <td>-8486</td>\n",
       "      <td>3.639</td>\n",
       "      <td>31.25</td>\n",
       "      <td>-9999</td>\n",
       "      <td>145</td>\n",
       "      <td>182</td>\n",
       "      <td>229</td>\n",
       "      <td>2.4</td>\n",
       "      <td>5.4</td>\n",
       "      <td>9.1</td>\n",
       "      <td>24.8</td>\n",
       "      <td>74.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122590</th>\n",
       "      <td>2021-09-22 18:07:00</td>\n",
       "      <td>-8485</td>\n",
       "      <td>3.639</td>\n",
       "      <td>31.25</td>\n",
       "      <td>-9999</td>\n",
       "      <td>135</td>\n",
       "      <td>189</td>\n",
       "      <td>243</td>\n",
       "      <td>2.4</td>\n",
       "      <td>4.9</td>\n",
       "      <td>8.3</td>\n",
       "      <td>24.9</td>\n",
       "      <td>74.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122591</th>\n",
       "      <td>2021-09-22 18:08:00</td>\n",
       "      <td>-8484</td>\n",
       "      <td>3.639</td>\n",
       "      <td>31.50</td>\n",
       "      <td>-9999</td>\n",
       "      <td>135</td>\n",
       "      <td>194</td>\n",
       "      <td>246</td>\n",
       "      <td>2.5</td>\n",
       "      <td>4.9</td>\n",
       "      <td>8.3</td>\n",
       "      <td>25.1</td>\n",
       "      <td>73.2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122592</th>\n",
       "      <td>2021-09-22 18:09:00</td>\n",
       "      <td>-8483</td>\n",
       "      <td>3.639</td>\n",
       "      <td>31.50</td>\n",
       "      <td>-9999</td>\n",
       "      <td>153</td>\n",
       "      <td>201</td>\n",
       "      <td>246</td>\n",
       "      <td>2.5</td>\n",
       "      <td>5.3</td>\n",
       "      <td>8.5</td>\n",
       "      <td>25.2</td>\n",
       "      <td>71.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>122593</th>\n",
       "      <td>2021-09-22 18:10:00</td>\n",
       "      <td>-8482</td>\n",
       "      <td>3.654</td>\n",
       "      <td>31.25</td>\n",
       "      <td>-9999</td>\n",
       "      <td>171</td>\n",
       "      <td>203</td>\n",
       "      <td>232</td>\n",
       "      <td>3.5</td>\n",
       "      <td>6.3</td>\n",
       "      <td>9.4</td>\n",
       "      <td>25.0</td>\n",
       "      <td>71.4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>122594 rows ?? 13 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "       Date and Time in UTC  SampNum  Battery  BoardTemp  signalPercent  \\\n",
       "0       2021-06-29 14:56:00        2    3.684      32.25          -9999   \n",
       "1       2021-06-29 14:57:00        3    3.654      32.00          -9999   \n",
       "2       2021-06-29 14:58:00        4    3.654      31.75          -9999   \n",
       "3       2021-06-29 14:59:00        2    4.745      32.00          -9999   \n",
       "4       2021-06-29 15:00:00        3    4.730      32.00          -9999   \n",
       "...                     ...      ...      ...        ...            ...   \n",
       "122589  2021-09-22 18:06:00    -8486    3.639      31.25          -9999   \n",
       "122590  2021-09-22 18:07:00    -8485    3.639      31.25          -9999   \n",
       "122591  2021-09-22 18:08:00    -8484    3.639      31.50          -9999   \n",
       "122592  2021-09-22 18:09:00    -8483    3.639      31.50          -9999   \n",
       "122593  2021-09-22 18:10:00    -8482    3.654      31.25          -9999   \n",
       "\n",
       "        WXTDn  WXTDm  WXTDx  WXTSn  WXTSm  WXTSx  WXTTa  WXTUa  \n",
       "0         170    202    238    0.0    5.1    7.0   26.3   77.4  \n",
       "1         173    205    232    3.1    4.8    7.1   26.4   77.0  \n",
       "2         180    210    247    2.8    4.7    7.1   26.4   78.0  \n",
       "3         190    215    247    2.6    4.5    7.0   26.4   77.7  \n",
       "4         169    207    243    2.6    4.8    7.0   26.4   76.7  \n",
       "...       ...    ...    ...    ...    ...    ...    ...    ...  \n",
       "122589    145    182    229    2.4    5.4    9.1   24.8   74.5  \n",
       "122590    135    189    243    2.4    4.9    8.3   24.9   74.2  \n",
       "122591    135    194    246    2.5    4.9    8.3   25.1   73.2  \n",
       "122592    153    201    246    2.5    5.3    8.5   25.2   71.0  \n",
       "122593    171    203    232    3.5    6.3    9.4   25.0   71.4  \n",
       "\n",
       "[122594 rows x 13 columns]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df=pd.read_csv(path_nm+file_name,skiprows=7)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "9b2247aa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>SampNum</th>\n",
       "      <th>Battery</th>\n",
       "      <th>BoardTemp</th>\n",
       "      <th>signalPercent</th>\n",
       "      <th>WXTDn</th>\n",
       "      <th>WXTDm</th>\n",
       "      <th>WXTDx</th>\n",
       "      <th>WXTSn</th>\n",
       "      <th>WXTSm</th>\n",
       "      <th>WXTSx</th>\n",
       "      <th>WXTTa</th>\n",
       "      <th>WXTUa</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.0</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "      <td>122594.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>292.856078</td>\n",
       "      <td>3.623003</td>\n",
       "      <td>23.456788</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>130.246709</td>\n",
       "      <td>183.433667</td>\n",
       "      <td>219.829209</td>\n",
       "      <td>2.371266</td>\n",
       "      <td>4.099445</td>\n",
       "      <td>5.886937</td>\n",
       "      <td>20.863037</td>\n",
       "      <td>86.168375</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>19517.272594</td>\n",
       "      <td>0.025389</td>\n",
       "      <td>5.225634</td>\n",
       "      <td>0.0</td>\n",
       "      <td>78.654022</td>\n",
       "      <td>91.405097</td>\n",
       "      <td>88.711210</td>\n",
       "      <td>1.723976</td>\n",
       "      <td>2.263441</td>\n",
       "      <td>3.041321</td>\n",
       "      <td>2.998218</td>\n",
       "      <td>11.434929</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>-32768.000000</td>\n",
       "      <td>3.563000</td>\n",
       "      <td>11.500000</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>12.300000</td>\n",
       "      <td>40.300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>-17444.000000</td>\n",
       "      <td>3.608000</td>\n",
       "      <td>19.500000</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>46.000000</td>\n",
       "      <td>106.000000</td>\n",
       "      <td>178.000000</td>\n",
       "      <td>1.200000</td>\n",
       "      <td>2.500000</td>\n",
       "      <td>3.600000</td>\n",
       "      <td>18.800000</td>\n",
       "      <td>78.100000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>2119.000000</td>\n",
       "      <td>3.624000</td>\n",
       "      <td>22.500000</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>162.000000</td>\n",
       "      <td>207.000000</td>\n",
       "      <td>241.000000</td>\n",
       "      <td>2.100000</td>\n",
       "      <td>3.800000</td>\n",
       "      <td>5.600000</td>\n",
       "      <td>20.700000</td>\n",
       "      <td>88.300000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>17443.000000</td>\n",
       "      <td>3.639000</td>\n",
       "      <td>27.250000</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>189.000000</td>\n",
       "      <td>231.000000</td>\n",
       "      <td>270.000000</td>\n",
       "      <td>3.100000</td>\n",
       "      <td>5.200000</td>\n",
       "      <td>7.600000</td>\n",
       "      <td>22.700000</td>\n",
       "      <td>96.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>32767.000000</td>\n",
       "      <td>4.745000</td>\n",
       "      <td>39.750000</td>\n",
       "      <td>-9999.0</td>\n",
       "      <td>351.000000</td>\n",
       "      <td>358.000000</td>\n",
       "      <td>358.000000</td>\n",
       "      <td>16.200000</td>\n",
       "      <td>21.600000</td>\n",
       "      <td>27.900000</td>\n",
       "      <td>31.400000</td>\n",
       "      <td>100.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             SampNum        Battery      BoardTemp  signalPercent  \\\n",
       "count  122594.000000  122594.000000  122594.000000       122594.0   \n",
       "mean      292.856078       3.623003      23.456788        -9999.0   \n",
       "std     19517.272594       0.025389       5.225634            0.0   \n",
       "min    -32768.000000       3.563000      11.500000        -9999.0   \n",
       "25%    -17444.000000       3.608000      19.500000        -9999.0   \n",
       "50%      2119.000000       3.624000      22.500000        -9999.0   \n",
       "75%     17443.000000       3.639000      27.250000        -9999.0   \n",
       "max     32767.000000       4.745000      39.750000        -9999.0   \n",
       "\n",
       "               WXTDn          WXTDm          WXTDx          WXTSn  \\\n",
       "count  122594.000000  122594.000000  122594.000000  122594.000000   \n",
       "mean      130.246709     183.433667     219.829209       2.371266   \n",
       "std        78.654022      91.405097      88.711210       1.723976   \n",
       "min         0.000000       0.000000       0.000000       0.000000   \n",
       "25%        46.000000     106.000000     178.000000       1.200000   \n",
       "50%       162.000000     207.000000     241.000000       2.100000   \n",
       "75%       189.000000     231.000000     270.000000       3.100000   \n",
       "max       351.000000     358.000000     358.000000      16.200000   \n",
       "\n",
       "               WXTSm          WXTSx          WXTTa          WXTUa  \n",
       "count  122594.000000  122594.000000  122594.000000  122594.000000  \n",
       "mean        4.099445       5.886937      20.863037      86.168375  \n",
       "std         2.263441       3.041321       2.998218      11.434929  \n",
       "min         0.000000       0.000000      12.300000      40.300000  \n",
       "25%         2.500000       3.600000      18.800000      78.100000  \n",
       "50%         3.800000       5.600000      20.700000      88.300000  \n",
       "75%         5.200000       7.600000      22.700000      96.000000  \n",
       "max        21.600000      27.900000      31.400000     100.000000  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c5dd8235",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x1b77898dac0>]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(df[\"WXTSn\"].values)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "a472a001",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.any(np.isnan(df[\"WXTSn\"].values))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aba1f75b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0. , 3.1, 2.8, ..., 2.5, 2.5, 3.5])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "wind_sp=df[\"WXTSn\"].values\n",
    "wind_sp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1f938b5f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "122594\n"
     ]
    }
   ],
   "source": [
    "def windspeed_mean(ws,cf=1.):\n",
    "    mn=np.sum(cf*ws)/len(ws)\n",
    "    n=len(ws)\n",
    "    return mn,n\n",
    "print(windspeed_mean(wind_sp,2)[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "f8c3cb8c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.742532260958938\n",
      "122594\n"
     ]
    }
   ],
   "source": [
    "x,y=windspeed_mean(wind_sp,2)\n",
    "print(x)\n",
    "print(y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "8917271c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4.742532260958938\n"
     ]
    }
   ],
   "source": [
    "x,_=windspeed_mean(wind_sp,2)\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "bf9d6e59",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "122594\n"
     ]
    }
   ],
   "source": [
    "_,y=windspeed_mean(wind_sp,2)\n",
    "print(y)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
