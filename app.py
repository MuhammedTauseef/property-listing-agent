import streamlit as st

avg_rate = {"DHA": 30, "G-13": 45, "E-11": 60, "B-17": 15, "Bahria": 20, "Gulberg": 18}


def analyze(listing):
    words = listing.split()
    price_lac = 0
    size_marla = 0
    area = ""
    for i in range(len(words)):
        word = words[i].strip(".,")
        if word == "crore":
            price_lac = float(words[i - 1]) * 100
        if word == "lac" or word == "lakh":
            price_lac = float(words[i - 1])
        if word == "marla":
            size_marla = float(words[i - 1])
        if word == "kanal":
            size_marla = float(words[i - 1]) * 20
        if word == "sq":
            size_marla = float(words[i - 1]) / 272
    for a in avg_rate:
        if a in listing:
            area = a
    if size_marla == 0 or area == "" or price_lac == 0:
        return "unknown", 0, area
    rate = price_lac / size_marla
    if rate < avg_rate[area] * 0.9:
        return "deal", round(rate, 1), area
    return "normal", round(rate, 1), area


st.title("Property Deal Finder")
st.write("Listing paste karo, agent batayega achi deal hai ya nahi.")

listing = st.text_area("Listing:", height=120)

if st.button("Check karo"):
    if listing.strip():
        verdict, rate, area = analyze(listing)
        if verdict == "deal":
            st.success(f"GOOD DEAL! {area} — {rate} lac/marla")
        elif verdict == "normal":
            st.info(f"Normal price — {area} — {rate} lac/marla")
        else:
            st.warning("Samajh nahi aayi — price/size/area check karo")
    else:
        st.warning("Pehle listing likho")
