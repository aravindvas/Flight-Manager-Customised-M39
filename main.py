from dmanager import DataManager
from flightsearch import Flight
from datetime import datetime, timedelta
from notify import Notification

dmgr = DataManager()
sht = dmgr.get_des_data()
fs = Flight()
notmgr = Notification()

org_city = "CCU"

if sht[0]["iataCode"] == "":
    for ct in sht:
        ct["iataCode"] = fs.get_des_code(ct["city"])
    dmgr.des_data = sht
    dmgr.upd_des_codes()
    # print(sht)

# tmr = datetime.now() + timedelta(days=34)
tmr = datetime(year=2021, month=7, day=14)
# sixmo = datetime.now() + timedelta(days=43)
sixmo = datetime(year=2021, month=7, day=18)

for des in sht:
    fl = fs.checkf(
        org_city_cd= des["iataCode"],
        des_city_cd= org_city,
        frm_tm= tmr,
        to_tm= sixmo
    )
    if fl is None:
      continue
    if fl.fprice < des["lowestPrice"]:
            if fl.forigin_city2 is None:
                notmgr.sms(
                    msg2=f"🇮🇳  ✈️\nLow Price Alert!! 🔻 \nOnly ₹ {fl.fprice} 🤑 \nto fly "
                         f"From {fl.forigin_city}-{fl.forigin_port} 🛫 "
                         f"To {fl.fdes_city}-{fl.fdes_port} 🛬 "
                         f"\nOn {fl.fout_date} at {fl.fout_tm} "
                )
            else:
                notmgr.sms(
                    msg2=f"🇮🇳  ✈️\nLow Price Alert!! 🔻 \nOnly ₹ {fl.fprice} 🤑 \nto fly "
                         f"From {fl.forigin_city}-{fl.forigin_port} 🛫 "
                         f"To {fl.fdes_city}-{fl.fdes_port} 🛬 "
                         f"\nand From {fl.forigin_city2}-{fl.forigin_port2} 🛫 "
                         f"To {fl.fdes_city2}-{fl.fdes_port2} 🛬 "
                         f"\nOn {fl.fout_date} at {fl.fout_tm} "
                         f"and On {fl.fout_date2} at {fl.fout_tm2}."
                )

