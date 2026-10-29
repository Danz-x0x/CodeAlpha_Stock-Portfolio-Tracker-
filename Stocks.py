import csv

def portfolio():
    sp = {"AAPL": 180, "TSLA": 250}
    pf = {}
    while True:
        s = input("Stock name (or 'done'): ").upper()
        if s == "DONE":
            break
        if s in sp:
            q = int(input("Quantity: "))
            pf[s] = pf.get(s, 0) + q
        else:
            print("Stock not found.")
            
    tot = sum(sp[k] * v for k, v in pf.items())
    print(f"Total Investment: {tot}")
    
    with open("portfolio.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Stock", "Quantity", "Price", "Total Value"])
        for k, v in pf.items():
            w.writerow([k, v, sp[k], sp[k] * v])
        w.writerow(["Total", "", "", tot])
    print("Saved to portfolio.csv.")

portfolio()