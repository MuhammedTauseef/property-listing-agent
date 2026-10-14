"""Property Listing Agent - daily deal report generator.

Reads listings from listings.txt, analyzes each one, writes verdicts to report.txt.
Run: python3 step12.py
"""

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
        return "unknown"
    rate = price_lac / size_marla
    if rate < avg_rate[area] * 0.9:
        return "deal"
    return "normal"


def main():
    with open("listings.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    with open("report.txt", "w") as out:
        out.write("Property Deal Report\n")
        out.write("====================\n")
        for line in lines:
            verdict = analyze(line)
            out.write(verdict + " - " + line + "\n")

    print("Report ban gayi: report.txt")


if __name__ == "__main__":
    main()
