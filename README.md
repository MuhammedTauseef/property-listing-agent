# Property Listing Agent

Islamabad property listings mein se achi deals nikalne wala Python agent.

## Kya karta hai
- Listing text se price, size (marla/kanal/sq-ft), area nikalta hai
- Per-marla rate ka area average se comparison kar ke GOOD DEAL flag karta hai
- Roz ki report `report.txt` mein likhta hai
- `app.py` mein Streamlit web frontend bhi hai

## Chalane ka tareeqa
1. Listings `listings.txt` mein daalo (har line ek listing)
2. `python3 step12.py` chalao
3. `report.txt` mein results dekho

## Web app
```
pip install streamlit
streamlit run app.py
```

## Eval
- Golden dataset: 5/5
- Stress test (10 tricky listings): 9/10

## Seekha
Python basics, functions, file I/O, eval-driven development (test → gap → fix)

Built jointly with Muse as an FDE learning project.
