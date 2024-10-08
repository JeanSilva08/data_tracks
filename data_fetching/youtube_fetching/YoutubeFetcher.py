from googleapiclient.discovery import build
from time import sleep
import csv

API_KEY = 'AIzaSyD74qS0b9EHk5P-wWMOXXqWk4HTe7Fas04'

BATCH_SIZE = 50

REQUEST_DELAY = 1


class YoutubeFetcher:
    def __init__(self, api_key):
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    def get_video_views(self, video_ids):
        video_info = {}
        batch_count = len(video_ids) // BATCH_SIZE + 1

        for i in range(batch_count):
            batch_ids = video_ids[i * BATCH_SIZE: (i + 1) * BATCH_SIZE]
            request = self.youtube.videos().list(
                part='snippet,statistics',
                id=','.join(batch_ids)
            )
            response = request.execute()

            for item in response.get('items', []):
                video_id = item['id']
                title = item['snippet']['title']
                view_count = int(item['statistics']['viewCount'])
                video_info[video_id] = {'title': title, 'views': view_count}

                print(f"Fetched views for video '{title}': {view_count}")

            sleep(REQUEST_DELAY)

        return video_info


def initialize_artist_videos():
    return {
        "Mainstreet": ["l3glrN_Ppn4",
                       "qUAfc4XuWGw",
                       "uFsGu8QaS4o",
                       "njLQnvU8vzk",
                       "NkbOmC6kK-c",
                       "7L4cWt1G3j4",
                       "2uWOxz1q2ic",
                       "T2BQG_8CFHI",
                       "9aWC3Z3hjII",
                       "Z9laTuc3bcs",
                       "sisGy19Vt78",
                       "kHuvJZ5kkKY",
                       "N6Rao_x2cJc",
                       "yXvDf3nLe8M",
                       "7Zd09_o608w",
                       "-D_HejAuy4A",
                       "0eieSZEFewI",
                       "1G3F42KeBiQ",
                       "kC8X06J4Q8Q",
                       "yXbeZ8qXDQA",
                       "s8EnhrR9Hxs",
                       "QrKmPd-Ai_U",
                       "NY09D_-Ull4",
                       "UR-ROJP92pc",
                       "ay9QbRAuEgc",
                       "eCpU8IsCUPE",
                       "nd_m17VsRh0",
                       "f0WcGsJwgxo",
                       "Z4Fu8bMzsOw",
                       "XuuoTqu2yQk",
                       "JxaMoRbS7kI",
                       "QPYUMO0leyw",
                       "e3gZqfhehYU",
                       "vopfn1FNDgo",
                       "WO52f2MsYzk",
                       "ugUmaOrYx6Q",
                       "KrLnAuQXDSA",
                       "5hj2kiGGbGs",
                       "kAgw1Gkw10U",
                       "zmlNLw6iVdY",
                       "OTAM6JX1M48",
                       "ZO4-cLCMJjE",
                       "6iAb5K0bDTw",
                       "xxsGLy_5Wbo",
                       "Oia1yrePjC8",
                       "CG9GvYdQvow",
                       "uwkBATNtEb4",
                       "rxLEL7xxCD8",
                       "AWUMbVKr8r8",
                       "XfhmsPMjlhQ",
                       "hQBeY2pqZ6c",
                       "GbYRNhr5lvQ",
                       "WVndi9ppDyo",
                       "Y69kiJ3fRr8",
                       "BJa8zgf0cdQ",
                       "ysn8Ifdfry4",
                       "Ww056PGMT8Y",
                       "E6FvqDOg4tQ",
                       "15bgB21zInE",
                       "cbKF2lmFPqo",
                       "NA1UqUuqnQ4",
                       "kqPSfz_bCX8",
                       "UacEnZDwmaM",
                       "N9liPvylviE",
                       "oq5dmtQhoHU",
                       "LPoFbsAT1sE",
                       "_DiJuGAtVWs",
                       "AERWeIkBrl0",
                       "9Ve1ZolHwVM",
                       "gp7QAVTTx3Q",
                       "3PVkxOaTIU0",
                       "-gysEtnzYEw",
                       "cmWuKuTigOc",
                       "2ylXpsNcYBU",
                       "_991ANrxkZM",
                       "HpuvuIf7fBE",
                       "cY7NVK5LqOg",
                       "i2zGRad5nw0",
                       "3aKrgl3-Unc",
                       "15NOE_RezAM",
                       "-tuwzPvyKzA",
                       "R_BSdnySVLg",
                       "cFtGtWsH4co",
                       "dUC7TBmzrL4",
                       "xBpUcJKYkSk",
                       "n43oZSY7df0",
                       "Wu7-MxFRwU0",
                       "7SvCM5XqPAc",
                       "dUDLQ8pR20o",
                       "N5SWwXTlsRE",
                       "tWmTHns2vKQ",
                       "yvHbajFWOQE",
                       "PJqHlzBiZ0A",
                       "TqrJszrcKpM",
                       "MnhQ98BBLeI",
                       "kMXEtoSQX-E",
                       "eR3InvME-rg",
                       "xBvMz2i0oEM",
                       "4GukYsC1DXY",
                       "Rn1bjVTjuYA",
                       "6nT50nEGINk",
                       "LxW6iWz6JFY",
                       "9qgDh36bfJk",
                       "_Mfq9xUim1w",
                       "CC08dwBPT6o",
                       "ospxD6iryWg",
                       "2PRAiVs3MVc",
                       "QzeAJrXOdJk",
                       "xogJfbDIwq4",
                       "nbbC6RJ1V0s",
                       "cIz_P0vRU30",
                       "q2p5lSK2mXU",
                       "7zaS4MnPtRw",
                       "YkBiDJS19gg",
                       "-L1_1-iErw0",
                       "NvNVagoHmrU",
                       "AxWwPP8WsEQ",
                       "A4pHiiUpCH0",
                       "qxB3anjq4Pc",
                       "Iz44nZh9vng",
                       "kzTGMTzKo1o",
                       "m4ltJtZsz0Q",
                       "TWZPignwC5M",
                       "HhR1wqiApJc",
                       "Lys1Az6LGSc",
                       "hT84iS8fThc"],

        "Orochi": ["3NblY0mxii0",
                   "jBE_X3cMCyM",
                   "yfGMPDKq1Pg",
                   "2DXQqIat098",
                   "AoIkvrgiPQg",
                   "24lfgigKHqQ",
                   "UvYYABiJV2E",
                   "CRbG78I6D44",
                   "3WGlmbKjmPY",
                   "lq9WPdUn-mE",
                   "X7D0ckM2p2A",
                   "L8_116bLouo",
                   "qUIqJWSAuXw",
                   "Ql3cVo2f9Sg",
                   "P4JqwCxeI9Y",
                   "dsMdKWG5YfY",
                   "8LkoFhQxHaI",
                   "dMDa6drnhAo",
                   "1BOJQX6_eYU",
                   "ffWGhCgeJ7o",
                   "mn937Jdqlmo",
                   "91Fw8XnqHy4",
                   "Pib9a5umxSM",
                   "fcSYYcYW1cY",
                   "XNROQyD5EH8",
                   "SslgMAOJZwI",
                   "6BgxLcofzoo",
                   "VANSAIGXsDw",
                   "23Ac1SLUnac",
                   "arapddN0bfc",
                   "pbYwQDjz_4E",
                   "e8j6mmp3W0E",
                   "qr8ET9SbOgwd",
                   "iTZjA_BIPaU",
                   "ligT_KhSf1E",
                   "YQBeWDtExQQ",
                   "aBPU4f6rH-w",
                   "r-sjxon3GOA",
                   "ofRCBvm3Muc",
                   "S9ZK79QhwgY",
                   "ahrOERDQVpU",
                   "g5lA4RNFT3I",
                   "yTz-LsOK6EA",
                   "q8l8bTWhXZ4",
                   "sslLBq7nDWU",
                   "lOrHb3JU3GM",
                   "1wgFHZweC20",
                   "CD_tFnM6Yd0",
                   "jEfzdMymlgs",
                   "FR3NDWKNA44",
                   "nRWP65v1a1o",
                   "GVIz0O605cE",
                   "u6ybSSTe-9E",
                   "QV8BimeAvbc",
                   "oleQvBelq7Q",
                   "EgODdGPikgM",
                   "GB3aoOOhoOk",
                   "iMBBrWKJy2M",
                   "qxB3anjq4Pc",
                   "0qK7rgf_zIM",
                   "q26rES2f74s",
                   "OEUCO6Q-OpA",
                   "yhb0wy7rLik",
                   "Ebu1s7kwO_s",
                   "QsgZ-rk39ao",
                   "xMfvCBjXDuo",
                   "p2Ca0wvX4VA",
                   "DlsEYkqJdfs",
                   "0vPEsz_GySQ",
                   "lIOzQxUBjwA",
                   "cM6apns26UM",
                   "jRZ73fzM2ck",
                   "U-n1RlLBwYk",
                   "7ZroMrxvCec",
                   "BY8e6rzDiMM",
                   "6VmZoGLJNY0",
                   "US4wxqc-rko",
                   "1cvuzEwNuI",
                   "-1cvuzEwNuI",
                   "UcBuFEDjDdY",
                   "pXEHFjYuIOo",
                   "gX57i6w3mN4",
                   "ubtEoq5gW7U",
                   "q4Upt1JeRAo",
                   "RNeUc9DEdRY",
                   "wr2q5k0FX_Q",
                   "vuq_-8eZn0I",
                   "8aOQ_ghG7VQ",
                   "bQnOR-h3-TA",
                   "TonvLOhEv_U",
                   "fK8oxXwSeMY",
                   "2JPqRa42Wg8",
                   "kxQZAYGSngw",
                   "fAzb_qu4LBw",
                   "8zg8UtnavxI",
                   ],

        "Mc Poze do Rodo": ["BKDz5kNjkfU",
                            "t43c5QW4GXA",
                            "78aBsqmXdk4",
                            "n2vr0aGhvTc",
                            "ChsgqzH-df4",
                            "xAM51Ovpr9M",
                            "N9liPvylviE",
                            "FXRfr5-n4bY",
                            "Sr0jJpvfS10",
                            "LwPlWd48Erw",
                            "dRK7c3Je9ts",
                            "xidqdlywq-4",
                            "wIEKZ9LtkQg",
                            "RtRGjVtVVrQ",
                            "rL-DNYVEnyk",
                            "BzcIno-D0Es",
                            "rnhrtIfi-HU",
                            "QQQqkDD7i8Y",
                            "RFqN8xx-h30",
                            "rCNOcBT0UQM",
                            "Upa9zMs4vLo",
                            "uFn3iMKke4o",
                            "FGd8odSxAVs",
                            "SVkNr-NNWUc",
                            "bXxhkzS2Qa8"],

        "BIN": ["VF97zz_5oCc",
                "stjSIweo0UY",
                "cE-mBCBuxYQ",
                "RiYQ90oyYBw",
                "vbI5LcMXlS4",
                "T3MH_nbQWqU",
                "H3E0RVgCf3g",
                "VDPol9p7a78",
                "pPN2IQbF4xQ",
                "iGQuS_xB8p8",
                "8q1dfQh6Xvw",
                "LgUOExHk6sM",
                "f6kNhWc__FM",
                "CyvGw2j4b4k",
                "yV6nB16HDpg",
                "Hw8RPU08JHY",
                "_NDkLCgmIAQ",
                "-FJNrlvmqFA",
                "ZtYKMPlcu5o",
                "7HqJuWO-C2E",
                "FZvzCz-TPf8",
                "igYePv-u1JU",
                "Ux2KiWUGutc",
                "pBWbvMtgrZU",
                "0Bmw2aIyPFM",
                "ffVywcCk8tw",
                "KS34Zr1ln_c",
                "oCetq1T0Kcc",
                "RVGJjmyxbLQ",
                "syAzgYwnjwM",
                "DX3iaaeRjhg",
                "bKLQ_85g_qw",
                "asCif2QpK3s",
                "MVHNzf7nCio",
                "VCguOTknnaM",
                "PoTaBZpX15o",
                "m71BJoIA1lE",
                "k94tTv5l1zs",
                "rscpk2O2R4A"],

        "Borges": ["ba969xr3krs",
                   "o8PTLzCOAtc",
                   "LEyr3Dr93z8",
                   "xv8NrFQqKJ8",
                   "oFl6nZwxgxI",
                   "iY9s37ExYQk",
                   "yJcihkWwjys",
                   "37U5GWqKYMs",
                   "crJNdgAqTRQ",
                   "FMoMy3SIgFc",
                   "pPYMJQ_n8U8",
                   "MZ6kM3eVQB0",
                   "v-dLApGFbHE",
                   "b1CgF81-tiE",
                   "UxyvEfCmYXo",
                   "GvgKo6beWiI",
                   "8nAaHVotbZo",
                   "5gHdJ2B8_kg",
                   "ot-1uHlTQGI",
                   "c4XECQVA9qc",
                   "oZ5cXFJPXDA",
                   "tPcwYGqkFEA",
                   "nOF-ddKIkzA",
                   "yDIJx1Owkjo",
                   "3zFxj3KXsOQ",
                   "Xy7r7-mDqAk",
                   "ucOYbNa4c2c",
                   "feUZgQ3Ez-M",
                   "8KNnRc_XNwI",
                   "iJ6-iRnskYg",
                   "_wbye6pkX4I",
                   ""],

        "Chefin": ["PWWWqchekYA",
                   "RczgLo49ax4",
                   "kC2t1LSFIoA",
                   "0nHjG3mAYRI",
                   "TKvH8SO82kA",
                   "UMfswjxmLd4",
                   "Pan6MPs4B-c"],

        "Oruam": ["",
                  ""],

        "Bielzin": ["",
                    ""],

        "Dfideliz": ["8wEpHmPvcUo",
                     "RpEW3QWTLs8",
                     "7RT8tzF4xD0",
                     "JwpmnefxQdc",
                     "7eAUyzIcxD8",
                     "De-6OGeMdPU",
                     "gghjGr02028",
                     "YTOi0Yv-eVg",
                     "DGA2ZKctY4k",
                     "KOiL6i_ppuI",
                     "kaKwZHUySuI",
                     "NQRjkcC7kdQ",
                     "6TWAu-E4rno",
                     "kMPclgdIQVk",
                     "iDqhLy94iyc",
                     "O3eepDML3YM",
                     "CctOil1j-jE",
                     "MWG9gnRSKJM",
                     "ibx40dOoSLk",
                     "bmsILfH-UOw",
                     "xdCKBq47I5g",
                     "cMxckJbbXkE",
                     "pq9Xm8JCRfE",
                     "yBYToMWrlcI",
                     "f4e4syhXWPA",
                     "bB_LAfyBXJg",
                     "ZLjZxhrqmpQ",
                     "Gl4JxI5u8vc",
                     "EJlbSPLuR-o",
                     "BC1V_ANf_Nk",
                     "4sAQoR5cNOo",
                     "X3oypuWViAA",
                     "DrR51EhBe4I",
                     "MKi97BjQHWM",
                     "7CHiHnUIdVk",
                     "-ox5hZkTepI",
                     "-CqxJnnWDEs",
                     "pzt_4b07Zfc",
                     "GIkcbf9SL4k",
                     "jvfR8tegkFU",
                     "7NzVoQc3m4E",
                     "OOEhuuGSBFI",
                     "eIotmHIedtA",
                     "LvjHktS96Tc",
                     "K64UxOTqU2s",
                     "e6QwM1AvI_Y",
                     "Thkaao63Lj4",
                     "ZYzGJDW41p8",
                     "JeZ9AzZq4HU",
                     "WWPd1rEm3sc",
                     "evpszNoh7WA",
                     "FIG7dU_D604",
                     "7uj81peiv7o",
                     "wE0mtLuGdlE",
                     "2CszZ9FLwS8",
                     "XnobfnCsieA",
                     "r0k2DnRu-S8",
                     "e0a9GgGm81M",
                     "XNyBPsct2EQ",
                     "mAvwAVAvfz0",
                     "qufHBP7Ky54",
                     "DRODFs9IYiQ",
                     "-u8FUNPycHU",
                     "Mi2HlgdvlEs",
                     "ZBhOY8-QTO0",
                     "e2G-PGbKF3g",
                     "nDkCIyZv-Nc",
                     "z_d6XQTac8k"],

        "PL Quest": ["mJ2eHyAej9E",
                     "V7S5BYb93kE",
                     "4IKM9Cy9maA",
                     "NDaqfhvGfec",
                     "mOjzW3qLU-8",
                     "lCQsRfNKqow",
                     "aKTjSCn9x-8",
                     "RSTA5ZmJwVE",
                     "EcJgPAm9E1o",
                     "zcPITugjdc0",
                     "yc3seeyi9_M",
                     "Y8FPy5OVKsk",
                     "ZdJoa9FAWUc",
                     "YosJYGKHTPk",
                     "xJn-kTNV6Rk",
                     "FrnKOZzHXu4",
                     "j-ttUGgDk6U"],

        "Raffé": ["KgxkUDlvqgk",
                  "k8oC4WGZ-P0",
                  "LL6tyGmzkaU",
                  "e3gZqfhehYU",
                  ""],

        "Azevedo": ["aZLIddtdTqI",
                    "82i_3yCFjAI",
                    "KnIwJyThrlE",
                    "EoMoMBF52w0",
                    "o1r4YtfWlec",
                    "uHaDRs_9jT8",
                    "pF1AZHA1ziI",
                    "wyYnNPV4328",
                    "4CFaWELaFRE",
                    "lIFAB34-xkM",
                    "w1hfyMOWR1o",
                    "_Khl1cOnqT0",
                    "yp1GYpC3h_o",
                    "4cr9HDJsls4",
                    "cuu4KdTwfoU"],

        "Leviano": ["TFBJaHj1dec",
                    "07zbLlyvbik",
                    "tiha0w154Oo",
                    "JavGACaJx0Y",
                    "lbcMDCp0y-U",
                    "cDGlZgt8Hd4",
                    "OXIn1q_n0mQ",
                    "yUbGdm2myZQ",
                    "LFMjgePhD_Y",
                    "UJ835PU_DNs",
                    "iDCj3zwQXKs",
                    "PI23ldAvdHY",
                    "8wmj9eTLlbE", ],

        "Ajaxx": ["",
                  ""],

        "Kizzy": ["",
                  ""],

        "jess beats": ["ax-tF42susI",
                       "zADt7Ue9V08",
                       "ifxwPX6oLDo",
                       "cET1r_wwnKU"],

        "RUXN": ["",
                 ""],

        "MC Cabelinho": ["Ih145yJGgYI",
                         "honBVnBZhcw",
                         "pZ9b62d673k",
                         "xLsqTvidVYs",
                         "o5FCMvsWbUE",
                         "ZGdM4bkwpns",
                         "pXnBkL8KM48",
                         "Qi9x-bHBHco",
                         "Dm5gNA5by6A",
                         "x2YU_aUhXOs",
                         "eF1uLRJDj4g",
                         "En-CwT4lQDY",
                         "iBRLCkxCRVo",
                         "s8FgoxW-0Vs",
                         "7c4YSODoQQ4",
                         "D-6e2tc7vM0",
                         "hXDvjHhqGfY",
                         "ZhWc-dcQTOE",
                         "eURx7KkkwvA",
                         "jwZBK_UOMm0",
                         "1d2zXIe0Rgo",
                         "jJR-QdeBpNc",
                         "6_azlz9Ml0Y",
                         "PNy4OZ2zC2k",
                         "Ws63FBV88wE",
                         "iFHJN70-zmo",
                         "5e9MIBlbTcU",
                         "6WpdP0rSFXU",
                         "J0etIAMcktQ",
                         "SJHJTDhhlxs",
                         "UfMzmpmfGQU",
                         "Z9ebJvRWMCA",
                         "nMEb6iFH5Os",
                         "0Uv9uTEZOXI",
                         "8YWb7jhxAqI",
                         "NIkxE_aOFPg",
                         "_4hwYXTya8Q",
                         "MepOOHUzgHQ",
                         "5smpIrRff3U",
                         "gk4B0Vq91y0",
                         "VdJx1_wCRlk",
                         "-wzuNR3pAho",
                         "WKCPQpy_3tE",
                         "uxQ6hBo0HoE",
                         "mB8CrTw6Ns4",
                         "e9SsF-rkzy4",
                         "Tg9VAQW11Mk",
                         "STubgV_6q7w",
                         "Efzw6hAV9_M",
                         "hyDElqwFnYI",
                         "t-lq1zA2E7E",
                         "S69dAPMYjqU",
                         "yUpSiovjhnM",
                         "tsHm2C3WJrg",
                         "0lrMyAShAmw",
                         "BGl9t82kCt0",
                         "zgdQsLH7sDw",
                         "8JFcR_PQMpo",
                         "mZ0Snvc1rHE",
                         "GqLrlHHeww0",
                         "5t0J5Yt4eI0",
                         "Mi5yFTpgHfc",
                         "CNQzFRN1bXM",
                         "To2MAzO0VEE",
                         "093Ovkt8r9U",
                         "Kh9fYUUMK9U",
                         "Ustgnn6Xp0o",
                         "_CnuuV6Ts80",
                         "gGKSDD4cQ_U",
                         "S65UMvDriZU",
                         "pHTRk0KSsmo",
                         "iBmrml_5JFk",
                         "har3c93pJe0",
                         "yXFR8I2LTTI",
                         "casdq7FlO4g",
                         "kWvFoR-Wf-I",
                         "sQQsR3rTj2k",
                         "CIa80t2zTto",
                         "MYZnSUmdqRE"],

        "Brutos": ["gYrkZNNuH1I",
                   "eJmt8UaMe_s",
                   "HIDgjZ0HUfY",
                   "wsHKkc7GBzQ",
                   "DXPzFw_iAEA"],

        "A.R": ["",
                ],

        "Vinicin": ["",
                    ""],

        "MANO R7": ["xCxhPbhqluA",
                    "LAdJhwA8XIY",
                    "Pa85oEhsCP0",
                    "W4KFwVLuCTs",
                    "5y-ZQiNaiHI",
                    "kbfMqcZuB9k",
                    "Cu4rRaLskQI",
                    "eQAJP7bpxYk",
                    "8VvLHQ5xlpA",
                    "_eqyScmkxDI",
                    "ArE4plnORrQ",
                    "sB91C0Gpixo",
                    "Hjb74U48a68",
                    "aHW_nEuOlVc",
                    "DWIfl6ooTdw"],

        "Amorim": ["",
                   ""],

        "Buddy": ["bFr5jbgS_QI",
                  "W8kLLjLA5IA",
                  "zx08Qj7lQOg",
                  "ucwlLW3Xr-g",
                  "u507AFf8EqI",
                  "RdjZfatXp1k",
                  "sKPJzHl7GCA",
                  "RdjZfatXp1k",
                  "u507AFf8EqI",
                  "R-KhC0k8LVw",
                  "lEdZbzcyTAE"],

        "Mvk": [""],

        "Pedrin": ["1OfecIoUhFg",
                   "mv6P031PXi4",
                   "-LM5LEEP-j4",
                   "I_7xxia03Mk",
                   "r3YmPuUDYMA",
                   "QY3P87EBxZA",
                   "vhCo3RUJ4YM"],

        "Mc Filhão": ["0v33d3J_NZE",
                      "KbfiiH9DGFc"],

        "Shenlong": [""],

        "DEGE": ["nWfBYcJYChk",
                 "ze0EOmupiD0",
                 "5kGBq5pygz8",
                 "ofGUh7MX2vc",
                 "AJu6NwNvUOo",
                 "txXNqi76BDg",
                 "iExnrlDlK94",
                 "HirQxZUGz_A"],

        "Hashi": ["",
                  ""],

        "Beny Free": ["C_Q07I0x6Vg",
                      "biGfq7cAIi4",
                      "YHAhOfxLE2E"],

        "Feek": ["nx_msNDB4EM",
                 "Xddfo0V5-MY"],

        "Oliveira": [""],

        "Pior Versão de Mim": ["8Y_BPNY7zFQ",
                               "84PnmwCwXMI",
                               "tPegDfbgHUU",
                               "SxJgvzoNSm0",
                               "H9yCwS3hph0",
                               "k_-ay5i8cKg"],

        "Oreozin": ["C50dj_YJm5o"],

        "Peziinho": [""],

        "Grone": ["zcWw1Afpofc",
                  "E7ciakIFlhU",
                  "6azxQECdZPg",
                  "1jj1Ehv4Pes",
                  "ws1el3bwjbA",
                  "ZRQCS51yefI",
                  "M_rb_yE1kMo",
                  "c3QAV3oZ5Mc",
                  "MyyOhvcNJ2A",
                  "Vg0AvYu0nPU",
                  "BixDPcfl5BQ",
                  "_IhghxbcbUw",
                  "AvlNK3pz1Vo",
                  "-pWCBF-Bt3M",
                  "lqPoX4iyriY",
                  "9AYIXylQw7k",
                  "RRbDhqnm6o0"],

        "Vt no beat": ["TQ7YbiuhOYU",
                       "D2Vn7uPLyKE"]

    }


def calculate_total_views(video_manager, artist_videos):
    total_views = {}

    for artist, video_ids in artist_videos.items():
        print(f"\nCalculating total views for {artist}:")
        video_views = video_manager.get_video_views(video_ids)
        total_views[artist] = sum(video_info['views'] for video_info in video_views.values())

    return total_views


def export_to_csv(total_views):
    with open('data/yt_total_views.csv', 'w', newline='') as csvfile:
        fieldnames = ['Artist', 'Total Views']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for artist, views in total_views.items():
            writer.writerow({'Artist': artist, 'Total Views': views})
